"""
Author: Nicholas Zankl
Date: September 6, 2026
Course: CSD-325
Assignment: Module 4.2 - High/Low Temperatures
Description: An interactive program that reads 2018 Sitka weather data and
             allows the user to plot daily high temperatures (in red) or
             low temperatures (in blue) using a menu loop until exiting.
"""

import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt


def get_weather_data(filename):
    """Reads the CSV file and returns dates, highs, and lows lists."""
    dates, highs, lows = [], [], []

    try:
        with open(filename, encoding='utf-8') as f:
            reader = csv.reader(f)
            _ = next(reader)

            # Extract date (index 2), high (index 5), and low (index 6)
            for row in reader:
                try:
                    current_date = datetime.strptime(row[2], '%Y-%m-%d')
                    high = int(row[5])
                    low = int(row[6])
                except ValueError:
                    # Skip rows with missing or corrupt data
                    continue
                else:
                    dates.append(current_date)
                    highs.append(high)
                    lows.append(low)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found in the current directory.")
        sys.exit()

    return dates, highs, lows


def plot_temperatures(dates, temperatures, title, color):
    """Plots and formats the weather chart for the specified temperatures."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(dates, temperatures, c=color, alpha=0.8)

    # Format the plot
    plt.title(title, fontsize=20)
    plt.xlabel('Date', fontsize=12)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (°F)", fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.grid(True, linestyle='--', alpha=0.5)

    # Display graph (blocks execution until closed)
    plt.show()


def display_menu():
    """Displays user instructions and interactive menu choices."""
    print("\n" + "=" * 45)
    print("      SITKA WEATHER DATA VISUALIZER (2018)")
    print("=" * 45)
    print("  [H] Highs  - View Daily High Temperatures (Red)")
    print("  [L] Lows   - View Daily Low Temperatures (Blue)")
    print("  [E] Exit   - Exit the application")
    print("=" * 45)


def main():
    """Main execution function to handle data loading and menu loop."""
    filename = 'sitka_weather_2018_simple.csv'
    dates, highs, lows = get_weather_data(filename)

    # Main menu loop
    while True:
        display_menu()
        choice = input("Enter your choice (H, L, or E): ").strip().lower()

        if choice in ['h', 'highs', 'high']:
            print("\nDisplaying Daily High Temperatures...")
            plot_temperatures(dates, highs, "Daily High Temperatures - 2018", 'red')
        elif choice in ['l', 'lows', 'low']:
            print("\nDisplaying Daily Low Temperatures...")
            plot_temperatures(dates, lows, "Daily Low Temperatures - 2018", 'blue')
        elif choice in ['e', 'exit', 'quit']:
            print("\nExiting program. Thank you for using Sitka Weather Visualizer!")
            sys.exit()
        else:
            msg = (
                "\n[!] Invalid selection. "
                "Please enter 'H' for Highs, 'L' for Lows, or 'E' to Exit."
            )
            print(msg)


if __name__ == '__main__':
    main()
