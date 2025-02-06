from django.shortcuts import render, redirect
from django.conf import settings
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import spotipy
from spotipy.exceptions import SpotifyException

sp_auth = SpotifyOAuth(
    client_id=settings.SPOTIPY_CLIENT_ID,
    client_secret=settings.SPOTIPY_CLIENT_SECRET,
    redirect_uri=settings.SPOTIPY_REDIRECT_URI,
    scope="user-top-read user-library-read",
)


def get_top_tracks(sp):
    top_tracks = sp.current_user_top_tracks(limit=10, time_range="medium_term")["items"]
    print("Top Tracks:", top_tracks)
    return top_tracks


def get_recommendations(sp, top_tracks):
    try:
        top_tracks_id = [track["id"] for track in top_tracks]
        if not top_tracks_id:
            raise ValueError("No valid track IDs found for recommendations.")
        
        recommendations = sp.recommendations(seed_tracks=top_tracks_id[:5], limit=10)["tracks"]
        return recommendations
    except SpotifyException as e:
        print(f"Spotify API Error: {e}")
        return []  # Return an empty list or handle the error as needed


# the view that displays hte top tracks and recommendations
def index(request):
    # check if the user is authenticated by looking for the 'token_info' in the session
    if not request.session.get("token_info"):
        return redirect("login")

    # retrieve the token info
    token_info = request.session.get("token_info")
    # create a spotify client using the token
    sp = Spotify(auth=token_info["access_token"])

    # get user top tracks
    top_tracks = get_top_tracks(sp)

    # reccomendation based on top tracks
    recommendations = get_recommendations(sp, top_tracks)

    return render(
        request,
        "index.html",
        {"top_tracks": top_tracks, "recommendations": recommendations},
    )


def login(reqeust):
    auth_url = sp_auth.get_authorize_url()
    return redirect(auth_url)


def callback(request):
    # retrieve the auth code from the request query
    auth_code = request.GET.get("code")
    # exchange auth code for access token
    token_info = sp_auth.get_access_token(auth_code)
    # store token info in session to use for auth requests
    request.session["token_info"] = token_info
    return redirect("index")