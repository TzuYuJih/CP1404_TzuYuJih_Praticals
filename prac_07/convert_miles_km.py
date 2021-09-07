from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class convert_miles_km_app(App):
    def build(self):
        Window.size = (300, 200)
        self.title = "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root
convert_miles_km_app().run()