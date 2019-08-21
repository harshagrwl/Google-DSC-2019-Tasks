from lyrics_extractor import Song_Lyrics
import os
import time
import numpy as np
import re
from slack import WebClient
import datetime

slack_client = WebClient('xoxp-718653270114-723720180593-730656138004-b42a3db0bf57886c3ba99372ecb96765')
RTM_READ_DELAY = 1


def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """

    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            message = event["text"].lower()

            # Splitting user's message for comp_names
 
    return None, None

def handle_command(channel, message):
    """
        Executes bot command if the command is known
    """

    response = None
   

    if message.startswith("lyrics for "):
        get_song_name = message[11:]
        lyrics_gen = Song_Lyrics('AIzaSyDtY1j0Bezk8BXw_9SKAXWYG6EyAoDryI8','004427544878426260376:axdgrmc-h0m')
        song = lyrics_gen.get_lyrics(get_song_name)
        response = '*' + song[0] + '*' + '\n\n' + song[1].replace('<br>','\n')

        slack_client.api_call(
            "chat.postMessage",
            channel = channel,
            text = response,
        )


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")

        # Read bot's user ID by calling Web API method `auth.test`
        # starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            try:
                channel, message = parse_bot_commands(slack_client.rtm_read())
                if message:
                    handle_command(channel, message)
                    # h_cmd = threading.Thread(target=handle_command, args=(channel, message))
                    # h_cmd.start()
                time.sleep(RTM_READ_DELAY)
            except Exception as e:
                print("Reconnecting..." + str(e))
                slack_client.rtm_connect(with_team_state=False)
    else:
        print("Connection failed. Exception traceback printed above.")