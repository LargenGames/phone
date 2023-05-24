from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class CarApp(MDApp):
    def build(self):
        return MDLabel(text="Приветик", halign="center")


CarApp().run()