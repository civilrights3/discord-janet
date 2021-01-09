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

    # TODO: normalize message parsing. Remove pleasantries, normallize would/will.
    roleUpgradeRegex = r"@Janet (please )?(would|will) you (please )?get @([^\s]*) a chair([.?])?"
    result = re.search(roleUpgradeRegex, prettyMessage)
    if result:
        return fn.promoteChairman()