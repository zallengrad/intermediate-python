import pandas as pd
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# student_data_frame = pd.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
# print(alphabet)

dict = { row.letter:row.code for (index, row) in alphabet.iterrows()}
{"A": "Alfa", "B": "Bravo"}
print(dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
masukan = input(f"masukan nama :  ").upper()

# output = [ i.split() for i in masukan ]
# result = { value for (key, value) in dict.items() if key in dict == masukan.split() }
# result = { value for (key, value) in dict.items() if key == masukan.split() }
result = [dict[i ]for i in masukan if i in dict ]
print(result)


