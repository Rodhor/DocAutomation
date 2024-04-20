from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout


class IndividualTab(MDTabsBase, MDFloatLayout):
    pass


class Screen1(MDScreen):
    pass


class Screen2(MDScreen):
    pass


class Screen3(MDScreen):
    pass


class MainApp(MDApp):
    def build(self):
        sm = MDScreenManager()
        sm.add_widget(Screen1(name="screen1"))
        sm.add_widget(Screen2(name="screen2"))
        sm.add_widget(Screen3(name="screen3"))
        return sm

    def on_start(self):
        for screen in self.root.screens:
            if screen.name == "screen1":
                for i in range(5):
                    screen.ids.tabs.add_widget(IndividualTab(title=f"test{i}"))


if __name__ == "__main__":
    MainApp().run()
