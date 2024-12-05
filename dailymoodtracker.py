import sqlite3
from datetime import datetime

# Initialize SQLite database
conn = sqlite3.connect("mood_tracker.db")
cursor = conn.cursor()

# Create tables if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS mood_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    mood TEXT NOT NULL,
    habits TEXT,
    goals TEXT,
    diary_entry TEXT
)
""")
conn.commit()

def log_mood():
    """Log daily mood, habits, goals, and diary entry."""
    date = datetime.now().strftime("%Y-%m-%d")
    mood = input("How do you feel today? (e.g., Happy, Sad, Neutral): ")
    habits = input("What habits did you engage in today? (e.g., Exercise, Reading): ")
    goals = input("What goals are you focusing on? ")
    diary_entry = input("Write a diary entry for today: ")
    
    cursor.execute("""
    INSERT INTO mood_logs (date, mood, habits, goals, diary_entry)
    VALUES (?, ?, ?, ?, ?)
    """, (date, mood, habits, goals, diary_entry))
    conn.commit()
    print("Mood logged successfully!")

def view_logs():
    """View all mood logs."""
    cursor.execute("SELECT * FROM mood_logs")
    logs = cursor.fetchall()
    
    if not logs:
        print("No logs found.")
        return
    
    print("\n--- Mood Logs ---")
    for log in logs:
        print(f"ID: {log[0]}, Date: {log[1]}, Mood: {log[2]}, Habits: {log[3]}, Goals: {log[4]}")
        print(f"Diary Entry: {log[5]}\n")

def analyze_mood():
    """Analyze mood trends."""
    cursor.execute("SELECT mood FROM mood_logs")
    logs = cursor.fetchall()
    
    if not logs:
        print("No logs available for analysis.")
        return
    
    mood_counts = {}
    for log in logs:
        mood = log[0]
        if mood in mood_counts:
            mood_counts[mood] += 1
        else:
            mood_counts[mood] = 1
    
    print("\n--- Mood Analysis ---")
    for mood, count in mood_counts.items():
        print(f"{mood}: {count} times")

def main_menu():
    """Main menu for the application."""
    while True:
        print("\n--- Daily Mood Tracker ---")
        print("1. Log today's mood")
        print("2. View mood logs")
        print("3. Analyze mood trends")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            log_mood()
        elif choice == '2':
            view_logs()
        elif choice == '3':
            analyze_mood()
        elif choice == '4':
            print("Exiting the application. Stay positive!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
