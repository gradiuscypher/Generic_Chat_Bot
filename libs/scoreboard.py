import pickle
import os.path
import ConfigParser
import pastebin_python

class Scoreboard:
    def __init__(self):
        print "Initialized Scoreboard lib"

        self.file_name = 'libs/scoreboard.dat'
        if os.path.isfile(self.file_name):
            self.sb = pickle.load(open(self.file_name, "rb"))
        else:
            self.sb = {}

        config = ConfigParser.RawConfigParser()
        config.read('configs/twitch.cfg')
        pb_api = config.get('Settings', 'pb_api')
        self.paste = pastebin_python.PastebinPython(api_dev_key=pb_api)

    def addPoints(self, user, value):
        print "Added", value, "to", user

        if user in self.sb.keys():
            self.sb[user] = int(self.sb[user]) + int(value)
        else:
            self.sb[user] = int(value)

        self.saveBoard(self.sb)

    def exportToPastebin(self):
        post_string = "===== Scoreboard =====\n\n"
        for key in self.sb:
            post_string += "%-20.20s"%(key) + "%10d"%(self.sb[key]) + " points\n"

        url = self.paste.createPaste(post_string)
        return "Scoreboard URL is: " + url

    def getPoints(self, user):
        return str(self.sb[user])

    def remPoints(self, user, value):
        print "Removed", value, "from", user

        if user in self.sb.keys():
            self.sb[user] = int(self.sb[user]) - int(value)
        else:
            self.sb[user] = int(value)

        self.saveBoard(self.sb)

    def saveBoard(self, obj):
        pickle.dump(obj, open(self.file_name, "wb"))
