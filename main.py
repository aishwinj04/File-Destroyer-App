from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog
from PyQt6.QtCore import Qt # alignment 
from pathlib import Path

# slot functions
def open_files():
    global filenames
    filenames, _ = QFileDialog.getOpenFileNames(window, 'Select Files')
    #print(filenames)
    #print(_)
    
    message_format = '\n'.join(filenames)
    message.setText(message_format)


    return filenames

def destory_files():

    for filename in filenames:  # string
        path = Path(filename)  # path object
        print(path)
        with open(path, 'wb') as file:  # file
            file.write(b'')  # overwrite content
        path.unlink()  # delete

    if not filenames:
        message.setText("None Selected")
    else:
     message.setText("Files Deleted")

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
select_btn.clicked.connect(open_files)
layout.addWidget(select_btn, alignment=Qt.AlignmentFlag.AlignCenter) 


# button2 for destroy action 
destroy_btn = QPushButton('Destroy Files')
destroy_btn.setToolTip('Delete Files')
destroy_btn.setFixedWidth(200)
destroy_btn.clicked.connect(destory_files)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)

# output message
message = QLabel('')
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)




window.setLayout(layout)
window.show()
app.exec()