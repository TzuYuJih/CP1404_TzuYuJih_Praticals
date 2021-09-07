from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label

class dynamic_labels_app(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.test_list = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}
    def build(self):
        self.title: 'Dynamic Labels'
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.test_list:
            label = Label(text="{}'s number is {}".format(name, self.test_list[name]))
        return label


dynamic_labels_app().run()