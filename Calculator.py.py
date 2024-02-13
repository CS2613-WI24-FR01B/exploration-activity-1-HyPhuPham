import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QDesktopWidget
import math

# - This program represent a calculator as an user interface where they can do basic arithmethic operations (+, -, x, /, and pi)
# - The calculator is developed by PyQt5 UI with functions similar to the Java-fx
# - Author: Phu Hy Pham - ID: 3741975

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(0, 0, 360, 550)  # Set initial size (width, height)

        # Center the window on the screen
        self.center()

        #
        self.label = QLabel("STANDARD",self)
        self.label.setGeometry(135, 0, 160, 30)

    # This is called input box where user can type their arithmetics
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(20, 50, 320, 80)

    # Button row 1: including
        # Delete all button
        # Delete each character button
        self.button = QPushButton("AC", self)
        self.button.setGeometry(20, 140, 160, 40)
        self.button.clicked.connect(self.process_clear)

        self.button = QPushButton("DEL", self)
        self.button.setGeometry(180, 140, 160, 40)
        self.button.clicked.connect(self.process_delete)

    # Button row 2: including
        # - number 7 button
        # - number 8 button
        # - number 9 button
        # - adding button

        self.button = QPushButton("7", self)
        self.button.setGeometry(20, 180, 80, 80)
        self.button.clicked.connect(self.n7Val)

        self.button = QPushButton("8", self)
        self.button.setGeometry(100, 180, 80, 80)
        self.button.clicked.connect(self.n8Val)

        self.button = QPushButton("9", self)
        self.button.setGeometry(180, 180, 80, 80)
        self.button.clicked.connect(self.n9Val)

        self.button = QPushButton("+", self)
        self.button.setGeometry(260, 180, 80, 80)
        self.button.clicked.connect(self.process_Add)

    # Button row 3: icluding
        # - number 4 button
        # - number 5 button
        # - number 6 button
        # - subtracting button

        self.button = QPushButton("4", self)
        self.button.setGeometry(20, 260, 80, 80)
        self.button.clicked.connect(self.n4Val)

        self.button = QPushButton("5", self)
        self.button.setGeometry(100, 260, 80, 80)
        self.button.clicked.connect(self.n5Val)

        self.button = QPushButton("6", self)
        self.button.setGeometry(180, 260, 80, 80)
        self.button.clicked.connect(self.n6Val)

        self.button = QPushButton("-", self)
        self.button.setGeometry(260, 260, 80, 80)
        self.button.clicked.connect(self.process_Subtract)

    # Button row 4: icluding
        # - number 1 button
        # - number 2 button
        # - number 3 button
        # - multiply button

        self.button = QPushButton("1", self)
        self.button.setGeometry(20, 340, 80, 80)
        self.button.clicked.connect(self.n1Val)

        self.button = QPushButton("2", self)
        self.button.setGeometry(100, 340, 80, 80)
        self.button.clicked.connect(self.n2Val)

        self.button = QPushButton("3", self)
        self.button.setGeometry(180, 340, 80, 80)
        self.button.clicked.connect(self.n3Val)

        self.button = QPushButton("x", self)
        self.button.setGeometry(260, 340, 80, 80)
        self.button.clicked.connect(self.process_multiply)

    # Button row 5: icluding
        # - symbol pi button
        # - number 0 button
        # - result pi button
        # - dividing button

        self.button = QPushButton("\u03C0", self)
        self.button.setGeometry(20, 420, 80, 80)
        self.button.clicked.connect(self.piVal)

        self.button = QPushButton("0", self)
        self.button.setGeometry(100, 420, 80, 80)
        self.button.clicked.connect(self.n0Val)
 
        self.button = QPushButton("=", self)
        self.button.setGeometry(180, 420, 80, 80)
        self.button.clicked.connect(self.process_result)

        self.button = QPushButton("\u00f7", self)
        self.button.setGeometry(260, 420, 80, 80)
        self.button.clicked.connect(self.process_divide)
        

     
    def center(self):
        frame = self.frameGeometry()
        center_pane = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center_pane)
        self.move(frame.topLeft())

# - This is where the calculator process themself to return value
#   when the users type any button on the calculator
        
