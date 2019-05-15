from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.lang import Builder

class LoginScreen(Screen):

    def varify_password(self):        
        data = {'Kaushal': 'kp123',
                'Pravinbhai': 'pz123',
                'Pinkal': 'pk123'}        

        self.username = self.ids['username'].text
        self.password = self.ids['password'].text

        print(data[self.username], self.password)

        if self.password == data[self.username]:
            self.manager.current = 'Welcome'
        else:
            self.manager.current = 'Login'
    
    def resetForm(self):
        self.ids['username'].text = ""
        self.ids['password'].text = ""

class WelcomeScreen(Screen):
    def logout(self):
        self.manager.transition = FadeTransition()
        self.manager.current = 'Login'
        self.manager.get_screen('Login').resetForm()


class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file('MyApp.kv')

class MyApp(App):
    def build(self):
        return presentation

if __name__ == '__main__':
    MyApp().run()