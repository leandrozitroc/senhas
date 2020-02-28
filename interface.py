import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.image import Image

Window.size = 600,300
Window.title = 'Sistema Athena'


class Athena(App):


        def build(self):

            layout2 = FloatLayout()

            layout = GridLayout(cols=2, row_force_default=True , row_default_height=40, pos=(0 ,-140 ))
            botao1 = layout.add_widget(Button(text='Gerar Senha'))
            botao2 = layout.add_widget(Button(text='Criptografar Senha'))
            botao3 = layout.add_widget(Button(text='Descriptografar Senha'))
            botao4 = layout.add_widget(Button(text='Criptografar Arquivo'))
            botao5 = layout.add_widget(Button(text='Descriptografar Arquvivo'))
            botao6 = layout.add_widget(Button(text='Acessar Repositorio de Senhas'))
            botao7 = layout.add_widget(Button(text='Sair'))
            botao8 = layout.add_widget(Button(text='Acesse nosso portifólio'))
            #tena = layout2.add_widget(Image(source= 'tena1.png'))

            return layout, layout2


if __name__ == '__main__':
    Athena().run()