from kivy.app import App
from kivy.lang import Builder
from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemo(App):
    """A simple Kivy application demonstrating a greeting interface with buttons and text input."""

    def build(self):
        """Build the application interface by loading the Kv file.

        Returns:
            The root widget loaded from 'box_layout.kv'.
        """
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle the greet button press event.

        Updates the output label with a greeting using the text from the input field.
        """
        print("greet")  # For testing
        self.root.ids.output_label.text = f"你好 {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Handle the clear button press event.

        Resets the text input field and output label to their initial states.
        """
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = "请输入您的姓名"

BoxLayoutDemo().run()