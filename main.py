import configparser
import os
import uuid
from datetime import datetime

from lib import (
    SFTPUploader,
    copy_to_clipboard,
    read_in,
    show_popup_message,
    get_password_from_pass,
)

# read config
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)

# get password
password = get_password_from_pass(config['credentials']['password_path'])

# connect to sftp
uploader = SFTPUploader(
    host=config['server']['host'],
    port=int(config['server']['port']),
    username=config['credentials']['username'],
    password=password,
)

# generate new file name
date = datetime.now().strftime(config['other']['date_format'])
screen_name = config['other']['name_pattern'].format(
    date=date,
    rand=uuid.uuid4().hex[:5],
)
screen_url = config['other']['url_pattern'].format(
    host=config['server']['host'],
    port=config['server']['port'],
    username=config['credentials']['username'],
    screen_name=screen_name,
)

data = read_in()
uploader.save(screen_name, data)

# copy file url to clipboard
copy_to_clipboard(screen_url)

# show popup
show_popup_message(
    "Screen uploaded",
    "File uploaded and url copied to clipboard: \n" + screen_url
)
