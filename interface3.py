import kivy
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.image import Image
import kivy.uix.widget
from kivy.lang import Builder


Window.size = 600, 300
Window.title = 'Sistema Athena'

class Botao1(Screen):
    def bt1(self, instance):
        m = FloatLayout
        m.add_widget(Button(on_press=settings))

class Botao2(Screen):
    pass
class MultiScreen(App):
    pass

sm = ScreenManager()
#sm.add_widget()
sm.add_widget(Botao2(name='settings'))


class Athena(App):



    def build(self):



        layout = GridLayout(cols=2, row_force_default=True, row_default_height=40, pos=(0, -140))
        botao1 = layout.add_widget(Button(text='Gerar Senha', on_press=Botao1))
        botao2 = layout.add_widget(Button(text='Criptografar Senha'))
        botao3 = layout.add_widget(Button(text='Descriptografar Senha'))
        botao4 = layout.add_widget(Button(text='Criptografar Arquivo'))
        botao5 = layout.add_widget(Button(text='Descriptografar Arquvivo'))
        botao6 = layout.add_widget(Button(text='Acessar Repositorio de Senhas'))
        botao7 = layout.add_widget(Button(text='Sair'))
        botao8 = layout.add_widget(Button(text='Acesse nosso portifólio'))

        return layout


if __name__ == '__main__':
    Athena().run()