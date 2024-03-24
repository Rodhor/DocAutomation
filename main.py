from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout

test = ["1 succes", "2 succes", "3 succes", "4 succes", "5 succes", "6 succes"]
test2 = ["1 Test", "2 Test", "3 Test", "4 Test", "5 Test", "6 Test"]


class Tab(MDFloatLayout, MDTabsBase):
    """Class implementing content for a tab."""


class LabelTest(MDTextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TestLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainApp(MDApp):
    def focus_next(self, next_field):
        if next_field:
            next_field.focus = True

    def on_start(self):
        if test != []:
            for i, task in enumerate(test):
                add_task = LabelTest(id=str(i), hint_text=task)
                self.root.ids.container.add_widget(add_task)

        if test2 != []:
            for i, task in enumerate(test2):
                add_task = LabelTest(id=str(i), hint_text=task)
                self.root.ids.containertwo.add_widget(add_task)

        self.iter_list_objects = iter(list(self.root.ids.tabs.get_tab_list()))

        # call method once to enable switching (first use does not switch the tab)
        self.switch_tab_by_object()

    def switch_tab_by_object(self):
        try:
            x = next(self.iter_list_objects)
            self.root.ids.tabs.switch_tab(x)
        except StopIteration:
            # reset the iterator an begin again.
            self.iter_list_objects = iter(list(self.root.ids.tabs.get_tab_list()))
            self.switch_tab_by_object()


if __name__ == "__main__":
    MainApp().run()
