# Exercise 1 - Reverse the list below in-place using an in-place algorithm.
# For extra credit: Reverse the strings at the same time.

words = ['this' , 'is', 'a', 'sentence', '.']

def reverseSent(z1):
    left = 0
    right = len(alist) - 1
    while left <= right:
        z1[left], z1[right] = z1[right], z1[left]
        left += 1
        right -= 1
    return z1

reverseSent(words)


# Exercise 2 - Create a function that counts how many distinct words are
# in the string below, then outputs a dictionary with the words as the 
# key and the value as the amount of times that word appears in the string.

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

# if a word exists, up the value. if it doesnt, create a new value

def word_count(string):                        # define the function here... Input is the string 
    word_counter_dict = {}                     # building dictionary for our keys, value pairings 
    list_of_words = string.split()             # splitting will create a list of all words in the string
    for pick_word in list_of_words:            # For every word in the list of words...
        count = 0                              # we're setting the default value to 0
        for word in list_of_words:             # inside of this for loop - for every word in the list of words...
            if pick_word == word:              # If the word(key) exists, 
                count +=1                      # up the value by 1 here.
        word_counter_dict[pick_word] = count   # the value of the dictionary is this count integer.
    return word_counter_dict                   # returning the dictionary

word_count(a_text)                             # running our function with our string that was provided (a_text)


# Exercise 3 - Write a program to implement a Linear Search Algorithm. 
# Also in a comment, write the Time Complexity of the following algorithm.


nums_list = [10,23,45,70,11,15]
#If target not inside list, return -1

def linSearch(array, target):           # Create function that will have a list/array and a target value
    for index in range(len(array)-1):   # Create a loop that is checking to see
        if array[index] == target:      # if the index contains the target value
            return index                # If it does, return the index number
    return -1                           # If it doesn't, return -1

linSearch(nums_list,45)                 # Calling function with our nums_list and passing through the target value of 45 which exists in index 2