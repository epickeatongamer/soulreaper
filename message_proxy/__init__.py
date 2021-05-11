from .message_proxy import Message_proxy


def setup(bot):
    bot.add_cog(Message_proxy())
