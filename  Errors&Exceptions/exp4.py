# Basic Logging Example
import logging

# Configuration logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# Exp
def calculate_sum(a, b):
    logging.debug(f"Calculating sum of {a} and {b}")
    result = a + b
    logging.info(f"Sum of {a} and {b} is {result}")
    return result

if __name__ == "__main__":
    logging.debug("Starting the program")
    calculate_sum(10, 20)
    logging.debug("Program completed")



# Create logger
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)  # Set global log level

# Create console handler and set level to debug
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add console handler to logger
logger.addHandler(console_handler)

# Example usage
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')