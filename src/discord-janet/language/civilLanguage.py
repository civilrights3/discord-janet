import re
import functionality as fn

serverID = 331869022503174174

def IsFromThisServer(message):
    if (message.guild.id == serverID):
        return True
    else:
        return False


def Interpret(message):
    prettyMessage = message.clean_content

    giveawayRegex = r"@Janet (please )?start the giveaway([.])?"
    result = re.search(giveawayRegex, prettyMessage)
    if result:
        return fn.giveaway()