# Welcome to Moodia!

### **Live Link: [Moodia](https://moodia-app.herokuapp.com/)**

![Moodia Homepage](react-app/src/images/readme-landing.png)

**Moodia** is a personal well-being application designed to help individuals track their daily mental health. The site allows users to track their moods, habits, and goals, as well as create picture diaries.

Check out the [wiki](https://github.com/hye-kim/moodia/wiki) for more information!

## Technologies

#### Front-End

- React
- Redux
- TailwindCSS

#### Back-End

- Python
- PostgreSQL
- Flask
- SQLAlchemy

## Features

- Create a new account and log in
- Track your mood from 5 different options by date
- Create goals and see the progress towards your completion of the goal
- Upload images and create diary entries on those images

## Instructions

To run this application:

1. Clone this repository (only this branch)

   ```bash
   git clone https://github.com/hye-kim/moodia.git
   ```

2. Install dependencies

   ```bash
   pipenv install --dev -r dev-requirements.txt && pipenv install -r requirements.txt
   ```

3. Create a **.env** file based on the **.env.example** file
4. Setup a PostgreSQL user, password and database that matches the **.env** file

5. Enter the python virtual environment, migrate the database, seed the database, and run the flask app

   ```bash
   pipenv shell
   ```

   ```bash
   flask db upgrade
   ```

   ```bash
   flask seed all
   ```

   ```bash
   flask run
   ```

6. Install front end dependencies from the `react-app` directory and then run the front end server
   ```bash
   npm install && npm run
   ```

## Code Snippets

Users can add moods to a specific calendar date. Creating the calendar component utilized finding the start and end days of the selected month and creating the array of day components populated with data from the mood entry.

```js
const startMonth = new Date(date.getFullYear(), date.getMonth(), 1);
const calendarItems = [];
for (
  let i = 0;
  i <= daysPerMonth[startMonth.getMonth()] + startMonth.getDay() - 1;
  i++
) {
  if (i < startMonth.getDay()) {
    calendarItems.push(<div key={i}></div>);
  } else {
    const calendarPos = i - startMonth.getDay() + 1;
    const c = !moodData[calendarPos]
      ? "white"
      : emoteColors[moodData[calendarPos]?.rating + 2];
    calendarItems.push(
      <CalendarDay
        key={i}
        color={c}
        day={calendarPos}
        date={date}
        setDate={setDate}
      />
    );
  }
}
```

![Moodia Moods](react-app/src/images/readme-mood.gif)
Daily Mood Tracker with Python by NHI VU 
COMING SOON!   

git add .
git commit -m "Initial commit: Added Daily Mood Tracker application"

git add <dailymoodtracker.py>
git commit -m "Description of the update"

git add <dailymoodtracker.py>
git commit -m "Made changes to add mood logging functionality"

## By NHI VU

# Initialize the database
import sqlite3
from datetime import datetime 

def initialize_database():
    conn = sqlite3.connect("mood_tracker.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS moods (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            mood TEXT NOT NULL,
            note TEXT
        )
    """)
    conn.commit()
    conn.close()

# Add a new mood entry

def add_mood():
    date = datetime.now().strftime("%Y-%m-%d")
    mood = input("How are you feeling today? (e.g., Happy, Sad, Neutral): ")
    note = input("Add any notes about your day (optional): ")

    conn = sqlite3.connect("mood_tracker.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO moods (date, mood, note) VALUES (?, ?, ?)", (date, mood, note))
    conn.commit()
    conn.close()

    print("Mood added successfully!")

# View mood history
def view_moods():
    conn = sqlite3.connect("mood_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM moods ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()

    if rows:
        print("\nYour Mood History:")
        for row in rows:
            print(f"Date: {row[1]}, Mood: {row[2]}, Note: {row[3]}")
    else:
        print("No mood entries found.")

# Delete a mood entry
def delete_mood():
    view_moods()
    mood_id = input("Enter the ID of the mood entry you want to delete: ")

    conn = sqlite3.connect("mood_tracker.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM moods WHERE id = ?", (mood_id,))
    conn.commit()
    conn.close()

    print("Mood entry deleted successfully!")

# Main menu
def main():
    initialize_database()

    while True:
        print("\nDaily Mood Tracker")
        print("1. Add Mood")
        print("2. View Moods")
        print("3. Delete Mood")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_mood()
        elif choice == "2":
            view_moods()
        elif choice == "3":
            delete_mood()
        elif choice == "4":
            print("Exiting the application. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
