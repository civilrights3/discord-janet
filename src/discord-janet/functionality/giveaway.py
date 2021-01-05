import time
from functionality import BotFunction

__all__ = ["giveaway"]

class giveaway(BotFunction.BotFunction):

    def __init__(self):
        pass

    async def execute(self, message, client):
        dest = message.channel

        time.sleep(10)
        await dest.send('#giveaways')
        time.sleep(2)
        await dest.send('cancel')
        # Test sending messages + delays
        # await dest.send('Hello! Testing message 1.')
        # time.sleep(2)
        # await dest.send('Hello! Testing message 2.')
        return