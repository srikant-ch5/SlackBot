import os
from slackclient import SlackClient

BOT_NAME = 'boter'

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

print(slack_client)

if __name__ == '__main__':
    api_call = slack_client.api_call("users.list")

    if api_call.get('ok'):
        #retrieve all users to find our bot

        users = api_call.get('members')

        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                print("BOT id for '"+user['name'] + "' is " + user.get('id'))

    else :
        print("are you a hacker?")
