name = "scoreboard_mod.py"
from libs.permissions import Permissions
from libs.scoreboard import Scoreboard

p = Permissions()
sb = Scoreboard()

def buildup(send_message_callback):
    print "This function is run at creation of the plugin"
    global send_message_function
    send_message_function = send_message_callback

def send_input(inp, sender, channel):
    if p.isMod(sender) and inp.split()[0] == "@points":
        if inp.split()[1] == "add":
            sb.addPoints(inp.split()[2],inp.split()[3])
        if inp.split()[1] == "rem":
            sb.remPoints(inp.split()[2],inp.split()[3])
        if inp.split()[1] == "get":
            send_message_function(channel,sb.getPoints(inp.split()[2]))
        if inp.split()[1] == "board":
            send_message_function(channel,sb.exportToPastebin())

## Returns a description of the module including the name at the top
def desc():
    return "Module name" + name + "Example Description"

def teardown():
    print "This function is run at removal of the plugin"
