import discord
import config
import language

client = discord.Client()

#Event hooks
@client.event
async def on_ready():
    print('We have successfully logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if talking_to_me(message):
        function = language.Interpret(message)
        print('function result: ', function)
        # await function.execute(message, client)

#Private functions
def talking_to_me(message):
    if message.author == client.user:
        return False

    print('Message Recieved - Content:', message.content)
    print('Message Recieved - Clean Content:', message.clean_content)

    # Make sure the message starts with the bot's userid
    if (message.clean_content.startswith("@Janet ")):
        return True
    
    return False

client.run(config.read_auth_key())