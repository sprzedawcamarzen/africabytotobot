import time
from atproto import Client

# Lyrics from "Africa" by Toto
lyrics = [

"There's nothing that a hundred men or more could ever do",
  "I bless the rains down in Africa",
  "Gonna take some time to do the things we never had",
  "The wild dogs cry out in the night",
  "As they grow restless longing for some solitary company",
  "I know that I must do what's right",
  "As sure as Kilimanjaro rises like Olympus above the Serengeti",
  "I seek to cure what's deep inside",
  "Frightened of this thing that I've become",
  "It's gonna take a lot to drag me away from you",
  "There's nothin' that a hundred men or more could ever do",
  "I bless the rains down in Africa",
  "Gonna take some time to do the things we never had, ooh-hoo",
  "I hear the drums echoing tonight",
  "But she hears only whispers of some quiet conversation",
  "She's coming in, 12:30 flight",
  "The moonlit wings reflect the stars that guide me towards salvation",
  "I stopped an old man along the way",
  "Hoping to find some old forgotten words or ancient melodies",
  "He turned to me as if to say",
  "'Hurry boy it's waiting there for you'",
  "It's gonna take a lot to drag me away from you",


]

# Bluesky credentials
USERNAME = "africabytoto.bsky.social"
PASSWORD = "AfricaByToto1906"

# Initialize the Bluesky client
client = Client()
client.login(USERNAME, PASSWORD)

def post_lyric(lyric):
    """Post a lyric to Bluesky."""
    try:
        client.send_post(text=lyric)
        print(f"Posted: {lyric}")
    except Exception as e:
        print(f"Error posting lyric: {e}")

def main():
    current_line = 0
    while True:
        # Post the current lyric
        post_lyric(lyrics[current_line])

        # Move to the next lyric
        current_line = (current_line + 1) % len(lyrics)

        # Wait for an hour before posting the next lyric
        time.sleep(5400)

if __name__ == "__main__":
    main()