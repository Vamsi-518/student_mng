def save_note():
    note = input("Write your note: ")
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    print("Note saved!")

save_note()