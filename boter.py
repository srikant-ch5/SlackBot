import os
import time
from slackclient import SlackClient

BOT_ID = "U4A5X6TAN"

AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


#this function will handle the commands which are being passed to the bot
def handle_command(command,channel):
    """
       Recieves commands directed at the bot and determines if they are valid commads
    """

    response = "Not sure what you are talking about .Use the *" + EXAMPLE_COMMAND + "* to start getting the boter in action"

    if command.startswith(EXAMPLE_COMMAND):
         response = "Come on dude write some more code Seriously!"
    slack_client.api_call("chat.postMessage",channel = channel,text=response,as_user = True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an event firehouse
        this parsing funciton returns None unless a message is been sent to out boter
    """

    output_list =  slack_rtm_output

    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                #return the text removing the @ and the whitespace
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    
    return None,None

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 sec of delay to read from firehouse

    if slack_client.rtm_connect():
        print("Boter has been connected and its running")

        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command,channel)
            time.sleep(READ_WEBSOCKET_DELAY)

    else:
        print("Connection failed Invalid Slack Token or bot id")

        
