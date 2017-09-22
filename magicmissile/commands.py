import discord
import asyncio

class Commands:

    """
    Pretty cool thing with which to store commands
    """
    def __init__(self, client):
        self.client = client
        self.config = client.config


    def isNumeric(self, message):
        try:
            int(message.content)
        except ValueError:
            return False
        else:
            return True

    def cleanInput(self, input):

        args = input[len(input.split()[0]):].split('|')
        newargs = []
        for i in args:
            newargs.append(i.strip())

        return newargs

    async def hello(self, message):
        """
        This is a test, its a test
        """
        if message.author.id == self.config.owner:
            return "Hello boss! How's it going?"
        else:
            return "Hey there!"
