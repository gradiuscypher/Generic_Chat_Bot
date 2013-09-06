from connectors.irc import IrcBot

irc = IrcBot("configs/twitch.cfg")
irc.bot_start()