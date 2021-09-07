from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class convert_miles_km_app(App):
    def build(self):
        Window.size = (300, 200)
        self.title = "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root
    def handle_increment(self, value):
        print()

    def handle_convert(self, value):
        result = value *1.61
        self.root.ids.output_label.text = str(result)
    def get_validated_mile(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0
convert_miles_km_app().run()