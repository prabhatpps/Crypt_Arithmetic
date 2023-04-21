import Question_Frame
# draw an addition table
for i in Question_Frame.word_a_list:
    print(i, end=" ")
print()
for i in Question_Frame.word_b_list:
    print(i, end=" ")
print()
for i in range(len(Question_Frame.word_c_list)):
    print("-", end="-")
print()
for i in Question_Frame.word_c_list:
    print(i, end=" ")
print()
for i in range(len(Question_Frame.word_c_list)):
    print("-", end="-")
print()
