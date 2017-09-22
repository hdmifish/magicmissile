#!/usr/bin/python3.5
import discord


class MagicMissile(discord.Client):

	def __init__(self, dev=False):
		try:
			print("This is a test...", end='')
		except Exception as e:
			print("error: " + str(e))
		else:
			print("Worked!")



	    def run(self):
	        try:
	            super().run(self.config.token, bot=not self.config.get("selfbot"))
	        except AttributeError as e:
	            log.err("Could not connect using the token provided: " + str(e))
	            exit(1)

	        except discord.errors.LoginFailure as e:
	            log.err("Authenication Failure. Your auth: \n"
	                    + str(self.config.token)
	                    + " is invalid " + str(e))
	            exit(401)
	        return


if __name__ == "__main__":
	client = MagicMissile()
	print("Running as main")
