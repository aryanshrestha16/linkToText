from transcriptAI import generate_summary
from youtube_transcript_api import YouTubeTranscriptApi
import re

# This extracts the video ID token from a URL. Try/catch for when invalid URL is given. Only accepts Youtube URL. 
# Returns videoID otherwise keeps on asking for input until user force quits. 
def extract_videoID(url):
    while True:
        if "youtube.com" not in url.lower():
            print("Not a valid YouTube URL.")
            url = input("Enter a YouTube URL: ")
            continue
        try:
            video_id = re.search(r"v=([A-Za-z0-9_-]{11})", url).group(1)
            return video_id
        except AttributeError:
            print("Not a valid YouTube video ID.")
            url = input("Enter a YouTube URL: ")


# This function extracts the Youtube Transcript for the given video ID. Uses Youtube Transcript API.
# Returns numbered text otherwise return error. 
def get_transcript(video_id):
    try:
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ""
        for i, line in enumerate(transcript_data):
            text = line['text']
            transcript_text += f"{i+1}. {text}\n"
        return transcript_text
    except Exception as e:
        print("Error:", e)
        return None


def main():
    url = input("Enter a YouTube URL: ")
    video_id = extract_videoID(url)
    if video_id:
        transcript = get_transcript(video_id)
        if transcript:
            generate_summary(transcript)

if __name__ == "__main__":
    main()