# Song Recommendation System

A song recommendation system that leverages the Spotify API to fetch and recommend songs based on user preferences.

## Features

- **User Authentication**: Secure Spotify login using OAuth 2.0.
- **Top Tracks**: Fetch and display top tracks based on user listening history.
- **Recommendations**: Generate song recommendations based on top tracks.
- **Django Backend**: Built using Django for managing user sessions and displaying recommendations.

**Note**: This application is designed to run locally and is not publicly accessible on the internet. Spotify API calls are made using the credentials and tokens configured in your local environment. Steps to get API key are shown below.

## Installation

### Prerequisites

- Python 3.8 or later
- Django 4.x
- Spotipy library
- API client secret and ID

## API Setup

1. Navigate to [Spotify Developer Dashboard](https://developer.spotify.com/) and log in with your Spotify account.
2. Click on the dropdown in the top right corner and select "Dashboard," or go directly to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
3. Click "Create an App" and fill in the required details for 'App Name' and 'App Description'. Set the Redirect URI to `http://localhost:8000/callback` and check off 'Web API'.
4. Agree to the terms of service and save.

   After saving, you'll be redirected to the app settings. Click on "Settings" in the top right corner to access your Client ID and Client Secret. Keep these credentials safe as you'll need them later.

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/tab1shh/song-recommendation.git
   cd song-recommendation
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows use 'venv\Scripts\activate\
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   Create a '.env' file in the root directory with the following content:

   ```dotenv
   SPOTIPY_CLIENT_ID=your_spotify_client_id
   SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
   SPOTIPY_REDIRECT_URI=http://localhost:8000/callback
   DJANGO_SECRET_KEY=your_django_secret_key
   ```

   Replace the placeholder values with your actual Spotify credentials and Django secret key.

5. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**
   ```
   python manage.py runserver
   ```
   Access the application at by copy pasting the link given in terminal (most likley http://localhost:8000/)

### Usage

1. Navigate to http://localhost:8000/login to start the authentication process with Spotify.
2. After successful authentication, you'll be redirected to the home page where you can view your top tracks and receive recommendations based on them.

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Contact

For any questions or feedback, you can reach out to tabishghouri3@gmail.com

Thank you for checking out this project!
