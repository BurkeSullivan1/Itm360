
"""

# Dictionary example - adding values and printing
capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals['Iowa'])
capitals['Utah']='SaltLakeCity'
print(capitals)
capitals['California']='Sacramento'
print(len(capitals))
for k in capitals:
    print(capitals[k]," is the capital of ", k)
"""
word_list = ['cat','dog','rabbit']
letter_list = [ ]
for a_word in word_list:
    for a_letter in a_word:
        letter_list.append(a_letter)
print(letter_list)

