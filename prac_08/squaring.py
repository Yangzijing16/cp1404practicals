"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

from kivy.app import App
from kivy.lang import Builder


class SquareNumberApp(App):
    """A Kivy application to calculate the square of a user-entered number."""

    def build(self):
        """Build the application interface by loading the Kv file.

        Returns:
            The root widget loaded from 'squaring.kv'.
        """
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle the calculate button press event.

        Calculates the square of the input value and updates the output label.
        If the input is invalid, sets the label to '0'.

        Args:
            value (str): The text input from the user.
        """
        try:
            result = int(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "0"


SquareNumberApp().run()
