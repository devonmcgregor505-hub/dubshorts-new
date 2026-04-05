import sys, json
from youtube_transcript_api import YouTubeTranscriptApi
try:
    t = YouTubeTranscriptApi.get_transcript(sys.argv[1], languages=['en','en-US','en-GB'])
    print(' '.join([x['text'] for x in t]))
except Exception as e:
    print('')
