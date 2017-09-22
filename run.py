#!/usr/bin/python3.5
from magicmissile import MagicMissile

import traceback
import os

os.system('')

bot = MagicMissile

try:
    bot.run()
except Exception as e:
    traceback.print_exc()
