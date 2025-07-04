import re
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import mysql.connector

# Set up Client credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="2ccd6c6e2f7b45109a3675d26bfbb918",
    client_secret="2f13fab3dd7d4fb3a2cad7eac34da90f"
))

# Connect to MySQL database
db_config = { 
    'host': 'localhost',
    'user': 'root',
    'password':'87654321',
    'database': 'spotify_db'
}

# Connect to the database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

#Read track URLs from the file
with open('spotify_tracks_list.txt', 'r') as file:
    track_urls = file.readlines()

# Process each track URL
for track_url in track_urls:
    track_url = track_url.strip()
    if not track_url:
        continue  # Skip empty lines
    try:
    # Extract track ID from URL
        track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)

    # Fetch track data from Spotify
        track = sp.track(track_id)

    # Extract metadata
        track_data = {
        'Track Name': track['name'],
        'Artist': track['artists'][0]['name'],
        'Album': track['album']['name'],
        'Popularity': track['popularity'],
        'Duration (minutes)': track['duration_ms'] / 60000
        }

    # Insert track data into MySQL database
        insert_query = """
        INSERT INTO spotify_tracks (track_name, artist, album, popularity, duration_minutes) VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
        track_data['Track Name'],
        track_data['Artist'],
        track_data['Album'],
        track_data['Popularity'],
        track_data['Duration (minutes)']
        ))
        connection.commit()
        print(f"Track '{track_data['Track Name']}' by {track_data['Artist']} has been inserted into the database.")
    except Exception as e:
        print(f"Error processing track URL '{track_url}': {e}")
# Close the cursor and connection
cursor.close()
connection.close()
