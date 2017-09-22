"""
Grasslands is a semi-public module for colored logging
"""

from datetime import datetime as dt
from random import randint
from colorama import init, Fore
import requests


class Peacock(object):
    def __init__(self, painter=None):
        init()

    def timestamp(self):
        return "[{}]".format(str(dt.utcnow())[:-7])

    def log(self, message):
        print(Fore.WHITE + "[LOG] " + self.timestamp() + " " +
              message.encode('ascii', 'ignore').decode('ascii') + Fore.RESET)
        return

    def warn(self, message):
        print(Fore.YELLOW + "[WARN] " + self.timestamp() +
              " " + message.encode('ascii', 'ignore').decode('ascii')
              + Fore.RESET)
        return

    def err(self, message):
        print(Fore.RED + "[ERROR] " + self.timestamp() + " " +
              message.encode('ascii', 'ignore').decode('ascii')
              + Fore.RESET)

    def info(self, message):
        print(Fore.CYAN + "[INFO] " + self.timestamp() + " " +
              message.encode('ascii', 'ignore').decode('ascii')
              + Fore.RESET)

    def com(self, message):
        print(Fore.BLUE + "[COMMAND] " + self.timestamp() + " " +
              message.encode('ascii', 'ignore').decode('ascii')
              + Fore.RESET)

    def member(self, message):
        print(Fore.CYAN + "[MEMBER] " + self.timestamp() + " " +
              message.encode('ascii', 'ignore').decode('ascii')
              + Fore.RESET)

    def debug(self, message):
        print(Fore.MAGENTA + "[DEBUG] " + self.timestamp() + " " +
              message.encode('ascii', 'ignore').decode('ascii')
              + Fore.RESET)

    def ready(self, message):
        print(Fore.GREEN + "[READY] " + self.timestamp() + " " +
              message.encode("ascii", "ignore").decode('ascii')
              + Fore.RESET)

    def f(self, func="basic", message=""):
        print(Fore.MAGENTA + "[FUNC/{}] ".format(func.upper())
              + self.timestamp() + " " +
              message.encode("ascii", "ignore").decode('ascii') + Fore.RESET)
