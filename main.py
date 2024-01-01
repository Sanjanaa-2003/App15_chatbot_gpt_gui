import threading

from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit,QPushButton, QLineEdit
import sys
from backend import ChatBot

class ChatbotWindow(QMainWindow):   #inherit from the QMainwindow class
    def __init__(self):             #define the main method
        super().__init__()          #instantiates the parent of this nethod, ie, QMainWindow
        self.chatbot = ChatBot()

        self.setMinimumSize(700,500)

        #Add chat area widget
        self.chat_area = QTextEdit(self)    #To enter bigger text
        self.chat_area.setGeometry(10,10,480,320)
        self.chat_area.setReadOnly(True)

        #Add the input field widget
        self.input_field = QLineEdit(self)  #To enter bigger text
        self.input_field.setGeometry(10,340,480,40)
        self.input_field.returnPressed.connect(self.send_message)


        #Add the button
        self.button= QPushButton("Send",self)
        self.chat_area.setGeometry(500,340,100,40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style>'color:#333333'>Me: {user_input}</p>")
        self.input_field.clear()

        thread=threading.Thread(target=self.get_bot_response, args=(user_input,))
        thread.start()

    def get_bot_response(self):
        user_input=self.input_field.text().strip()
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'>Bot: {response}</p>")



app=QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
