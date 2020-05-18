# Script for updating config files
# What config files do I need to grab?
# - i3 config
# - polybar config
# - custom scripts


import os
from shutil import copy, copytree, rmtree

# Pull i3 config
copy("/home/grim/.i3/config", "./i3")
copy("/home/grim/.i3/polybar_config", "./i3")

# Pull polybar config
rmtree("./polybar")
copytree("/home/grim/.config/polybar", "./polybar")
