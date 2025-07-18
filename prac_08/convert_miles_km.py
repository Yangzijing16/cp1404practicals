from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

# Global constant for miles to kilometers conversion factor
MILES_TO_KM = 1.60934


class ConvertMilesKm(App):
    """A Kivy application to convert miles to kilometers with increment/decrement functionality."""

    km_output = StringProperty("0.0")

    def build(self):
        """Build the application interface by loading the Kv file.

        Returns:
            The root widget loaded from 'convert_miles_km.kv'.
        """
        self.title = "英里转公里"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        """Handle the convert button press event.

        Converts the input miles to kilometers and updates the output label.
        Sets output to '0.0' if the input is invalid.
        """
        try:
            miles = float(self.root.ids.miles_input.text)
            self.km_output = str(miles * MILES_TO_KM)
        except ValueError:
            self.km_output = "0.0"

    def handle_increment(self, value):
        """Handle the increment/decrement button press event.

        Adjusts the miles value by the given increment and triggers conversion.

        Args:
            value (int): The increment value (1 for up, -1 for down).
        """
        try:
            miles = float(self.root.ids.miles_input.text)
        except ValueError:
            miles = 0.0
        miles += value
        self.root.ids.miles_input.text = str(miles)
        self.handle_convert()

    def handle_text(self, text):
        """Handle text input changes in the miles input field.

        Triggers conversion when the text changes.

        Args:
            text (str): The current text in the input field.
        """
        self.handle_convert()


ConvertMilesKm().run()