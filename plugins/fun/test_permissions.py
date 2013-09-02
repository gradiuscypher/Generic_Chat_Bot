## This is an example file for how all IRC modules should be
import time
from libs.permissions import Permissions

## Name of the module, to be returned in desc()
name = "test_permissions.py"
permissions = Permissions()

## What the module should return when processing text from IRC
## Gets inp from IRC, processes it, and returns the
def buildup(send_message_callback):
    print "This function is run at creation of the plugin"
    global send_message_function
    send_message_function = send_message_callback

def send_input(inp, sender, channel):

    if inp.split()[0] == "isMod":
        send_message_function(channel,"isMod:" + str(permissions.isMod(inp.split()[1])))

    if inp.split()[0] == "addMod" and permissions.isMod(sender):
        permissions.addMod(inp.split()[1])
        send_message_function(channel,"Added mod.")

    if inp.split()[0] == "remMod" and permissions.isMod(sender):
        permissions.remMod(inp.split()[1])
        send_message_function(channel,"Removed mod.")

    if inp == "listmods":
        send_message_function(channel,permissions.listMods())

## Returns a description of the module including the name at the top
def desc():
    return "Module name" + name + "Example Description"

def teardown():
    print "This function is run at removal of the plugin"
