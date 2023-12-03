# Take in a word and determine if word is the same backwards and forward
# no built in functions to make reverse function
def my_reverse(word):
    #take in word(string), break it down and flip it
    new_str = ""
    for x in word:
        new_str = x + new_str
    return new_str

word_input = input("Enter word: ").lower()
reversed_word = my_reverse(word_input)

def flip_word():
    # reverse_word = list(word)
    # reverse_word.reverse()
    new_word = ''.join(reversed_word)
    if new_word == word_input:
        print("Palindrome!")
    else:
        print("Non-palindrome!")

flip_word()