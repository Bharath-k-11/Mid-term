MID TERM: Advanced Python Calculator 

Project Overview

This midterm assignment involves creating a Python-based calculator application. The project emphasizes software engineering best practices, including writing maintainable and scalable code, implementing appropriate design patterns, incorporating comprehensive logging systems, utilizing environment variables for dynamic configuration, leveraging Pandas for data operations, and developing an interactive command-line interface (REPL) for user interaction. The focus is on building a modular and extensible architecture to simplify future enhancements.

Prerequisites

Python – Ensure that Python is installed and added to the system path.
pip – Python's package manager for installing and managing dependencies.
Installation

Clone the repository:
git clone https://github.com/srikargoud2002/Mid_Term
Navigate to the project directory:
cd Mid_Term
Install the required dependencies:
pip install -r requirements.txt
Make sure that the installation completes without any errors. If there are dependency conflicts, try using a virtual environment:

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Usage

To start the calculator, run the following command:

python main.py
This will launch the REPL interface, where you can perform arithmetic operations, manage calculation history, and access additional functionalities through plugins. If the REPL does not start, verify the Python version and ensure that the necessary dependencies are installed.

Commands

menu – Lists all available plugins.
add <operand1> <operand2> – Performs addition of two numbers.
subtract <operand1> <operand2> – Performs subtraction of two numbers.
multiply <operand1> <operand2> – Performs multiplication of two numbers.
divide <operand1> <operand2> – Performs division of two numbers.
history_show – Displays the calculation history in a formatted list.
history_clear – Clears the calculation history.
history_save – Saves the history into a CSV file with date and time for future reference.
history_load – Loads the history from the available CSV files.
last_op – Shows the last operation performed, along with operands and result.
exit – Exits the calculator application.
Note: The commands are case-sensitive and must be typed exactly as shown. Improper formatting or typos will result in an error message.

Plugins

The calculator supports dynamic loading of plugins. The menu itself is generated by fetching all the available plugins dynamically. If any new plugin is added to the project directory, it will automatically be available in the menu after restarting the application.

Example:
If a new plugin modulus.py is added, the menu command will automatically reflect the new option without needing code changes. This allows for flexible and scalable feature expansion.

Features

Command-Line Interface (REPL)
An interactive environment for performing arithmetic operations and managing calculation history. The REPL accepts direct input, processes commands, and provides real-time feedback.

Plugin System
A system to extend functionalities through dynamically loaded plugins. New plugins can be added without modifying the core codebase, ensuring high extensibility.

Calculation History Management with Pandas
Leverages Pandas for efficient storage, retrieval, and manipulation of calculation history. The history can be exported to CSV files for backup or analysis.

Comprehensive Logging
Implements detailed logging for operations, errors, and informational messages. Logging helps in debugging and tracking the flow of execution during runtime.

Design Patterns
Facade Pattern – Implemented in history management to simplify access to complex underlying functionality.
Command Pattern – Implemented in the commands management to decouple input processing from execution logic.
Factory Method – Implemented in calculation.py to enable creation of objects based on input type.
The design patterns promote modularity, extensibility, and maintainability, making it easier to introduce new features without altering existing code.

Logging

The calculator application uses a comprehensive logging system to record detailed application operations, data manipulations, errors, and informational messages.

Example:
INFO – Records standard operations.
WARNING – Captures potential issues that don't disrupt execution.
ERROR – Logs errors that prevent command execution.
The logging system supports different log levels via environment variables, allowing developers to control the amount of logged information during debugging and production.

Environment Variables

Environment variables are used to set logging levels dynamically, output path of the logs, history saving path, and the environment setting.

Example:

LOG_LEVEL=DEBUG # INFO, WARNING, ERROR, CRITICAL
LOG_OUTPUT=./logs/app.log
HISTORY_PATH=./calculator_history
ENVIRONMENT=DEVELOPMENT
LOG_LEVEL – Controls the verbosity of logs.
LOG_OUTPUT – Specifies the file path for storing log output.
HISTORY_PATH – Directory where calculation history files are stored.
ENVIRONMENT – Sets the current environment mode (e.g., DEVELOPMENT or PRODUCTION).
Ensure that environment variables are configured correctly before starting the application.

Testing & Coverage

Run the following command to execute tests and ensure the application behaves as expected:

pytest
Get coverage details:
pytest --pylint --cov
pylint – Linting ensures that the code adheres to Python's coding standards.
cov – Provides test coverage statistics, highlighting untested code paths.

EAFP & LBYL

LBYL (Look Before You Leap)
This approach is used to validate conditions before attempting operations. It prevents unnecessary errors by checking prerequisites first.

Code example:

if 'divide' in self.command_handler.commands:
    if isinstance(operand2, (int, float)) and operand2 != 0:
        result = operand1 / operand2
        print(f"Result: {result}")
    else:
        print("Invalid operation: Division by zero or invalid operand type.")
else:
    print("Command not found.")
    
In this example, the code checks whether the divide command exists and validates that the second operand is a valid non-zero number before executing the division.

EAFP (Easier to Ask for Forgiveness than Permission)
This approach attempts execution directly and handles any resulting exceptions. It is preferred in Python due to its simplicity and performance.

Code example:

try:
    result = operand1 / operand2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except TypeError:
    print("Operands must be numbers.")
    
In this example, the code directly attempts to divide the operands and handles any exceptions (like division by zero or type errors) that might occur.
