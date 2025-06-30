import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLabel, QPushButton, QHBoxLayout, QMessageBox, QScrollArea
)
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtCore import Qt
from task1 import MTAFeed

class AlertBoard(QWidget):
    def __init__(self, title, lines, icon_path='subway_signs', active=True):
        super().__init__()
        layout = QVBoxLayout(self)
        label = QLabel(title)
        label.setStyleSheet('color: #002d7c; font-family: Arial; font-size: 16px; font-weight: bold;')
        layout.addWidget(label)

        line_layout = QHBoxLayout()
        for line in lines:
            svg_file = os.path.join(icon_path, f"{line}.svg")
            if os.path.exists(svg_file):
                icon = QSvgWidget(svg_file)
                icon.setFixedSize(40, 40)
                line_layout.addWidget(icon)
            else:
                placeholder = QLabel(line)
                placeholder.setStyleSheet("border: 1px solid black; padding: 5px;")
                line_layout.addWidget(placeholder)

        layout.addLayout(line_layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MTA Live Alert Feed")
        self.resize(700, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.title = QLabel("🚇 MTA Subway Service Status")
        self.title.setStyleSheet("font-size: 24px; font-weight: bold; padding: 10px;")
        self.layout.addWidget(self.title)

        self.timestamp_label = QLabel()
        self.layout.addWidget(self.timestamp_label)

        self.alert_container = QVBoxLayout()
        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_widget.setLayout(self.alert_container)
        scroll_area.setWidget(scroll_widget)
        scroll_area.setWidgetResizable(True)
        self.layout.addWidget(scroll_area)

        self.refresh_button = QPushButton("🔄 Refresh")
        self.refresh_button.clicked.connect(self.load_alerts)
        self.layout.addWidget(self.refresh_button)

        self.load_alerts()

    def load_alerts(self):
        try:
            self.feed = MTAFeed()
            self.timestamp_label.setText(f"Last Updated: {self.feed.getRefreshTime().strftime('%Y-%m-%d %H:%M:%S')}")
            self.clear_alerts()

            for status, lines in self.feed.items():
                self.alert_container.addWidget(AlertBoard(status, sorted(lines)))

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load alerts: {str(e)}")

    def clear_alerts(self):
        while self.alert_container.count():
            child = self.alert_container.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()