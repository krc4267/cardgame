# install_twisted_rector must be called before importing  and using the reactor
from kivy.support import install_twisted_reactor
install_twisted_reactor()


from twisted.internet import reactor
from twisted.internet import protocol


class EchoProtocol(protocol.Protocol):
    def dataReceived(self, data):
        response = self.factory.app.handle_message(data)
        if response:
            self.transport.write(response)


class EchoFactory(protocol.Factory):
    protocol = EchoProtocol

    def __init__(self, app):
        self.app = app


from kivy.app import App
from kivy.uix.label import Label


class TwistedServerApp(App):
    def build(self):
        self.label = Label(text="server started\n")
        reactor.listenTCP(8000, EchoFactory(self))
        return self.label
    
    def handle_message(self, msg):
        self.label.text = "received:  %s\n" % msg

        if msg == "ping":
            msg = "pong"
        if msg == "plop":
            msg = "kivy rocks"
        if len(msg.split()) <= 1:
            return msg
        if msg.split()[1] == "playing_card":
            cardPlayer = msg.split()[0]
            playedCard = msg.split()[2]
            playedCardLocation = msg.split()[3]
            msg = "played_card "+playedCard+" at "+playedCardLocation
        
        
        if msg.split()[0] == "joining":
            if gameRunning == 1:
                msg = "disconnect The game is already running"
            
        self.label.text += "responded: %s\n" % msg
        return msg


if __name__ == '__main__':
    TwistedServerApp().run()
