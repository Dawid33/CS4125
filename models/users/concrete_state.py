# pylint: disable=too-few-public-methods
# pylint: disable=import-error
# pylint: disable=no-name-in-module

from models.users.user_state import *

class ActivesState(UserState):
    def send_message(self):
        print("Message Received")

    def access_resource(self):
        print("Access Granted")

class BlockedSate(UserState):
    def send_message():
        print("User is blocked")

    def access_resource():
        print("Denied. User is blocked")