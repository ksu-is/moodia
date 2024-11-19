import sqlite3
from datetime import datetime

# Initialize the database
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

git add <dailymoodtracker.py>
git commit -m "Made changes to add mood logging functionality"
