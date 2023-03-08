import sys

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import *

from api import load_database, search
from ui_MainWindow import Ui_MainWindow

__version__ = '0.2.2'

class ResultWidget(QWidget):
    nameFont = QFont('Consolas', 16)
    nameFont.setBold(True)

    clicked = Signal(dict)

    def __init__(self, result_dict, parent=None):
        super().__init__(parent)

        self.result_dict = result_dict

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignLeft)

        self.labName = QLabel(result_dict['name'], self)
        self.labName.setFont(self.nameFont)
        self.labDescription = QLabel(result_dict['short_description'], self)

        layout.addWidget(self.labName)
        layout.addWidget(self.labDescription)

        self.setLayout(layout)

    def enterEvent(self, event) -> None:
        self.setStyleSheet('background-color: #dcdcdc;')
        return super().enterEvent(event)

    def leaveEvent(self, event) -> None:
        self.setStyleSheet('background-color: #ffffff;')
        return super().leaveEvent(event)

    def mousePressEvent(self, event) -> None:
        self.clicked.emit(self.result_dict)
        return super().mousePressEvent(event)

class OiDictionaryMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Load database & Initialize
        db = load_database()
        self.dicts = [None] * len(db)
        self.dict_chkBox = [None] * len(db)
        layout = QHBoxLayout(self.ui.groupBox_enabledDicts)
        count = 0
        for i, (name, description, data) in enumerate(db):
            self.dicts[i] = data
            count += len(data)
            checkBox = QCheckBox(name, self.ui.groupBox_enabledDicts)
            checkBox.setChecked(True)
            checkBox.setToolTip(description)
            layout.addWidget(checkBox)
            self.dict_chkBox[i] = checkBox
        self.ui.statusbar.showMessage(f'数据库加载完成，共 {count} 条记录。版本号：{__version__}')

        # Initialize result box
        self.resultLayout = QVBoxLayout(self.ui.resultWidget)
        self.ui.resultWidget.setLayout(self.resultLayout)
        self.resultLayout.setAlignment(Qt.AlignTop)

        # Connect slots
        for checkBox in self.dict_chkBox:
            checkBox.stateChanged.connect(self.__update_search_results)
        self.ui.exactSearch.toggled.connect(self.__update_search_results)
        self.ui.searchEdit.textChanged.connect(self.__update_search_results)

    def __get_current_dicts(self):
        result = []
        for dict, chkBox in zip(self.dicts, self.dict_chkBox):
            if chkBox.checkState() == Qt.Checked:
                result += dict
        return result

    @staticmethod
    def __generate_html(word):
        html = f"<h2>{word['name']}</h2><p>{word['description']}</p>"
        if word['sources']:
            html += '<h4>来源</h4><ul>'
            for source in word['sources']:
                html += f'<li><a href="{source}">{source}</a></li>'
            html += '</ul>'
        return html

    def __view_explanation(self, word):
        dialog = QDialog(self)
        dialog.setMinimumWidth(400)
        dialog.setWindowTitle(word['name'] + ' 的释义')

        layout = QVBoxLayout(dialog)
        dialog.setLayout(layout)

        browser = QTextBrowser(dialog)
        layout.addWidget(browser)

        browser.setOpenLinks(True)
        browser.setOpenExternalLinks(True)
        # https://blog.csdn.net/qq_43213582/article/details/104704678
        vsb = browser.verticalScrollBar()
        browser.setMinimumHeight(vsb.maximum() - vsb.minimum() + vsb.pageStep())
        browser.setHtml(self.__generate_html(word))
        dialog.exec()

    def __update_search_results(self, _):
        word = self.ui.searchEdit.text()
        while child := self.resultLayout.takeAt(0):
            child.widget().deleteLater()
        if not word:
            self.ui.statusbar.showMessage('就绪')
            return
        cutoff = 0.7 if self.ui.exactSearch.isChecked() else 0.5
        results = search(word, self.__get_current_dicts(), 20, cutoff)
        self.ui.statusbar.showMessage(f'找到 {len(results)} 个结果。')
        for result in results:
            resultWidget = ResultWidget(result, self.ui.resultWidget)
            resultWidget.clicked.connect(self.__view_explanation)
            self.resultLayout.addWidget(resultWidget)


app = QApplication(sys.argv)

mainform = OiDictionaryMainWindow()
mainform.show()

sys.exit(app.exec())