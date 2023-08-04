from pytube import YouTube

def download_video(url, output_path=None):
    try:
        # Create a YouTube object with the video URL
        yt = YouTube(url)

        # Get the highest resolution stream available (first stream in the list)
        video_stream = yt.streams.get_highest_resolution()

        # Set the output path for the downloaded video (default to current directory if not provided)
        if not output_path:
            output_path = "."

        # Download the video
        video_stream.download(output_path)

        print("Download successful!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
