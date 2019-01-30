import subprocess
import sys

import pyperclip
import notify2


def get_password_from_pass(password_path):
    """Get password from `pass` utility."""
    result = subprocess.check_output(['pass', 'show', password_path])
    return result.decode('utf-8').strip('\n')


def read_in():
    """Read raw data from stdin."""
    return sys.stdin.buffer.read()


def show_popup_message(title, text, app_name="Uploader"):
    # initialise the d-bus connection
    notify2.init(app_name)

    # create Notification object
    n = notify2.Notification(title)
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.set_timeout(notify2.EXPIRES_DEFAULT)
    n.update(title, text)
    n.show()


def copy_to_clipboard(text):
    # copy url to clipboard
    pyperclip.copy(text)
