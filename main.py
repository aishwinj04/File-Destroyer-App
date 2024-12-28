from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


app = QApplication([])
window = QWidget()
window.setWindowTitle('File Destroyer 3000')

layout = QVBoxLayout()
header_label = QLabel(
    'Select the files you wish to delete. <font color="red">Warning: This action is destructive!</font>')
layout.addWidget(header_label)







window.setLayout(layout)
window.show()
app.exec()