# --------- The functions of row 1 --------- 
    # - This function clear each character each time press  
    def process_delete(self):
        current_text = self.input_field.text()
        if len(current_text) >= 0:
            current_text = current_text[:-1]

        self.input_field.setText(current_text)

    # - This function clear all the result and the input box      
    def process_clear(self):
        self.input_field.setText("")

# --------- The functions of row 2 --------- 
    # - This function represent the number 7 on the input box        
    def n7Val(self):
        current_text = self.input_field.text()
        n7Val = current_text = current_text + "7"
        self.input_field.setText(n7Val)

    # - This function represent the number 8 on the input box        
    def n8Val(self):
        current_text = self.input_field.text()
        n8Val = current_text = current_text + "8"
        self.input_field.setText(n8Val)

    # - This function represent the number 9 on the input box        
    def n9Val(self):
        current_text = self.input_field.text()
        n9Val = current_text = current_text + "9"
        self.input_field.setText(n9Val)

    # - This function represent the adding sign on the input box        
    def process_Add(self):
        current_text = self.input_field.text()
        add_sign = current_text = current_text + "+"
        self.input_field.setText(add_sign)


# --------- The functions of row 3 --------- 
    # - This function represent the number 7 on the input box        
    def n4Val(self):
        current_text = self.input_field.text()
        n4Val = current_text = current_text + "4"
        self.input_field.setText(n4Val)

    # - This function represent the number 8 on the input box        
    def n5Val(self):
        current_text = self.input_field.text()
        n5Val = current_text = current_text + "5"
        self.input_field.setText(n5Val)

    # - This function represent the number 9 on the input box        
    def n6Val(self):
        current_text = self.input_field.text()
        n6Val = current_text = current_text + "6"
        self.input_field.setText(n6Val)

    # - This function represent the adding sign on the input box        
    def process_Subtract(self):
        current_text = self.input_field.text()
        minus_sign = current_text = current_text + "-"
        self.input_field.setText(minus_sign)


# --------- The functions of row 4 --------- 
    # - This function represent the number 1 on the input box        
    def n1Val(self):
        current_text = self.input_field.text()
        n1Val = current_text = current_text + "1"
        self.input_field.setText(n1Val)

    # - This function represent the number 2 on the input box        
    def n2Val(self):
        current_text = self.input_field.text()
        n2Val = current_text = current_text + "2"
        self.input_field.setText(n2Val)

    # - This function represent the number 3 on the input box        
    def n3Val(self):
        current_text = self.input_field.text()
        n3Val = current_text = current_text + "3"
        self.input_field.setText(n3Val)

    # - This function represent the multiply sign on the input box        
    def process_multiply(self):
        current_text = self.input_field.text()
        multy_sign = current_text = current_text + "x"
        self.input_field.setText(multy_sign)


# --------- The functions of row 5 --------- 
    # - This function represent the pi sign on the input box        
    def piVal(self):
        current_text = self.input_field.text()
        piVal = current_text = current_text + "\u03C0"
        self.input_field.setText(piVal)

    # - This function represent the number 0 on the input box        
    def n0Val(self):
        current_text = self.input_field.text()
        n0Val = current_text = current_text + "0"
        self.input_field.setText(n0Val)

    # - This function takes responsibility to process the input and return the result on the input box       
    def process_result(self):
        input_text = self.input_field.text()
        number = ''
        operation = "+"
        num_result = 0

        for char in input_text:
            if char.isdigit() or char == '.':
                number += char
            elif char == '\u03C0':
                num_result += math.pi
                number = ''
            else:
                if number:
                    if operation == "+":
                        num_result += int(number)
                    elif operation == "-":
                        num_result -= int(number)
                    elif operation == "x":
                        num_result *= int(number)
                    elif operation == "\u00f7":
                        num_result /= int(number)
                    number = ''
                operation = char

        # Perform the last operation if there's still a number left
        if number:
            if operation == "+":
                num_result += int(number)
            elif operation == "-":
                num_result -= int(number)
            elif operation == "x":
                num_result *= int(number)
            elif operation == "\u00f7":
                num_result /= int(number)

        # Update the input field with the final result
        self.input_field.setText(str(num_result))



    # - This function represent the divide sign on the input box        
    def process_divide(self):
        current_text = self.input_field.text()
        divide_sign = current_text = current_text + "\u00f7"
        self.input_field.setText(divide_sign)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
