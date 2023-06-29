import json
import datetime

notes = []  # List to store all the notes

def save_notes():
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)

def load_notes():
    global notes
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

def show_notes():
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Title: {note['title']}")
        print(f"Body: {note['body']}")
        print(f"Last Modified: {note['timestamp']}")
        print("--------------------------")

def add_note():
    title = input("Enter the note title: ")
    body = input("Enter the note body: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Generate a unique ID for the note
    if notes:
        note_id = notes[-1]['id'] + 1
    else:
        note_id = 1

    note = {
        'id': note_id,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }
    notes.append(note)
    print("Note added successfully!")

def edit_note():
    note_id = int(input("Enter the ID of the note you want to edit: "))

    for note in notes:
        if note['id'] == note_id:
            title = input("Enter the new title: ")
            body = input("Enter the new body: ")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            note['title'] = title
            note['body'] = body
            note['timestamp'] = timestamp

            print("Note edited successfully!")
            return

    print("Note not found!")

def delete_note():
    note_id = int(input("Enter the ID of the note you want to delete: "))

    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            print("Note deleted successfully!")
            return

    print("Note not found!")

def find_notes_by_date():
    date = input("Enter the date (YYYY-MM-DD) to find notes last modified on that date: ")

    found_notes = []
    for note in notes:
        if note['timestamp'].startswith(date):
            found_notes.append(note)

    if found_notes:
        print(f"Notes last modified on {date}:")
        for note in found_notes:
            print(f"ID: {note['id']}")
            print(f"Title: {note['title']}")
            print(f"Body: {note['body']}")
            print(f"Last Modified: {note['timestamp']}")
            print("--------------------------")
    else:
        print(f"No notes found last modified on {date}")

def show_menu():
    print("Note Taking App")
    print("1. Show all notes")
    print("2. Add a note")
    print("3. Edit a note")
    print("4. Delete a note")
    print("5. Find notes by date last modified")
    print("6. Exit")

def main():
    load_notes()
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            show_notes()
        elif choice == '2':
            add_note()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            find_notes_by_date()
        elif choice == '6':
            save_notes()
            print("Exiting the application...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()
