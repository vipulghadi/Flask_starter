from youtube_transcript_api import YouTubeTranscriptApi # type: ignore



def extract_video_id(url):
    # Check if the URL contains 'youtu.be/' format
    if 'youtu.be/' in url:
        video_id_index = url.index('youtu.be/') + len('youtu.be/')
        video_id = url[video_id_index:].split('?')[0]
        return video_id
    # Check if the URL contains 'watch?v=' format
    elif 'watch?v=' in url:
        video_id_index = url.index('watch?v=') + len('watch?v=')
        video_id = url[video_id_index:].split('&')[0]
        print(video_id)
        return video_id
    # If the URL format is not recognized
    else:
        return None
    
def get_video_transcript(url):
        video_id=extract_video_id(url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id,languages=["en","hi"])
        transcript_text = ' '.join([entry['text'] for entry in transcript])
        return transcript_text