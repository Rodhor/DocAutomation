from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import TwoLineAvatarIconListItem


class IndividualTab(MDTabsBase, MDFloatLayout):
    pass


class TagListItem(TwoLineAvatarIconListItem):
    pass


class MainScreen(MDScreen):
    pass


class TagSettingsScreen(MDScreen):
    pass


class CategorySettingsScreen(MDScreen):
    pass


class MainApp(MDApp):
    def build(self):
        # Setting the theme to be a nice shade of orange with white and black text
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.primary_hue = "900"

        # Defining and loading the screens, adding them to the screenmanager
        sm = MDScreenManager()
        sm.add_widget(MainScreen(name="MainScreen"))
        sm.add_widget(TagSettingsScreen(name="TagSettingsScreen"))
        sm.add_widget(CategorySettingsScreen(name="CategorySettingsScreen"))
        return sm

    def on_start(self):

        for screen in self.root.screens:
            if screen.name == "MainScreen":
                for i in range(5):
                    screen.ids.tabs.add_widget(IndividualTab(title=f"test{i}"))

    def change_tags(self):
        self.root.current = "TagSettingsScreen"

    def change_categories(self):
        self.root.current = "CategorySettingsScreen"

    def change_templates_path(self):
        pass

    def add_new_tag(self, tag_text, tag_type, tag_description):
        if not tag_text == "" and not tag_type == "":
            new_tag = TagListItem(
                id=tag_text, text=tag_type, secondary_text=tag_description
            )
            screen = self.root.screens[1]
            screen.ids.taglist.add_widget(new_tag)
            screen.ids.tag_field.text = ""
            screen.ids.type_field.text = ""
            screen.ids.description_field.text = ""
            screen.ids.tag_field.focus = True


if __name__ == "__main__":
    MainApp().run()
