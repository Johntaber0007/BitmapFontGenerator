import os
import base64
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QVBoxLayout, QPushButton, QSpinBox, QWidget, QHBoxLayout, QSizePolicy
from PyQt6.QtCore import Qt, QLocale
from PyQt6.QtGui import QIcon, QPixmap
from PIL import Image, ImageDraw, ImageFont

base64_icon = """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"""

def render_text_to_bitmap(text, font_path, output_image_path, font_size=50):
    font = ImageFont.truetype(font_path, font_size)

    temp_image = Image.new('RGBA', (1, 1), (0, 0, 0, 0))
    draw = ImageDraw.Draw(temp_image)

    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    padding_x = 30
    padding_y = 40

    image_width = text_width + 2 * padding_x
    image_height = text_height + 2 * padding_y
    image = Image.new('RGBA', (image_width, image_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    text_position = (padding_x - text_bbox[0], padding_y - text_bbox[1])
    draw.text(text_position, text, font=font, fill='white')

    image.save(output_image_path, 'PNG')

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

class FontRendererApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("BitmapFontGenerator By Johntaber")
        self.setGeometry(100, 100, 500, 400)
        self.setFixedSize(400, 280)

        pixmap = QPixmap()
        pixmap.loadFromData(base64.b64decode(base64_icon))
        self.setWindowIcon(QIcon(pixmap))

        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        
        font_layout = QHBoxLayout()
        layout.addLayout(font_layout)

        self.select_font_btn = QPushButton('Select Font', self)
        self.select_font_btn.clicked.connect(self.select_font)
        font_layout.addWidget(self.select_font_btn)

        self.font_size_label = QLabel("Font Size:", self)
        font_layout.addWidget(self.font_size_label)

        self.font_size_spinbox = QSpinBox(self)
        self.font_size_spinbox.setRange(10, 200)
        self.font_size_spinbox.setValue(50)
        font_layout.addWidget(self.font_size_spinbox)

        self.selected_font_label = QLabel("Selected Font: None", self)
        layout.addWidget(self.selected_font_label)

        layout.addStretch()

        self.render_btn = QPushButton('Generate', self)
        self.render_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.render_btn.setMinimumHeight(150)
        self.render_btn.clicked.connect(self.render_glyphs)
        layout.addWidget(self.render_btn)
        
        self.setCentralWidget(widget)
        
        self.font_path = None
        self.glyphs_file_path = "characters.txt"
    
    def select_font(self):
        font, _ = QFileDialog.getOpenFileName(self, 'Select Font', '', 'Font Files (*.ttf *.otf)')
        if font:
            self.font_path = font
            self.selected_font_label.setText(f"Selected Font: {os.path.basename(font)}")
    
    def render_glyphs(self):
        if not self.font_path:
            self.statusBar().showMessage("Please select a font.", 5000)
            return
        
        font_size = self.font_size_spinbox.value()
        output_directory = "output"
        create_directory(output_directory)
        
        with open(self.glyphs_file_path, 'r', encoding='utf-8') as file:
            composite_glyphs = [line.strip() for line in file if line.strip()]
        
        for idx, glyph in enumerate(composite_glyphs):
            output_image_path = os.path.join(output_directory, f"character_{idx}.png")
            render_text_to_bitmap(glyph, self.font_path, output_image_path, font_size)
        
        self.statusBar().showMessage("Complete!", 5000)

if __name__ == "__main__":
    locale = QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
    QLocale.setDefault(locale)

    app = QApplication([])
    window = FontRendererApp()
    window.show()
    app.exec()
