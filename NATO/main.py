student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato = pandas.read_csv("100DOC/NATO/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}
# print(nato_dict.values())
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

while True:
    name = input("Please enter your word: ").strip().upper()
    name_list = [n for n in name]
    try:
        nato_name = [nato_dict[n] for n in name_list]
        print(nato_name)
        break
    except KeyError:
        print("Sorry, only letters in the alphabet please.")

