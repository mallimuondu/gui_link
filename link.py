import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('PyQt5 App')  
window.setGeometry(100, 120 , 280 ,80)
window.move(500, 300)
helloMsg = QLabel('<p style="color:red;">My name is malli<p>',parent=window)
helloMsg = QLabel('You have been hacked')
helloMsg.move(60, 30)
window.show()
sys.exit(app.exec_())