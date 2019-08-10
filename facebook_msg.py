########################### Import
import fbchat
from getpass import getpass
from fbchat.models import *
import warnings

########################### control panel
FRIENDS_NUM = 5
blocklist = [
"Mahammad Abul-Soad",
"Ahmed Abas"
]
msg = "كل سنة و انتم طيبين <3"


########################### connecting to facebook
username = str(input("Username: "))
client = fbchat.Client(username, getpass())
print("Getting users ...")
users = client.fetchThreads(thread_location=ThreadLocation.INBOX, limit=FRIENDS_NUM)

########################### main
if __name__ == '__main__':
    for i in range(FRIENDS_NUM):
        if users[i].type == ThreadType.USER:
            if users[i].name not in blocklist:
                print("Sending Message to user {}/{}\n".format(i+1, FRIENDS_NUM))
                client.send(Message(text=msg), thread_id=users[i].uid, thread_type=ThreadType.USER)
