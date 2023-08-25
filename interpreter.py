import os
import json
from pathlib import Path
import dictionary_functions as df
from ipapy import UNICODE_TO_IPA

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PUNCTUATION = "-,.;:!?()\'\""

##################################################
#VALUATION
##################################################

"""
Evaluates given statement
Takes word, language, relation, value, for_conversation as inputs

word: Name of the word
language: Language of statement
relation: Way in which word is related to value
value: Given description for word as it relates to it

If for_conversation == True (default)
    Then valuation will be stored in temporary file (conversation.json)
If for_conversation == False
    Then valuation goes to the permanent dictionary
"""

class Valuation:
    #Adds valuation to word.json
    def __init__(self, word, language, relation, value, for_conversation = True):
        #Store data in dictionary using JSON file format
        #All quantities are fully capitalized for dictionary manipulation
        self.word = word.upper()
        self.language = language.upper()
        self.relation = relation.upper()
        self.value = value.upper()
        self.for_conversation = for_conversation
        self.path = self.__get_path()
        self.data = self.__get_data()
        self.__update_file()

    #Retrieves path in directory for word.json
    #Returns path
    def __get_path(self):
        #Retrieve path
        if self.for_conversation == False:
            letters = list(self.word)
            path = Path.cwd().joinpath("dictionary")
            for l in letters:
                if l == " ":
                    path = path.joinpath("_")
                else:
                    path = path.joinpath(f"{l}")
            #If directory doesn't exist, build it
            path.mkdir(parents = True, exist_ok = True)
            path = path.joinpath(f"{self.word}.json")
        else:
            path = Path.cwd().joinpath("conversation.json")
        return path

    #Retrieves data from word.json
    #Returns file contents as dictionary
    def __get_data(self):
        #Check if name has existing file
        if os.path.isfile(self.path):
            file = open(self.path, "a")
        #If not, create new file called word.json
        else:
            file = open(self.path, "x")
            file.write("{}")

        #Returns json file contents
        file = open(self.path, "r")
        return json.loads(file.read())

    #Updates word.json by appending valuation
    def __update_file(self):
        entry = {self.language:{self.relation:self.value}}
        self.data = df.merge(self.data,entry)
        self.data = df.format(self.data)
        file = open(self.path, "w", encoding = "utf-8")
        file.write(self.data)
        file.close()

##################################################
#SENTENCE
##################################################

"""
Transforms sentences into valuations
Takes text as input

text: Input from loop.py
"""

class Sentence:
    def __init__(self, text):
        self.text = text.upper()
        self.position = -1
        self.char = None
        self.__advance()
        self.sentence = self.__read_sentence()

    #Advances position of read character in text
    def __advance(self):
        self.position += 1
        if self.position < len(self.text):
            self.char = self.text[self.position]
        else:
            self.char = None

    #Constructs word from consecutive string of letters
    #Returns word as string
    def __build_word(self):
        word = ''
        while self.char != None and self.char in ALPHABET:
            word += self.char
            self.__advance()
        return word

    #Separates text into component words and punctuation
    #Returns sentence as list
    def __read_sentence(self):
        sentence = []
        while self.char != None:
            if self.char in ' \t':
                self.__advance()
            elif self.char in ALPHABET:
                sentence.append(self.__build_word())
            elif self.char in PUNCTUATION:
                sentence.append(self.char)
                self.__advance()
            else:
                sentence.append(self.char + ' ?')
                self.__advance()
        return sentence

    #Separates sentence into subject and predicate
    def __structure_sentence(self):
        #Check language, use that to check sentence structure type
        #Go through self.sentence and check what parts of speech each word belongs to.
        #If word has no declared part of speech, ask
        #This will results in a list of dictionaries, the key of each is the word or
        #punctuation, the value will be a list of all stated options.
        #Given this, build a list of all possible senteces
        #Each element of list will be a dictionary with subject, verb, and object
        #Use probalistic model and context of conversation to determine
        #most likely meaning out of options
        #If unsure, ask
        #If statement is a question, call a Question instance
        #If statement isn't a question, call a Valuation instance
        #(Store data into conversation.json)
        pass

#def run(text):
    #words = Sentence(text).__read_sentence()
    #return words

Valuation("USES","ENGLISH","IS","THIRD PERSON SINGULAR OF USE", False)
#YES IS NOT NO
