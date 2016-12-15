from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from Registrierung import Register


class RegisterScreen(Screen):
    """Für die Registrierung gedacht. Variablen in dem jeweiligen Screen deklarieren mit ObjectProperty().
    Dann können Variablen in der .kv Datei auch angespochen werden. Wenn das eine TextInputBox ist kann so de"""
    username = ObjectProperty()
    passwort = ObjectProperty()

    """
    Beispiel Methode für das Holen der eingegebenen Wörter in der
    def get_username_passwd(self):
        print(self.username.text)
        print(self.passwort.text)
    """
class MainScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class Manager(ScreenManager):

    register_screen = ObjectProperty(None)
    #main_screen = ObjectProperty(None)
    login_screen = ObjectProperty(None)


class LIMSApp(App):

    def build(self):
        return Manager()



if __name__ == "__main__":
    LIMSApp().run()
