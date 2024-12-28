from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt # alignment 


app = QApplication([])
window = QWidget()
window.setWindowTitle('File Destroyer 3000')
window.setFixedWidth

layout = QVBoxLayout()

# header
header_label = QLabel(
    'Select the files you wish to delete. <font color="red">Warning: This action is destructive!</font>')
layout.addWidget(header_label)

# button1 for file selection
select_btn = QPushButton('Select Files')
select_btn.setToolTip('Select Files') # hover
select_btn.setFixedWidth(200)
layout.addWidget(select_btn, alignment=Qt.AlignmentFlag.AlignCenter) 

# button2 for destroy action 
destroy_btn = QPushButton('Destroy Files')
destroy_btn.setToolTip('Delete Files')
destroy_btn.setFixedWidth(200)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)





window.setLayout(layout)
window.show()
app.exec()