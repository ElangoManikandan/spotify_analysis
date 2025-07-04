from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re

#Set up Client credentials
sp=spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="2ccd6c6e2f7b45109a3675d26bfbb918",client_secret="2f13fab3dd7d4fb3a2cad7eac34da90f"))
track_url="https://open.spotify.com/track/003vvx7Niy0yvhvHt4a68B"

track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)
track=sp.track(track_id)
print(track)
track_data={
    'Track Name': track['name'],
    'Artist': track['artists'][0]['name'],
    'Album': track['album']['name'],
    'Popularity': track['popularity'],
    'Duration (minutes)': track['duration_ms']/60000
}
#Display metadata
print(f"\n Track Name: {track_data['Track Name']}")
print(f" Artist: {track_data['Artist']}")
print(f" Album: {track_data['Album']}")   
print(f" Popularity: {track_data['Popularity']}")
print(f" Duration: {track_data['Duration (minutes)']:.2f} minutes")

#convert metadata to DataFrame
df = pd.DataFrame([track_data])
print("\n Track Data as DataFrame:")
print(df)

#Save DataFrame to CSV
df.to_csv('track_data.csv', index=False)

#Visualize Track Data
features = ['Popularity', 'Duration (minutes)']
values = [track_data['Popularity'], track_data['Duration (minutes)']]


plt.figure(figsize=(8, 5))
plt.bar(features, values, color='SkyBlue',edgecolor='black')
plt.title(f"Track Metadata for '{track_data['Track Name']}'")
plt.ylabel("Value")
plt.show()
 
 