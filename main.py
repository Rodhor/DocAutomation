from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout


class IndividualTab(MDTabsBase, MDFloatLayout):
    pass


class TagListItem(MDBoxLayout):
    tag = ""
    meaning = ""
    description = ""


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

    def change_tags(self):
        self.root.current = "screen2"

    def change_categories(self):
        self.root.current = "screen3"

    def change_templates_path(self):
        pass

    def add_new_tag(self, tag_text, tag_meaning, tag_description):
        new_tag = TagListItem(
            text=tag_text, secondary_text=tag_meaning, tertiary_text=tag_description
        )
        screen = self.root.screens[1]
        screen.ids.taglist.add_widget(new_tag)
        screen.ids.tag_field.text = ""
        screen.ids.meaning_field.text = ""
        screen.ids.description_field.text = ""
        screen.ids.tag_field.focus = True


if __name__ == "__main__":
    MainApp().run()
