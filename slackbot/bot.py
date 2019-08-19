from lyrics_extractor import Song_Lyrics
import os
import time
import numpy as np
import re
from slack import WebClient
import datetime

token = 'xoxp-718653270114-723720180593-730656138004-b42a3db0bf57886c3ba99372ecb96765'
#Connecting using access token
slack_client = WebClient(token)

#Checking the connection
bool = slack_client.rtm_connect(with_team_state=False)

events = slack_client.rtm_read()

#slack_client.api_call(“chat.postMessage”, channel=channel, text=t)

extract_lyrics = Song_Lyrics('AIzaSyDtY1j0Bezk8BXw_9SKAXWYG6EyAoDryI8', '004427544878426260376:axdgrmc-h0m')
song_title, song_lyrics = extract_lyrics.get_lyrics("Shape of You")
