from kivy.app import app
from kivy.unix.button import button
from kivy.unix.label import label
from kivy.unix.boxlayout import boxlayout

class MainPage(BoxLayout):
    def __init__(self, **kwargs):
        super(MainPage,self).__init__(**kwargs)
        self.orientation = 'vertical'

        # add tag and button
        self.label = Label(text='Welcome to My App')
        self.add_widget(self.label)

        self.button = Button(text='Click Me')
        self.button.bind(on_press = self.on_button_click)
        self.add_widget(self.button)


    def on_button_click(self, instance):
        self.label.text = 'Button Clicked!'

class MyApp(App):
    def build(self):
        return MainPage()


if __name__ =='__main__':
    MyApp().run()