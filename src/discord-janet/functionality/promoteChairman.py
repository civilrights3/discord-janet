from discord.utils import get
from functionality import BotFunction
import emoji

__all__ = ["promoteChairman"]

roleName = "Chairmen"

class promoteChairman(BotFunction.BotFunction):

    NotPermittedMessage = "I'm sorry {user}. You don't have permission to do that. If you like, I can get you another chair instead. {smile}"
    ErrorMessage        = "There appears to have been an error {user}. This will have to be done the old-fashioned way. {e}"
    SuccessMessage      = "Welcome {user} to Chairodynamic! Please, have a seat. It is freshly created from nothingness! {smile}"

    def __init__(self):
        pass

    async def execute(self, message, client):
        dest = message.channel
        sender = message.author
        target = self.getTarget(message, client.user)

        chairmanRole = get(sender.guild.roles, name=roleName)

        if not self.hasPermissions(sender, chairmanRole):
            dest.send(self.NotPermittedMessage.format(user = sender.mention, smile = emoji.slight_smile))
            return

        try:
            await target.add_roles(chairmanRole)
        except Exception as e:
            await dest.send(self.ErrorMessage.format(user = sender.mention, e = str(e)))
        else:
            await dest.send(self.SuccessMessage.format(user = target.mention, smile = emoji.slight_smile))        

        return

    def hasPermissions(self, user, targetRole):
        if targetRole in user.roles:
            return True
        else:
            return False

    def getTarget(self, message, janetUser):
        mentions = message.mentions
        author = message.author
        for user in mentions:
            if user != author and user != janetUser:
                return user
