import interpreter

while True:
  text = input('IO : ')
  words = interpreter.run(text)
  print(words)
