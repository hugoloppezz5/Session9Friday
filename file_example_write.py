#lets create a journal\
with open("journal.txt","a") as journal:
    while True: #infinite loop until q is pressed
        text = input("Enter a journal entry: (press q to quit):")
        if text =="q":
            break
        journal.write(text.capitalize()+"\n") # need to add the new line
