import re
import functionality as fn

serverID = "600896271900737599"

def IsFromThisServer(message):
    if (message.guild.id == serverID):
        return True
    else:
        return False


def Interpret(message):
    print('Interpreting chairman message')
    prettyMessage = message.clean_content

    roleUpgradeRegex = r"@Janet (please )?(would|will) you get @([^\s]*) a chair([.])?"
    result = re.search(roleUpgradeRegex, prettyMessage)
    if result:
        return fn.promoteChairman()