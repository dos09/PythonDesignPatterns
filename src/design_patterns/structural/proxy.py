"""
Proxy is a structural design pattern that lets you provide a substitute or 
placeholder for another object. A proxy controls access to the original 
object, allowing you to perform something either before or after the 
request gets through to the original object.

Instead of using object X use proxy of X which will
take care for some additional stuff (security, logging... it can
do something before/after or during the main action where object X is used)
"""


class GuildVault:

    def view(self, player):
        print('Player "%s" is viewing the guild vault' % player.name)


class ProxyGuildVault:

    def __init__(self, *args, **kwargs):
        self.guild_vault = GuildVault(*args, **kwargs)
        self.black_list_players = ['Mogka', 'Banana']

    def view(self, player):
        if player.name in self.black_list_players:
            print('!!! Player "%s" is not allowed to view '
                  'the guild vault !!!' % player.name)
            return

        self.guild_vault.view(player)


class Player:

    def __init__(self, name):
        self.name = name


def run():
    mogka = Player('Mogka')
    ra = Player('Ra')
    guild_vault = GuildVault()
    proxy_vault = ProxyGuildVault()

    players = [mogka, ra]
    print(' * plain vault')
    for player in players:
        guild_vault.view(player)

    print(' * proxy vault')
    for player in players:
        proxy_vault.view(player)


if __name__ == '__main__':
    run()
