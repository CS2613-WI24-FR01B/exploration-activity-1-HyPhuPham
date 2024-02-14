[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/FJiO-WNb)
# EA1
# EXPLOIRATION ACTIVITY 1

## CALCULATOR
This program is a calculator application developed with the purpose is allowing users to implement arithmetic calculation

- **Programming language use:** Python

- **Package use:** PyQt5

- **Reason:** Building an application as a calculator using GUI makes users easier to interact with.

- * Learning this package supports me in building the front-end and back-end of a basic application, and understanding what a software developer does.
 
  * Using PyQt5 which is similar to Java-fx brings me experiences in both Languages when I can flexibly switch between two languages.


## About the PyQt5 package
Definition: Is a cross-platform GUI toolkit, a set of Python bindings for Qt v5. As well as Java-fx of Java, PyQt5 provides easier ways to develop an interactive desktop application. [1]

* **Year of release:** 1998
* **Developer:** Riverbank Computing

### To use
* On the terminal - first we use the command line:

        pip install pyqt5

* On the program 
        
        import sys
        from PyQt5.QtWidgets import...(widgets)"


### Some basic widgets
* QApplication: A class that manages the GUI application's control flow and main settings.

* QMainWindow: A class that allows the application to present on the desktop.

* QPushButton: A class that represents a pushed-button widget. It is a clickable button to trigger any activity in the application.

* QLabel: A class that represents texts or image display widgets.

* QLineEdit: A class that represents a single-line text input box widget.

* QDesktopWidget: A class that provides information about the size, screen geometry, and available space in the user's desktop environment.

### Syntax (Example)
- Create a Calculator class with the construction method

        class Calculator(QMainWindow):
            def __init__(self):
                super().__init__()

- Set up the title for the application
- Concurrently set the size for the application in the display.
                 
                self.setWindowTitle("Calculator")
                self.setGeometry(0, 0, 360, 550) 

  - Center the window on the screen
  
          self.center()
  
- To create a button called "AC" itself

- Set the position and size of the button in order (x-axis, y-axis, length, width)

- Initialize a function to do the activity when pressing the button

        self.button = QPushButton("AC", self)
        self.button.setGeometry(20, 140, 160, 40)
        self.button.clicked.connect(self.process_clear)

- The function does the activity (clear all characters on the input box and display it)
 
        def process_clear(self):
          self.input_field.setText("")


- Main method to run the application and display it on the screen
 
          if __name__ == "__main__":
            app = QApplication(sys.argv)
            window = MyWindow()
            window.show()
            sys.exit(app.exec_())

# Note: TO RUN
 * Step 1: Open the terminal
 * Step 2: Traverse to the folder where the code at (use: "cd <folder_name>")
 * Step 3: Use the command line: python <file_name>.py

<img width="1280" alt="terminal use" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-HyPhuPham/assets/114414645/6afd0109-e9ab-4499-aa8b-fc726679c6f5">

# Reference
[1] https://www.geeksforgeeks.org/python-introduction-to-pyqt5/

## Application Sample Output

# Apperance

<img width="182" alt="Interface" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-HyPhuPham/assets/114414645/e12b6e17-59ec-4900-bf28-ac84ac89a490">

# Fucntions

- An input box to display the chosen character and the result

- Number buttons (from 0 to 9)

- Mathematical symbols (+, -, x, ÷, pi, and =)

- AC (to clear all) and DEL (to erase characters one by one)

## Adding-function
<img width="181" alt="Adding-input2" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-HyPhuPham/assets/114414645/2a512f00-c049-4261-bf70-306a489cab4d">
<img width="180" alt="Sample-output" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-HyPhuPham/assets/114414645/2abb7f1c-e8e7-490d-8fc2-9f24aa7b5995">

## Subtract-function
<img width="184" alt="Subtract-Input" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-HyPhuPham/assets/114414645/72daa1d9-ddbe-43a4-ae2b-6e4c847f8e9e">
<img width="180" alt="Subtract-output" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-HyPhuPham/assets/114414645/f9722416-ac09-4292-9702-40a6308efb67">

## Multiply-function
<img width="176" alt="Mul-input" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-HyPhuPham/assets/114414645/1109cd4d-b378-4a10-9a1f-b2294378968b">
<img width="183" alt="Mul-output" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-HyPhuPham/assets/114414645/ed07ceb6-ebd5-4a7f-8c9c-b2b2d5bffc8d">

## Divide-function
<img width="179" alt="div-input" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-HyPhuPham/assets/114414645/a75527ff-b9f2-409d-9c78-a6a26779ff4c">
<img width="180" alt="div-output" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-HyPhuPham/assets/114414645/4cbdb241-1b3e-43d5-9006-d1b0e8f8dd78">

## Pi number

<img width="178" alt="pi-input" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-HyPhuPham/assets/114414645/24ab0e76-b9f8-47b8-983d-7a64557766df">
<img width="181" alt="pi-output" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-HyPhuPham/assets/114414645/e9b05815-ef5f-4e78-bb6b-b0350189a58e">


