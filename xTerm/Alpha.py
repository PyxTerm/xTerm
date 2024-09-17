from ._utils import *


class Maths:
    def __init__(self, font_type="Sans_Serif"):
        """Conver a string of words to their respective Unicode fonts.
        - font_type: str - The name of the font type to use.

        Examples:

            >>> from xTerm.Alpha import Maths
            >>> maths = Maths(font_type="Sans_Serif")
            >>> maths = Maths(font_type="Sans_Serif_bold")
            >>> maths = Maths(font_type="Sans_Serif_italic")
            >>> maths = Maths(font_type="Sans_Serif_bold_italic")
            >>> maths = Maths(font_type="Mathematical_bold")
            >>> maths = Maths(font_type="Mathematical_italic")
            >>> maths = Maths(font_type="Mathematical_Fraktur")
            >>> maths = Maths(font_type="Mathematical_bold_Fraktur")
            >>> maths = Maths(font_type="Mathematical_double_struck")
            >>> maths = Maths(font_type="Mathematical_monospace")
            >>> converted_text = maths.Convert("Hello World")
            >>> print(converted_text)
            Hello World

        """
        # Load the font type
        if font_type == "Sans_Serif":
            self.Words = Sans_Serif
        elif font_type == "Sans_Serif_bold":
            self.Words = Sans_Serif_bold
        elif font_type == "Sans_Serif_italic":
            self.Words = Sans_Serif_italic
        elif font_type == "Sans_Serif_bold_italic":
            self.Words = Sans_Serif_bold_italic
        elif font_type == "Mathematical_bold":
            self.Words = Mathematical_bold
        elif font_type == "Mathematical_italic":
            self.Words = Mathematical_italic
        elif font_type == "Mathematical_Fraktur":
            self.Words = Mathematical_Fraktur
        elif font_type == "Mathematical_bold_Fraktur":
            self.Words = Mathematical_bold_Fraktur
        elif font_type == "Mathematical_double_struck":
            self.Words = Mathematical_double_struck
        elif font_type == "Mathematical_monospace":
            self.Words = Mathematical_monospace
        else:
            raise ValueError(f"Font type '{font_type}' is not recognized.")

    def Convert(self, words_string):
        characters = [char for char in words_string]
        # Convert the characters to their respective fonts
        return "".join([self.Words.get(char, char) for char in characters])


class FontManager:
    """A class to manage different Unicode fonts and provide conversions."""

    def __init__(self):
        # Map of font names to their corresponding Unicode dictionaries
        self.fonts = {
            "Sans_Serif": Sans_Serif,
            "Sans_Serif_bold": Sans_Serif_bold,
            "Sans_Serif_italic": Sans_Serif_italic,
            "Sans_Serif_bold_italic": Sans_Serif_bold_italic,
            "Mathematical_bold": Mathematical_bold,
            "Mathematical_italic": Mathematical_italic,
            "Mathematical_Fraktur": Mathematical_Fraktur,
            "Mathematical_bold_Fraktur": Mathematical_bold_Fraktur,
            "Mathematical_double_struck": Mathematical_double_struck,
            "Mathematical_monospace": Mathematical_monospace,
        }
        # Cache for storing converted words to avoid redundant processing
        self._cache = {}

    def list_fonts(self):
        """Return the list of available font types."""
        return list(self.fonts.keys())

    def set_font(self, font_type):
        """Set the current font type for conversion."""
        if font_type not in self.fonts:
            raise ValueError(f"Font type '{font_type}' is not supported. Available fonts: {self.list_fonts()}")
        self.current_font = self.fonts[font_type]
        # Reset cache when changing fonts
        self._cache = {}

    def convert(self, words_string):
        """Convert the input string to the selected font."""
        if not hasattr(self, 'current_font'):
            raise ValueError("No font has been selected. Use 'set_font' to select a font.")

        # Check cache to avoid redundant processing
        if words_string in self._cache:
            return self._cache[words_string]

        # Convert each character using the current font's dictionary
        characters = [self.current_font.get(char, char) for char in words_string]
        result = "".join(characters)

        # Cache the result for future calls
        self._cache[words_string] = result
        return result

    def show_example(self):
        """Show an example of text converted into all available fonts."""
        example_text = "Professional Programming With Mmdrza.Com"
        examples = {}
        for font in self.list_fonts():
            self.set_font(font)
            examples[font] = self.convert(example_text)
        return examples

    def clear_cache(self):
        """Clear the cache."""
        self._cache.clear()

    def __del__(self):
        self.clear_cache()

    def __repr__(self):
        return f"<FontManager: {self.current_font}>"

    def __str__(self):
        return self.current_font

    def __getitem__(self, font_type):
        return self.fonts[font_type]
