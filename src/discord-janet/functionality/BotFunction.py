from abc import ABC, abstractmethod

__all__ = ["BotFunction"]

class BotFunction(ABC):

    def __init__(self):
        pass

    def setString(self, outputMessage):
        self.outputMessage = outputMessage

    async def execute(self, message, client):
        await message.channel.send(self.outputMessage)