import re
import functionality as fn

serverID = 600896271900737599

def IsFromThisServer(message):
    if (message.guild.id == serverID):
        return True
    else:
        return False


def Interpret(message):
    prettyMessage = message.clean_content

    # TODO: normalize message parsing. Remove pleasantries, normallize would/will.
    roleUpgradeRegex = r"@Janet\s+(please\s+)?(would|will)\s+you\s+(please\s+)?get\s+@([^\s]*)\s+a\s+chair([.?])?\s*"
    result = re.search(roleUpgradeRegex, prettyMessage)
    if result:
        return fn.promoteChairman()