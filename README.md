
# 🎵 Spotify Track Metadata Analysis

This project allows you to extract metadata of tracks from Spotify using the [Spotipy](https://spotipy.readthedocs.io/) API and optionally store the data in a MySQL database. It supports single-track analysis, batch processing of multiple tracks from a URL list, and visualizes track metadata.

## 📁 Project Structure

```
spotify_analysis/
│
├── main.py                    # Fetches a single Spotify track's metadata and visualizes it
├── spotify_mysql.py           # Extracts and inserts single track metadata into MySQL
├── spotify_mysql_urls.py      # Batch processes multiple track URLs and inserts into MySQL
├── spotify_tracks_list.txt    # List of Spotify track URLs (one per line)
├── track_data.csv             # Output CSV file with single track metadata
```

## 🧰 Requirements

- Python 3.7+
- Spotipy
- pandas
- matplotlib
- mysql-connector-python
- MySQL server (local or remote)

Install dependencies:

```bash
pip install spotipy pandas matplotlib mysql-connector-python
```

## 🔐 Spotify API Setup

You need Spotify Developer credentials to access the Web API:

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create an app to get the **Client ID** and **Client Secret**
3. Replace the credentials in each script:
   ```python
   SpotifyClientCredentials(
       client_id="YOUR_CLIENT_ID",
       client_secret="YOUR_CLIENT_SECRET"
   )
   ```

## 🛠️ How to Use

### 1. Analyze a Single Track and Plot (no database)
Run `main.py` to fetch metadata for a hardcoded Spotify track and visualize it:

```bash
python main.py
```

Output:
- Track metadata printed in console
- Bar chart of popularity and duration
- Saves metadata to `track_data.csv`

### 2. Insert a Single Track into MySQL

Before running, ensure a MySQL database and table exist:

```sql
CREATE DATABASE spotify_db;
USE spotify_db;

CREATE TABLE spotify_tracks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    track_name VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    popularity INT,
    duration_minutes FLOAT
);
```

Then run:

```bash
python spotify_mysql.py
```

### 3. Insert Multiple Tracks from URL List

Add your track URLs to `spotify_tracks_list.txt` (one per line). Then run:

```bash
python spotify_mysql_urls.py
```

Each track's metadata will be inserted into the `spotify_tracks` table.

## 📊 Sample Track Metadata Fields

- 🎵 Track Name
- 👤 Artist
- 💿 Album
- 🔥 Popularity (0–100)
- ⏱️ Duration (in minutes)

## ⚠️ Notes

- Be careful with API rate limits while processing multiple tracks.
- Error handling is included for failed track fetches or database issues.
- Ensure your MySQL user credentials match those in the scripts.

## 📌 License

MIT License
