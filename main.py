# keyword argument

def hello(last, first, middle):
    print("\n[ Hello " + last + ' ' + middle + ' ' + first + " ]")


stword = input("\ninput a word: ")
ndword = input("input another word: ")
rdword = input("input another word: ")

hello(last=stword,first=ndword,middle=rdword)