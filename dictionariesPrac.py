#COMMIT ATTEMPT 1


#ACTIVITY 1
#1 Print Elizabeth's phone numbers
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

# liz = phonebook_dict.get("Elizabeth")
# print liz
#
# or
#
# print phonebook_dict["Elizabeth"]


#2 ADDS KAREEM TO DICTIONARY

# phonebook_dict["Kareem"] = "938-489-1234"
#
# keys = phonebook_dict.items()
# print keys


#3 DELETES ALICE FROM DICTIONARY

# del phonebook_dict['Alice']
# print phonebook_dict

#4 CHANGES BOB'S PHONE NUMBER

# phonebook_dict['Bob'] = "968-345-2345"
# print phonebook_dict


#5 PRINTS ALL OF THE PHONE NUMBERS BY CALLING ON THE VALUE

#print phonebook_dict.values()


#ACTIVITY 2
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

#1 GET HIS EMAIL ADDRESS

#print ramit["email"]


#2

#print ramit["interests"][0]

#3

#print ramit["friends"][0]["email"]

#4

#print ramit["friends"][1]["interests"][1]

#ACTIVITY 3
# def letter_histogram(word):
#      x = {} #This creates an empty dictionary to add to
#      for char in word:
#          if x.get(char) != None: #This line checks to see if char(the letter)
#                                  #is in the word.  If it is not equal to None
#                                  # we now know that the letter already exists
#                                  #and is currently in the dictionary.
#
#              x[char] += 1        #Increments the counter of the letter by 1 each time.
#
#          if x.get(char) == None: #This line checks to see if char(the letter)
#                                  #is in the word.  If it equals None
#                                  # we now know that the letter has been found
#                                  #and does NOT exist.
#
#             x[char] = 1           #This line give the first instance of the letter
#                                  # value of of 1 and will be increased on the
#                                  # next loop.
#      print x
#
# letter_histogram('sistersister')

#ACTIVITY 4
# my_para = raw_input("Tell me what's on your mind in 50 to 100 words. ")
# def word_histogram(paragraph):
#     wordCount = {}
#     words = my_para.split(" ")
#     for i in range(len(words)):
#         if wordCount.get(words[i]) != None:
#             wordCount[words[i]] += 1
#
#         if wordCount.get(words[i]) == None:
#             wordCount[words[i]] = 1
#             print wordCount
#
# word_histogram(my_para)


#HOW WE DID IT TOGETHER IN class
def isWhiteSpace(character):
    return character == " " or character == "\n" #detects for whitespace and if rolls to a new line

def slice(sentence): #this is a function that to divides a sentence into words
    words = [] #This is an empty list
    begginingOfWord = 0
    currentCharacter = 0
    for character in sentence:   #This will take us through the chacters in the sentence
        if isWhiteSpace(character):
            word = sentence[begginingOfWord:currentCharacter]  #This slices the found letters from the list
            words.append(word.lower()) #This adds and lowercases what we "sliced" from the sentence to the empty list
            begginingOfWord = currentCharacter + 1  #This is a counter that increases allows you to start at the next word by counting the currentCharacter
                                                    # index plus the whitespace
        #    currentCharacter += 1                  These next 2 lines were removed because it is redundant
        #else:
        currentCharacter += 1 # skips past the whitespace to the start of the next word
    return words
def countWords(sentence):
    wordCount = {}
    words = slice(sentence)
    for word in words:
        if word in wordCount:
            wordCount[word] += 1

    else:
        wordCount[word] = 1
    print wordCount



countWords("hello this is my sentence this is a sentence")
