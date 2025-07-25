from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """A Kivy application to dynamically create labels from a list of names."""

    def __init__(self, **kwargs):
        """Initialize the application with a list of names.

        Args:
            **kwargs: Additional keyword arguments for the App class.
        """
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana"]

    def build(self):
        """Build the application interface by loading the Kv file and adding dynamic labels.

        Returns:
            The root widget loaded from 'dynamic_labels.kv'.
        """
        self.title = "dynamic labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)
        return self.root


DynamicLabelsApp().run()