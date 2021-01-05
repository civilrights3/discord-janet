import discord
import re
import functionality as fn
import language.civilLanguage as civil
import language.genericLanguage as generic
import language.chairmanLanguage as chairman

# TODO: write a proper parsing of sentences
def Interpret(message):
    print('Routing interpretation')
    returnResult = None

    if civil.IsFromThisServer(message):
        returnResult = civil.Interpret(message)

    if chairman.IsFromThisServer(message):
        returnResult = chairman.Interpret(message)

    # Nothing server specific, lets try general
    # if not returnResult:
        # returnResult = generic.Interpret(message) No commands exist yet. uncomment later

    # Default answer when we dont understand the command
    print('Before default', returnResult)
    if not returnResult:
        returnResult = MakeCommandNotFound()
    print('After default', returnResult)
    return returnResult

def MakeCommandNotFound():
    returnResult = fn.BotFunction()
    returnResult.setString('I\'m sorry, I don\'t understand :)')
    return returnResult
