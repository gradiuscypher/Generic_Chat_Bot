import pickle
import os.path

class Scoreboard:
    def __init__(self):
        print "Initialized Scoreboard lib"

        self.file_name = 'libs/scoreboard.dat'
        if os.path.isfile(self.file_name):
            self.sb = pickle.load(open(self.file_name, "rb"))
        else:
            self.sb = {}

    def addPoints(self, user, value):
        print "Added", value, "to", user

        if user in self.sb.keys():
            self.sb[user] = int(self.sb[user]) + int(value)
        else:
            self.sb[user] = int(value)

        self.saveBoard(self.sb)

    def exportToPastebin(self):
        print "Scoreboard URL is:"

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
