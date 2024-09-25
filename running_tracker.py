import csv
from datetime import datetime, timedelta

# File to store the data
DATA_FILE = 'running_progress.csv'

def initialize_file():
    with open(DATA_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Week', 'Date', 'Total Distance (km)', 'Long Run (km)', 'Speed Workout', 'Cross-training'])

def add_week_data():
    week = input("Enter week number: ")
    date = input("Enter date (YYYY-MM-DD): ")
    total_distance = input("Enter total distance run this week (km): ")
    long_run = input("Enter long run distance (km): ")
    speed_workout = input("Enter speed workout details: ")
    cross_training = input("Enter cross-training details: ")

    with open(DATA_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([week, date, total_distance, long_run, speed_workout, cross_training])

def view_progress():
    with open(DATA_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))

def main():
    while True:
        print("\n1. Add week's data")
        print("2. View progress")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_week_data()
        elif choice == '2':
            view_progress()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    initialize_file()
    main()