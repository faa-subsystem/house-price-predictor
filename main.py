from kivy.animation import Animation
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.textfield import MDTextFieldRect
import rf_model


class MainScreen(MDScreen):
    pass


class InputDataScreen(MDScreen):
    pass


class OnFrontText(MDTextFieldRect):
    pass


class InteractiveBL(MDBoxLayout, HoverBehavior):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print("BoxLayout clicked!")
            return True
        return super().on_touch_down(touch)

    def on_enter(self, *args):
        self.on_touch_down(self)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__()
        self.main_screen = None
        self.inout_data_screen = None
        self.screen = None
        self.estimated_price = ""
        self.correlation_description = '''The data shows the number of bathrooms and the number of rooms influences 
        directly in the price. Also, the number of bathrooms is strongly correlated with the number of rooms in the 
        property, which is very understandable. '''
        self.square_footage_price_description = """Opposite to the intuition, the land size is not a noticeable influence on the price if we consider other factors. The type of property is one direct factor that affects the price. Houses tend to be more expencive than other type of properties. """
        self.price_distribution = """Our data shows a majority of houses priced between 500,000 and 1,000,000"""

    def build(self):
        self.icon = 'src\logo.ico'
        self.title = 'DH Price Estimator'
        self.main_screen = MainScreen()
        self.inout_data_screen = InputDataScreen()
        self.theme_cls.theme_style = "Dark"

        self.screen = MDScreenManager()

        self.screen.add_widget(self.main_screen)
        self.screen.add_widget(self.inout_data_screen)
        return self.screen

    def change_screen(self, index):
        if index == "main":
            self.screen.current = self.main_screen
        elif index == "input":
            self.screen.current = self.inout_data_screen

    def re_size(self, widget, neighbors):
        for i in neighbors:
            i.size_hint = (.1, 1)

        anim = Animation(size_hint=(1, 1), duration=.5)
        anim += Animation(pos_hint={'center_x': 0.5}, duration=1.)
        anim.start(widget)

        for i in neighbors:
            i.size_hint = (.3, 1)

    def do_prediction(self):
        screen = self.root.get_screen('data_input_screen')
        input = [screen.ids.rooms.text,
                 screen.ids.bath.text,
                 screen.ids.land.text,
                 screen.ids.lat.text,
                 screen.ids.lon.text]

        for i in range(len(input)):
            input[i] = 0.0 if input[i] == '' else float(input[i])

        if all(i == 0 for i in input):
            screen.ids.estimated_price_field.text = "0.0"
        else:
            prediction = rf_model.rf_predictor(input[0], input[1], input[2], input[3], input[4])
            screen.ids.estimated_price_field.text = str(prediction)
        # screen.ids.estimated_price_field.text = "str(prediction)"


MainApp().run()
