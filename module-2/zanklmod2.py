"""
CSD-325 Module 2.2 Assignment
Purpose: Converts Fahrenheit temperatures to Celsius and displays formatted results.
"""

# Student Name: Nicholas Zankl
# Date: August 23, 2026
# Class: CSD-325
# Assignment: Module 2.2 - Documented Debugging
# Purpose: Convert Fahrenheit temperatures to Celsius and display formatted results.

def fahrenheit_to_celsius(fahrenheit):
    """
    Converts a Fahrenheit temperature to Celsius.
    """
    # Apply standard conversion formula: (F - 32) * 5/9
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius

def main():
    """
    Main function to execute temperature conversion test cases.
    """
    # Display program header output
    print("--- Temperature Conversion Program ---")

    # Define list of test temperatures in Fahrenheit
    test_temps = [32, 68, 100, 212]

    # Iterate through test temperatures, convert values, and display output
    for f_temp in test_temps:
        c_temp = fahrenheit_to_celsius(f_temp)
        print(f"{f_temp}°F is equal to {c_temp:.2f}°C")

if __name__ == "__main__":
    # Program entry point execution
    main()
