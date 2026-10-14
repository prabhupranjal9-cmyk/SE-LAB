
"""A simple music catalog with playlist and play-count operations."""

import json
import secrets
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    """
    CREATE TABLE songs (
        id INTEGER PRIMARY KEY,
        title TEXT,
        artist TEXT,
        plays INTEGER
    )
    """
)


def add_song(title, artist, plays=0, playlist=None):
    """Add a song to the catalog and its title to the playlist."""
    if playlist is None:
        playlist = []

    conn.execute(
        "INSERT INTO songs (title, artist, plays) VALUES (?, ?, ?)",
        (title, artist, plays),
    )
    playlist.append(title)
    return playlist


def shuffle_pick():
    """Return a randomly selected song ID, or None if the catalog is empty."""
    ids = [row[0] for row in conn.execute("SELECT id FROM songs")]
    return secrets.choice(ids) if ids else None


def popularity(title):
    """Return the popularity category for a song title."""
    row = conn.execute(
        "SELECT plays FROM songs WHERE title = ?", (title,)
    ).fetchone()

    if row is None:
        return "unknown"
    return "popular" if row[0] > 100 else "niche"


def save_playlist(playlist):
    """Serialize a playlist to a JSON string."""
    return json.dumps(playlist)


def load_playlist(data):
    """Deserialize a playlist from a JSON string."""
    return json.loads(data)


def total_plays():
    """Return the total number of plays across all songs."""
    result = conn.execute("SELECT SUM(plays) FROM songs").fetchone()[0]
    return result if result is not None else 0


def main():
    """Run a demonstration of the music catalog."""
    playlist = add_song("Aurora", "Nila", 250)
    add_song("Monsoon", "Kavya", 40, playlist)

    data = save_playlist(playlist)
    loaded_playlist = load_playlist(data)

    if len(loaded_playlist) > 1:
        print("multi-song playlist")

    print(
        popularity("Aurora"),
        popularity("Monsoon"),
        shuffle_pick(),
        total_plays(),
    )


if __name__ == "__main__":
    main()
