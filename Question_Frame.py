# Question frame input
word_a_list1 = list(input("First Word: ").upper())
word_b_list1 = list(input("Second Word: ").upper())
word_c_list1 = list(input("Resulting Word: ").upper())

# Creating a valid range for variables
Number_Range = list(range(10))

# Separating Variables
variables = []
for i in word_a_list1:
    if i not in variables:
        variables.append(i)
for j in word_b_list1:
    if j not in variables:
        variables.append(j)
for k in word_c_list1:
    if k not in variables:
        variables.append(k)

# Taking and arranging given values in dictionary
data_input_dict = {}

for i in range(len(variables)):
    ask_input = input("Want to take input(yes/no): ").upper()
    if ask_input == "YES":
        variable_input = input("Variable: ").upper()
        value_input = int(input("Value: "))
        data_input_dict.update({variable_input: value_input})
    elif ask_input == "NO":
        break

# Arrangement for addition
word_a_list = [0]*(len(word_c_list1)-len(word_a_list1))
word_a_list.extend(word_a_list1)
word_b_list = [0]*(len(word_c_list1)-len(word_b_list1))
word_b_list.extend(word_b_list1)
word_c_list = word_c_list1.copy()

# non data variables
non_data_variables = []
for i in variables:
    if i not in data_input_dict:
        non_data_variables.append(i)
