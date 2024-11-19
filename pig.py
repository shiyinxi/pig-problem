def pig_latin(sentence):
    # Write your solution here!
    word_list = sentence.split()
    for i in range(len(word_list)):
        if word_list[i][0] not in "aeiou":
            word_list[i] = word_list[i][1:] + word_list[i][0] + 'ay'
        
    return " ".join(word_list)

print(pig_latin("latin is a hard language"))
# Test cases
assert pig_latin("something") == "omethingsay"
assert pig_latin("awesome") == "awesome"
assert pig_latin("latin is a hard language") == "atinlay is a ardhay anguagelay"
assert pig_latin("y") == "yay"
assert pig_latin("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")

