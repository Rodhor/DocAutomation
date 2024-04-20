from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import ThreeLineAvatarIconListItem

test = ["1 succes", "2 succes", "3 succes", "4 succes", "5 succes", "6 succes"]
test2 = ["1 Test", "2 Test", "3 Test", "4 Test", "5 Test", "6 Test"]


# Class implementing content for a tab
class Tab(MDFloatLayout, MDTabsBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# Class implementing content for a textnputfield
class TextInputField(MDTextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class CustomDialog(MDDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.content_cls = Tag_settings_layout()


class ListItem(ThreeLineAvatarIconListItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainApp(MDApp):
    dialog = None

    def on_start(self):
        if test != []:
            for i, task in enumerate(test):
                add_task = TextInputField(id=str(i), hint_text=task)
                self.root.ids.container.add_widget(add_task)

        if test2 != []:
            for i, task in enumerate(test2):
                add_task = TextInputField(id=str(i), hint_text=task)
                self.root.ids.containertwo.add_widget(add_task)

        self.iter_list_objects = iter(list(self.root.ids.tabs.get_tab_list()))

        # call method once to enable switching (first use does not switch the tab)
        self.switch_tab_by_object()

    def focus_next(self, next_field):
        if next_field:
            next_field.focus = True

    def switch_tab_by_object(self):
        try:
            x = next(self.iter_list_objects)
            self.root.ids.tabs.switch_tab(x)
        except StopIteration:
            # reset the iterator an begin again.
            self.iter_list_objects = iter(list(self.root.ids.tabs.get_tab_list()))
            self.switch_tab_by_object()

    def show_category_settings(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Category settings",
                type="custom",
                content_cls=Tag_settings_layout(),
            )
        self.dialog.open()

    def show_tag_setings(self):
        if not self.dialog:
            self.dialog = CustomDialog(
                title="Tag settings", type="custom", content_cls=Tag_settings_layout()
            )
        self.dialog.open()

    def close_dialog(self):
        pass

    def add_tag(self, tag, tag_meaning, tag_description):
        tagitem = ListItem(
            text=tag, secondary_text=tag_meaning, tertiary_text=tag_description
        )
        # Access the taglist from the dialog's content class
        # print(self.dialog.ids.items())
        self.dialog.ids.taglist.add_widget(tagitem)

    def add_category(self, category_tag, category, category_description):
        pass


if __name__ == "__main__":
    MainApp().run()
