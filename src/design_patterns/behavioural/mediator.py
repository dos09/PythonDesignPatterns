"""
Mediator is a behavioral design pattern that lets you reduce chaotic 
dependencies between objects. The pattern restricts direct communications 
between the objects and forces them to collaborate only via a mediator object.

Objects communicate to each other using mediator, not directly
"""


class ChatRoom:

    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def notify(self, sender, msg):
        for member in self.members:
            if member.name != sender.name:
                member.display_msg('[%s]: %s' % (sender.name, msg))


class Member:

    def __init__(self, name, chat_room):
        self.name = name
        self.chat_room = chat_room  # mediator
        self.chat_room.add_member(self)

    def send_msg(self, msg):
        self.chat_room.notify(self, msg)

    def display_msg(self, msg):
        print('chat window of %s: %s' % (self.name, msg))


if __name__ == '__main__':
    chat_room = ChatRoom()
    asen = Member('Asen', chat_room)
    kiro = Member('Kiro', chat_room)
    ivan = Member('Ivan', chat_room)
    asen.send_msg('opa')
    asen.send_msg('az sym ot Sliven')
    ivan.send_msg('dobre')

