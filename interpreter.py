ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#WORDS

class Word:
  def __init__(self, value = None, type_ = 'WORD'):
    self.type = type_
    self.value = value

  def __repr__(self):
    if self.value:
      return f'{self.type}:{self.value}'
    else:
      return f'{self.type}'

#READER

class Reader:
  def __init__(self, text):
    self.text = text
    self.pos = -1
    self.this_letter = None
    self.advance()

  def make_word(self):
    word_str = ''
    while self.this_letter != None and self.this_letter in ALPHABET:
      word_str += self.this_letter
      self.advance()
  
  def advance(self):
    self.pos += 1
    if self.pos < len(self.text):
      self.this_letter = self.text[self.pos]
    else:
      self.this_letter = None

  def read(self):
    sentence = []
    while self.this_letter != None:
      if self.this_letter in ' \t':
        self.advance()
      elif self.this_letter in ALPHABET:
        sentence.append(self.make_word())
      else:
        sentence.append('!!')
        self.advance()
  return sentence

def run(text):
  reader = Reader(text)
  words = reader.read()
  return words
  
