import configparser
import os
import subprocess
import sys
from datetime import datetime

import paramiko
import pyperclip


def read_in():
    """Read raw data from stdin."""
    return sys.stdin.buffer.read()


def show_message(text):
    subprocess.Popen(['notify-send', text])
    return


dirname = os.path.dirname(__file__)
config_path = os.path.join(dirname, 'config.ini')

# read config
config = configparser.ConfigParser()
config.sections()
config.read(config_path)

# connect to server
t = paramiko.Transport((
    config['server']['host'],
    int(config['server']['port']),
))
t.connect(
    username=config['credentials']['username'],
    password=config['credentials']['password'],
)
sftp = paramiko.SFTPClient.from_transport(t)

# generate new file name
screen_name = datetime.now().strftime(config['other']['name_pattern'])
new_url = config['other']['url_pattern'].format(
    host=config['server']['host'],
    username=config['credentials']['username'],
    port=config['server']['port'],
    screen_name=screen_name,
)

with sftp.open(screen_name, "wb") as f:
    f.write(read_in())

# copy url to clipboard
pyperclip.copy(new_url)

# show popup
show_message("File uploaded and url copied to clipboard: \n" + new_url)
