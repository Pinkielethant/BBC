import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPalette, QColor

class SEOAnalyzerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('SEO Анализатор текста')
        self.setGeometry(100, 100, 900, 700)
        
        # Установка стиля
        self.setStyleSheet("""
            QMainWindow {
                background-color: #ffa6fc;
            }
            QTextEdit {
                background-color: white;
                border: 1px solid #ff144b;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #ff144b;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e014ff;
            }
            QLabel {
                font-size: 14px;
                color: #333;
            }
            QTableWidget {
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 5px;
                gridline-color: #fdf0ff;
            }
            QHeaderView::section {
                background-color: #fdf0ff;
                padding: 8px;
                border: none;
                font-weight: bold;
            }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #ff144b;
                border-radius: 8px;
                margin-top: 10px;
                font-size: 16px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        title_label = QLabel('SEO Анализатор текста')
        title_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
            padding: 10px;
            text-align: center;
        """)
        main_layout.addWidget(title_label)
        
        # Поле для ввода текста
        text_group = QGroupBox('Введите текст для анализа')
        text_layout = QVBoxLayout()
        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText('Введите текст здесь...')
        self.text_input.setMinimumHeight(150)
        text_layout.addWidget(self.text_input)
        text_group.setLayout(text_layout)
        main_layout.addWidget(text_group)
        # Кнопка анализа
        self.analyze_button = QPushButton('Анализировать текст')
        self.analyze_button.clicked.connect(self.analyze_text)
        main_layout.addWidget(self.analyze_button, alignment=Qt.AlignmentFlag.AlignCenter)
        # Виджет с вкладками для результатов
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)
        # Вкладка со статистикой
        stats_tab = QWidget()
        stats_layout = QVBoxLayout()
        # Статистика текста
        stats_group = QGroupBox('Статистика текста')
        stats_group_layout = QVBoxLayout()
        self.stats_table = QTableWidget()
        self.stats_table.setColumnCount(2)
        self.stats_table.setHorizontalHeaderLabels(['Наименование показателя', 'Значение'])
        self.stats_table.horizontalHeader().setStretchLastSection(True)
        stats_group_layout.addWidget(self.stats_table)
        stats_group.setLayout(stats_group_layout)
        stats_layout.addWidget(stats_group)
        # Семантическое ядро
        semantic_group = QGroupBox('Семантическое ядро')
        semantic_layout = QVBoxLayout()
        self.semantic_table = QTableWidget()
        self.semantic_table.setColumnCount(3)
        self.semantic_table.setHorizontalHeaderLabels(['Фраза/слово', 'Количество', 'Частота, %'])
        self.semantic_table.horizontalHeader().setStretchLastSection(True)
        semantic_layout.addWidget(self.semantic_table)
        semantic_group.setLayout(semantic_layout)
        stats_layout.addWidget(semantic_group)
        stats_tab.setLayout(stats_layout)
        self.tabs.addTab(stats_tab, 'Результаты анализа')
        # Вкладка с советами
        advice_tab = QWidget()
        advice_layout = QVBoxLayout()
        advice_group = QGroupBox('Рекомендации по SEO')
        advice_group_layout = QVBoxLayout()
        self.advice_text = QTextEdit()
        self.advice_text.setReadOnly(True)
        self.advice_text.setStyleSheet("""
            font-size: 14px;
            background-color: #f8f9fa;
        """)
        advice_group_layout.addWidget(self.advice_text)
        advice_group.setLayout(advice_group_layout)
        advice_layout.addWidget(advice_group)
        advice_tab.setLayout(advice_layout)
        self.tabs.addTab(advice_tab, 'Рекомендации')
        # Заполняем тестовыми данными
        self.load_sample_data()
    def load_sample_data(self):
        """Загрузка тестовых данных"""
        sample_text = """Здравствуйте! Это моя пятая домашка"""
        self.text_input.setText(sample_text)
        # Тестовые данные для статистики
        stats_data = [
            ('Количество символов', '-'),
            ('Количество символов без пробелов', '-'),
            ('Количество слов', '-'),
            ('Количество уникальных слов', '-'),
            ('Количество значимых слов', '-'),
            ('Количество стоп-слов', '-'),
            ('Вода', '-'),
            ('Количество грамматических ошибок', '-'),
            ('Классическая тошнота документа', '-'),
            ('Академическая тошнота документа', '-')
        ]
        self.stats_table.setRowCount(len(stats_data))
        for i, (name, value) in enumerate(stats_data):
            self.stats_table.setItem(i, 0, QTableWidgetItem(name))
            self.stats_table.setItem(i, 1, QTableWidgetItem(value))
        # Тестовые данные для семантического ядра
        semantic_data = [
            ('моя', '1', '-'),
        ]
        self.semantic_table.setRowCount(len(semantic_data))
        for i, (phrase, count, frequency) in enumerate(semantic_data):
            self.semantic_table.setItem(i, 0, QTableWidgetItem(phrase))
            self.semantic_table.setItem(i, 1, QTableWidgetItem(count))
            self.semantic_table.setItem(i, 2, QTableWidgetItem(frequency))
        # Тестовые рекомендации
        advice = """📈 Рекомендации по улучшению текста:"""
        self.advice_text.setText(advice)
        # Настройка размеров таблиц
        self.stats_table.resizeRowsToContents()
        self.semantic_table.resizeRowsToContents()
    def analyze_text(self):
        """Анализ текста (заглушка для демонстрации)"""
        text = self.text_input.toPlainText()
        if not text.strip():
            QMessageBox.warning(self, 'Ошибка', 'Введите текст для анализа!')
            return
        # Здесь будет логика анализа текста
        QMessageBox.information(self, 'Анализ завершен', 
                               'Анализ текста выполнен успешно!\n\nПроверьте вкладки с результатами и рекомендациями.')
        # Обновляем таблицы (в реальном приложении здесь будут расчеты)
        self.stats_table.resizeRowsToContents()
        self.semantic_table.resizeRowsToContents()
def main():
    app = QApplication(sys.argv)
    window = SEOAnalyzerApp()
    window.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()