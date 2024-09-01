import language_tool_python

class TextCorrector:
    def __init__(self):
        self.tool = language_tool_python.LanguageTool('es')

    def correct_text(self, text):
        matches = self.tool.check(text)
        corrected_text = language_tool_python.utils.correct(text, matches)
        return corrected_text
