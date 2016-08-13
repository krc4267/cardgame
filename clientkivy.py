#install_twisted_rector must be called before importing the reactor
from kivy.support import install_twisted_reactor
install_twisted_reactor()


#A simple Client that send messages to the echo server
from twisted.internet import reactor, protocol


class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.factory.app.on_connection(self.transport)

    def dataReceived(self, data):
        self.factory.app.print_message(data)
        if type(data) is dict:
            self.factory.app.update_checker(data)


class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def __init__(self, app):
        self.app = app

    def clientConnectionLost(self, conn, reason):
        self.app.print_message("connection lost")

    def clientConnectionFailed(self, conn, reason):
        self.app.print_message("connection failed")


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


# A simple kivy App, with a textbox to enter messages, and
# a large label to display all the messages received from
# the server
class TwistedClientApp(App):
    connection = None

    def build(self):
        root = self.setup_gui()
        self.connect_to_server()
        return root

    def setup_gui(self):
        self.textbox = TextInput(size_hint_y=.1, multiline=False)
        self.textbox.bind(on_text_validate=self.send_message)
        self.label = Label(text='connecting...\n')
        self.layout = BoxLayout(padding=5, orientation='vertical')
        self.away_layout = BoxLayout(padding=5, orientation='horizontal')
        self.home_layout = BoxLayout(padding=5, orientation='horizontal')
        self.hand_layout = BoxLayout(padding=5, orientation='horizontal')
        self.hand_layout.add_widget(Button(text='haaai'))
        self.play_button = Button(text='Play a Card')
        self.play_button.bind(on_press=self.send_card)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.textbox)
        self.hand_layout.add_widget(self.play_button)
        self.layout.add_widget(self.away_layout)
        self.layout.add_widget(self.home_layout)
        self.layout.add_widget(self.hand_layout)
        self.away_layout.add_widget(Button(text='enemy cards'))
        self.home_layout.add_widget(Button(text='friendly cards'))
        self.hand_layout.add_widget(Button(text='your hand'))
        self.hand_1 = Button(text='Plaaaay')
        self.hand_1.bind(on_press=self.enemy_playcard)
        self.hand_layout.add_widget(self.hand_1)
        
#        self.
        
        return self.layout

    def connect_to_server(self):
        reactor.connectTCP('localhost', 8000, EchoFactory(self))
    def on_connection(self, connection):
        self.print_message("connected succesfully!")
        self.connection = connection
    def send_card(self, *args):
        msg = "client1 playing_card 120 3"
        if msg and self.connection:
            self.connection.write(str(msg))
    def send_message(self, *args):
        msg = self.textbox.text
        if msg and self.connection:
            self.connection.write(str(self.textbox.text))
            self.textbox.text = ""
    def print_message(self, msg):
        self.label.text += msg + "\n"
    
    def enemy_playcard(self, *args):
        self.away_layout.add_widget(Button(text='Heheheheeeehe'))
    def update_checker(self, data, *args):
        if type data is dict:
            hand = data['hand']
            
            

if __name__ == '__main__':
    TwistedClientApp().run()
