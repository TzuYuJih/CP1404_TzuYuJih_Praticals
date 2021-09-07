from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
convert_m_to_km = 1.60934
class convert_miles_km_app(App):
    def build(self):
        Window.size = (300, 200)
        self.title = "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root
    def handle_increment(self, change):
        value = self.get_validated_mile() + change
        self.root.ids.input_number.text = str(value)
        self.handle_convert()

    def handle_convert(self):
        value = self.get_validated_mile()
        result = value * convert_m_to_km
        self.root.ids.output_label.text = str(result)

    def get_validated_mile(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0
convert_miles_km_app().run()