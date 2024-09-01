from fpdf import FPDF
import os

class OutputManager:
    def __init__(self, output_dir, output_format='txt'):
        self.output_dir = output_dir
        self.output_format = output_format

    def save_output(self, text, filename="output"):
        output_path = os.path.join(self.output_dir, f"{filename}.{self.output_format}")
        if self.output_format == 'txt':
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
        elif self.output_format == 'pdf':
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, text.encode('latin1', 'ignore').decode('latin1'))
            pdf.output(output_path)
