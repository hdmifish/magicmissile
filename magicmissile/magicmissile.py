#!/usr/bin/python3.5
import discord
import asyncio
from .config import Config
from .grasslands import Peacock
from .commands import Commands
log = Peacock()
class MagicMissile(discord.Client):

    def __init__(self, dev=False):
        try:
            super().__init__()
            self.config = Config()
            self.commands = Commands(self)
            print("This is a test...", end='')
        except Exception as e:
            print("error: " + str(e))
        else:
            print("Worked!")



    def run(self):
        try:
            super().run(self.config.token, bot=True)
        except AttributeError as e:
            log.err("Could not connect using the token provided: " + str(e))
            exit(1)

        except discord.errors.LoginFailure as e:
            log.err("Authenication Failure. Your auth: \n"
                    + str(self.config.token)
                    + " is invalid " + str(e))
            exit(401)
        return

    def isPM(self, message):
        if message.channel.is_private:
            return True
        else:
            return False

    def removePrefix(self, input):
        return input[len(input.split()[0]):]

    def getMainServer(self):
        if len(self.servers) == 0:
            log.err("This client is not a member of any servers")
            exit(404)


    async def on_ready(self):
        """
        Called once a connection has been established
        """
        log.ready("Running discord.py version: " + discord.__version__)
        log.ready("Connected to Discord!")
        log.info("Logged in as {0.name}.{0.discriminator} ({0.id})"
                 .format(self.user))
        log.info("Prefix: " + self.config.prefix)

        return

    async def send_message(self, channel, message, timeout=0):
        """
        Overload on the send_message function"
        """
        # TODO: Make this do things
        return await super().send_message(channel, message)

    async def send_embed(self, channel,  embedded):
        return await super().send_message(channel, embed=embedded)


    async def on_member_join(self, member):
        log.info(member.name + " joined!")
        return True

    async def on_member_remove(self, member):
        log.info(member.name + " left!")
        return True

    async def on_message_delete(self, message):
        #to run on message Delete
        return True

    async def on_message_edit(self, before, after):
         #to run on message edit
        return True

    async def on_message(self, message):
        await self.wait_until_ready()
        content = message.content.strip()

        if not message.channel.is_private:
            return

        if message.author == self.user:
            return
        if message.content == self.config.prefix:
            return


        if not content.startswith(self.config.prefix):
            return
        com = content[len(self.config.prefix):].lower().strip()


        if com.split()[0] in dir(self.commands):
            methodToCall = getattr(self.commands, com.split()[0])
            if methodToCall.__doc__ is None:
                log.warn("All commands require a docstring to not be " +
                         "ignored. If you dont know what caused this, " +
                         "it's safe to ignore the warning.")
                return
            log.com("[{0}] [{1}] [{1.id}] [{2}] ".format(message.channel,
                                                         message.author,
                                                         com))

            response = await methodToCall(message)
            if response:
                self.config.get("stats")["comCount"] += 1
                await self.send_message(message.channel, response)
                return


if __name__ == "__main__":
    client = MagicMissile()
    print("Running as main")
