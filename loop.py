import interpreter

is_awake = True
is_asleep = False

while is_awake:
    text = input('IO : ')
    words, unknowns = interpreter.run(text)
    print(words)

    #if is_bored:
        #play()

    #if is_tired:
        #sleep()

while is_asleep:
    #if is_tired:
        #dream()

    #if is_rested:
        #wake_up()

    pass
