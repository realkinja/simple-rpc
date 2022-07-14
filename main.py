from pypresence import Presence
import time
import json

with open("config.json", "r") as f:
    f = json.load(f)

client_id = f.get("client_id")
RPC = Presence(client_id=client_id)
RPC.connect()
state = f.get("state")
details = f.get("details")
largeimage = f.get("largeimage")
largetext = f.get("largetext")
smallimage = f.get("smallimage")
smalltext = f.get("smalltext")

RPC.update(state=state, details=details, large_image=largeimage, large_text=largetext, small_image=smallimage, small_text=smalltext)

while 1:
    time.sleep(15)