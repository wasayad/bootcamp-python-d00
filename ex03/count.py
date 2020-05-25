def text_analyzer(*args):
    """This function counts the number of upper characters,
    lower characters, punctuation and spaces in a given text."""
    test = ""
    if len(args) > 1:
        return(print("Error number of arguement invalid"))
    elif len(args) is 0 or args[0] is "()":
        test = input()
    else:
        test = "".join(args)
    charup = 0
    space = 0
    charlow = 0
    punct = 0
    character = len(test)
    for i in range(0, len(test)):
        if test[i].isupper() is True:
            charup = charup + 1
        if test[i].islower() is True:
            charlow = charlow + 1
        if test[i] is ' ':
            space = space + 1
        if test[i] is '.' or test[i] is ',':
            punct = punct + 1
        elif test[i] is '?' or test[i] is '!':
            punct = punct + 1
        elif test[i] is ':' or test[i] is ';':
            punct = punct + 1
        elif test[i] is '(' or test[i] is ')':
            punct = punct + 1
        elif test[i] is '\'' or test[i] is '-' or test[i] is '_':
            punct = punct + 1
        elif test[i] is '/':
            punct = punct + 1
        elif test[i] is '[' or test[i] is ']':
            punct = punct + 1
        elif test[i] is '"' or test[i] is '"':
            punct = punct + 1
    print("The text contains", character, "characters:\n")
    print(charup, "upper letters\n")
    print(charlow, "lower letters\n")
    print(punct, "punctuation marks\n")
    print(space, "spaces")
