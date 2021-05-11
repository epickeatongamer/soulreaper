from .message_proxy import message_proxy


def setup(bot):
    bot.add_cog(message_proxy())
