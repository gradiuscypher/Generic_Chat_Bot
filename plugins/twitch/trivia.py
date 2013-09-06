## This is an example file for how all IRC modules should be
## Name of the module, to be returned in desc()
import sqlite3
import sys
import libs.load_temp as temp
from libs.permissions import Permissions
from libs.scoreboard import Scoreboard

db = sqlite3.connect('plugins/twitch/questions.sqlite')
c = db.cursor()
name = "trivia.py"
t_file = "plugins/twitch/trivia.tmp"
data = temp.load_temp(t_file)
perm = Permissions()
sb = Scoreboard()

def buildup(send_message_callback):
    print "This function is run at buildup of function."
    global send_message_function
    send_message_function = send_message_callback

def send_input(inp, sender, channel):
    if inp == "trivia" and data["asked"] == "false" and perm.isMod(sender):
        trivia_question(channel)

    if data["asked"] == "true":
        trivia_answer(channel,inp,sender)

    if len(inp.split()) == 2 and inp.split()[0] == "trivia" and perm.isMod(sender):
        send_message_function(channel,"Starting a trivia loop of " + inp.split()[1] + " questions.")
        data["loop"] = "true"
        data["loop_count"] = str(int(inp.split()[1]) - 1)
        trivia_question(channel)

def desc():
    return ""

def teardown():
    print "Removing the Trivia module."

def trivia_question(channel):
    ans = ""

    if data["asked"] == "false":
        try:
            c.execute("select question,answer from questions order by random() limit 1")
            s = c.fetchone()
            data["answer"] = s[1]
            ans = s[0].encode('ascii', 'ignore')
            data["asked"] = "true"
            temp.save_temp(t_file, data)
        except:
            print "Error generating question:", sys.exc_info()

        send_message_function(channel,ans)

def trivia_answer(channel,message,sender):
        if str.lower(message) == str.lower(str(data['answer'])):
            data["asked"] = "false"
            temp.save_temp(t_file, data)
            send_message_function(channel,"You are correct " + sender + "!")
            sb.addPoints(sender, 10)

            if data["loop"] == "true" and int(data["loop_count"]) == 0:
                data["loop"] = "false"
                send_message_function(channel,"I'm done with my trivia spree now.")
                temp.save_temp(t_file, data)

            if data["loop"] == "true" and int(data["loop_count"]) != 0:
                data["loop_count"] = str(int(data["loop_count"]) - 1)
                temp.save_temp(t_file, data)
                trivia_question(channel)
