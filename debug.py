def has_three_consecutive_double_letters(word):
    count = 0
    i = 0
    
    while i < len(word):
        if word[i] == word[i+1]:
            count += 1
            i = i + 1
            if count == 3:
                return True
            
        else:
            count = 0
            i += 1
            
    return False

word_list = ["bookkeeper","committee","mississippi","bookkeeping","subbookkeeper"]
has_three_consecutive_double_letters(word_list)

for word in word_list:
    if has_three_consecutive_double_letters(word) == True:
        print("Found it:",word)
