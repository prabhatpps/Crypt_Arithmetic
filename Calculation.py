import Question_Frame

# Printing statement
print("Possible solutions for this Cript Arithmetic is given below")

# Main Calculation part
word1 = Question_Frame.word_a_list.copy()
word2 = Question_Frame.word_b_list.copy()
word3 = Question_Frame.word_c_list.copy()

# data assumption
data_assumptions = []

# Create a list of all possible combinations of digits
for a_number_in_data_range in range(10 ** len(Question_Frame.non_data_variables)):
    one_data_str = str(a_number_in_data_range)
    one_data_str = ("0" * (len(Question_Frame.non_data_variables) - len(one_data_str))) + one_data_str
    one_data_list = []
    for a_letter_of_one_data_str in one_data_str:
        one_data_list.append(int(a_letter_of_one_data_str))
    data_assumptions.append(one_data_list)

# unique data assumption
unique_data_assumptions = []

values_input_data = Question_Frame.data_input_dict.values()

for assumption in data_assumptions:
    if len(set(assumption)) == len(assumption):
        for j in values_input_data:
            if j not in assumption:
                unique_data_assumptions.append(assumption)

# Create a list of dictionaries for each combination of digits
assumed_data = []
for one_assumption in unique_data_assumptions:
    one_assumed_data_dict = Question_Frame.data_input_dict.copy()
    for j in range(len(Question_Frame.non_data_variables)):
        one_assumed_data_dict.update({Question_Frame.non_data_variables[j]: one_assumption[j]})
    assumed_data.append(one_assumed_data_dict)

# Testing Cases
for one_assumption in assumed_data:
    word1_to_number_str = ""
    for i in word1:
        if i in one_assumption:
            word1_to_number_str = word1_to_number_str + str(one_assumption[i])
    word1_to_number = int(word1_to_number_str)

    word2_to_number_str = ""
    for i in word2:
        if i in one_assumption:
            word2_to_number_str = word2_to_number_str + str(one_assumption[i])
    word2_to_number = int(word2_to_number_str)

    word3_to_number_str = ""
    for i in word3:
        if i in one_assumption:
            word3_to_number_str = word3_to_number_str + str(one_assumption[i])
    word3_to_number = int(word3_to_number_str)

    if word3_to_number == word1_to_number + word2_to_number:
        print(one_assumption)
