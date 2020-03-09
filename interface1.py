from kivy.app import App
from password_generator import PasswordGenerator
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import kivy
import webbrowser
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import pyperclip
from kivy.core.clipboard import Clipboard
from luli import encript_senha
from luli import decript_senha

Window.size = 600, 300
Window.title = 'Sistema Athena'
# Create screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        #cols:2
        #row_force_default: True
        #row_default_height: 50
        Label:
            text: 'BEM VINDO AO SISTEMA ATHENA. ESCOLHA UMA OPÇÃO:'
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        Button:
            text: 'Gerar Senha'
            on_press: root.manager.current = 'senha'
        Button:
            text: 'Criptografar/Decriptografar Senha'
            on_press: root.manager.current = 'cript'
      
        Button:
            text: 'Criptografar/Decriptografar Arquivo'

        Button:
            text: 'Acessar Repositorio de Senhas'
            on_press: root.manager.current= 'repsenha'
        Button:
            text: 'Sair'
            on_press: exit()

        Button:
            text: 'Acesse nosso portifolio'
            on_press:
                import webbrowser
                webbrowser.open('http://flowredes.com')

        
<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
            
<DescripEncript>:
    BoxLayout:
        Button:
            text: 'Criptografar Senha'
            on_press: root.manager.current = 'pgencriptsenha'
        Button:
            text: 'Descriptografar Senha'
            on_press: root.manager.current = 'pgdecriptsenha'
        
        Button:
            text: 'Volte ao Menu'
            on_press: root.manager.current = 'menu'
            
<Senha>:
    BoxLayout:
        Button:
            text: 'Gerar Senha'
            on_press: root.manager.current = 'pagsenha'
        Button:
            text: 'Volte ao Menu'
            on_press: root.manager.current = 'menu'    
            
<Repositorio>:
    BoxLayout:
        Label:
            text: 'Escolha uma das senhas abaixo.'
        Button: 
            text: 'texte'

<PaginaSenha>
    BoxLayout:
        orientation: 'vertical'
        TextInput: 
            text: 'A senha gerada é:   '+    root.gerarsenha()
            color: (3,1,2,1)
            multiline: False
            back_ground_color: 1,0,2,1
        Button: 
            text: 'Volte ao Menu'
            on_press: root.manager.current = 'menu' 
 
<PaginaEncriptSenha>:
    BoxLayout:
        orientation: 'vertical'
        Label: 
            text: 'Digite a Senha a ser Encriptada: '
            id: titulo_encript
        TextInput:
            id: senha_1
        Button: 
            text: 'Encriptar'
            on_press: root.save()
            on_release: 
                root.mostra_senha()
        Button:
            text: 'Copiar Senha:'
            on_press:
                app.clipcopy(senha_1.text)        
        
        Button: 
            text: 'Volte ao Anterior'
            on_press: root.manager.current = 'cript' 
            on_release: root.apaga_text()
        
        Button: 
            text: 'Volte ao Menu'
            on_press: root.manager.current = 'menu' 
            on_release: root.apaga_text()

<PaginaDecriptSenha>:
    BoxLayout:
        orientation: 'vertical'
        Label: 
            text: 'Digite a Senha a ser Decriptada: '
            id: titulo_decript
        TextInput:
            id: senha_2
        Button: 
            text: 'Decriptar'
            on_press: root.save()
            on_release: 
                root.mostra_senha()
        
        Button:
            text: 'Cole a Senha a ser Decriptada: '
            on_press: 
                root.clippaste()
                    
        Button:
            text: 'Copiar Senha:'
            on_press:
                app.clipcopy(senha_2.text)
                
                
        Button: 
            text: 'Volte ao Anterior'
            on_press: root.manager.current = 'cript' 
            on_release: root.apaga_text()
        
        Button: 
            text: 'Volte ao Menu'
            on_press: root.manager.current = 'menu' 
            on_release: root.apaga_text()
            
        

               
                
""")

# Declare screens

class Senha(Screen):
    pass

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class DescripEncript(Screen):
    pass

class Criptarq(Screen):
    pass

class Repositorio(Screen):
    pass
class Paginasenha(Screen):
    def gerarsenha(self):

        pwo = PasswordGenerator()
        pwo.minlen = 8
        pwo.maxlen = 12

        pw = pwo.generate()
        return pw

class PaginaEncriptSenha(Screen):
    def save(self):
        global my_pwd1
        my_pwd = self.ids.senha_1.text
        my_pwd1 = encript_senha(my_pwd, "ccLmrWCJu7vpwaroDuSEjv6amtpLyiY9MI-PS-oWy_4=")

    def mostra_senha(self):
        self.ids.senha_1.text = my_pwd1
        self.ids.titulo_encript.text = 'Senha Encriptada'
    def apaga_text(self):
        self.ids.senha_1.text = ''
        self.ids.titulo_encript.text = 'Digite a Senha a ser Encriptada:'

class PaginaDecriptSenha(Screen):
    def save(self):
        global my_pwd2
        my_pwd = self.ids.senha_2.text
        my_pwd2 = decript_senha(my_pwd, "ccLmrWCJu7vpwaroDuSEjv6amtpLyiY9MI-PS-oWy_4=")

    def mostra_senha(self):
        self.ids.senha_2.text = my_pwd2
        self.ids.titulo_decript.text = 'Senha Decriptada'

    def apaga_text(self):
        self.ids.senha_2.text = ''
        self.ids.titulo_decript.text = 'Digite a Senha a ser Decriptada:'

    def clippaste(self):
        self.ids.senha_2.text = pyperclip.paste()

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(DescripEncript(name = 'cript'))
sm.add_widget(Senha(name='senha'))
sm.add_widget((Criptarq(name='criptarq')))
sm.add_widget((Repositorio(name='repsenha')))
sm.add_widget((Paginasenha(name='pagsenha')))
sm.add_widget((PaginaEncriptSenha(name='pgencriptsenha')))
sm.add_widget(PaginaDecriptSenha(name='pgdecriptsenha'))

class TestApp(App):

    def build(self):
        return sm

    def clipcopy(self, data):
        pyperclip.copy(str(data))
    def clippaste(self):
        pyperclip.paste()


if __name__ == '__main__':
    TestApp().run()