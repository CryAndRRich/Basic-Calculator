# Basic Calculator
This project implements a basic calculator using the Pygame library in Python. It provides a graphical user interface (GUI) for users to enter expressions and view the results
# Features:
* Basic arithmetic operations (`+`, `-`, `*`, `/`)
* Modulo operation (`%`)
* Exponentiation (`^`)
* Factorial (`!`, calculated using `math.factorial`)
* Scientific constants (`e`, calculated using a constant value)
* Trigonometric functions (`sin`, `cos`, `tan`, calculated using `math.sin`, `math.cos`, `math.tan`)
* Logarithmic functions (`ln`, `log`, calculated using `math.log`, `math.log10`)
* `Radian`/`Degree` mode toggle
* Basic error handling (e.g., division by zero)
# Code Structure
The code is organized into three main parts:
* `calculatorScreen` class:
  + Handles the graphical elements of the calculator, including buttons, display area, and text rendering
  + Defines button positions, colors, and labels
  + Provides `handle_click` method to process user interactions with buttons
  + Offers `draw_buttons` and `draw_frame` methods to draw the UI elements
  + Maintains the calculator's state (input text, result text, equal button pressed flag)
* `Calculate` function:
  + Takes an expression string as input and performs the calculations using a stack-based approach
  + Supports various mathematical operations and functions, including handling nested parentheses and error conditions
  + Uses a global variable `isRadian` to track the mode for trigonometric functions
* `Calculator` function:
  + The main loop of the program, handling user input (mouse clicks) and updating the display based on button presses and calculations
  + Creates a `calculatorScreen` object to manage the GUI
  + Continuously loops to check for events (quit or mouse clicks)
  + Processes mouse clicks using `screen.handle_click(event.pos)`
  + Evaluates expressions using `Calculate` when the equal button is pressed
  + Handles errors and displays appropriate messages (e.g., `"Stop! Too long!"` for lengthy expressions)
  + Updates the screen using `screen.update_display()` and `pygame.display.update()`
# Additional Notes
This is not the best version of the calculator yet, so if you're interested in improving it:
* Feel free to customize the calculator's appearance and functionality by modifying the code within the classes
* There are still some minor errors in the calculation due to the irrational nature of `e` (for example, if you calculate `ln(e)`, the result will be `1.0000000000003135`)
* Consider adding more advanced features like memory functions(`Ans`), scientific constants(e.g., `pi`) and absolute value(`| |`)
* Try adding advanced arithmetic operations such as permutation(`P(n,r)`), combination(`C(n,r)`) and complex number(`i`)
