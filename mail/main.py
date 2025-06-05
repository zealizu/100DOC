
with open("/Users/mac/Desktop/Projects/Python/100DOC/mail/Input/Names/invited_names.txt", "r") as names:
    name = names.readlines()

with open("/Users/mac/Desktop/Projects/Python/100DOC/mail/Input/Letters/starting_letter.txt", "r") as text:
    message = text.read()

for i in name:
    with open(f"/Users/mac/Desktop/Projects/Python/100DOC/mail/Output/ReadyToSend/{i}.txt", "w") as ready_message:
        ready_message.write(message.replace("[name]", f"{i.strip()}"))