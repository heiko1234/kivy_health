# https://www.youtube.com/watch?v=S4X-YdnVtVA

# from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Properties
from kivy.properties import ObjectProperty

# Progressbar
# https://www.geeksforgeeks.org/python-progress-bar-widget-in-kivy/
# https://www.youtube.com/watch?v=K6j2NPsKDGE

# Clock
from kivy.clock import Clock

# partial: funktions reverenz + parameter übergabe
from functools import partial


# Define our differeent screens
class WelcomeWindow(Screen):

    entrance_name_label = ObjectProperty(None)
    entrance_user_name = ObjectProperty(None)

    def on_enter(self, *args):
        # on_enter works automatically, while keyword
        Clock.schedule_once(self.switch_to_healing_view, 5)

    def entrance_button_behavior(self, *args):
        Clock.schedule_once(self.switch_to_healing_view, 1)

    def switch_to_healing_view(self, *args):
        self.manager.current = "worldwindow"
        self.manager.transition.direction = "left"


class WorldWindow(Screen):

    healing_message = ObjectProperty(None)
    progress_bar = ObjectProperty(None)
    breath_message = ObjectProperty(None)

    def next(self, dt, *args):

        # Progress Messages
        if self.progress_bar.value <= 2:
            self.healing_message.text = ""
        elif self.progress_bar.value > 2 and self.progress_bar.value < 10:
            self.healing_message.text = "Problems identified"
        elif self.progress_bar.value > 10 and self.progress_bar.value < 42:
            self.healing_message.text = "Repairing in progress"
        elif self.progress_bar.value > 42 and self.progress_bar.value < 64:
            self.healing_message.text = "You have taff problems"
        elif self.progress_bar.value > 64 and self.progress_bar.value < 72:
            self.healing_message.text = "It takes some more time"
        elif self.progress_bar.value > 72 and self.progress_bar.value < 100:
            self.healing_message.text = "Reparing in progress"
        elif self.progress_bar.value >= 100:
            self.healing_message.text = "I hope your world is \n   a bit better now"

        # Breath messages
        if self.progress_bar.value > 2 and self.progress_bar.value < 17:
            self.breath_message.text = "Breath IN"
        elif self.progress_bar.value > 17 and self.progress_bar.value < 42:
            self.breath_message.text = "Breath OUT"
        elif self.progress_bar.value > 42 and self.progress_bar.value < 57:
            self.breath_message.text = "Breath IN"
        elif self.progress_bar.value > 57 and self.progress_bar.value < 77:
            self.breath_message.text = "Breath Out"
        elif self.progress_bar.value > 77 and self.progress_bar.value < 100:
            self.breath_message.text = "Breath and Relax"

        elif self.progress_bar.value >= 100:
            self.breath_message.text = ""

            return False
        self.progress_bar.value = self.progress_bar.value + 0.1

    def heal_your_world(self, *args):

        if self.progress_bar.value >= 100:
            self.progress_bar.value = 0
            self.healing_message.text = ""

        # self.healing_message.text = "Healing in progress"
        Clock.schedule_interval(partial(self.next), 1 / 15)


class WindowManager(ScreenManager):
    pass


# Designate our .v design file
kv = Builder.load_file("fix_my_world.kv")


class HealApp(App):
    # without MD components
    def build(self):
        return kv


if __name__ == "__main__":
    HealApp().run()
