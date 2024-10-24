#Author: Jose Guerrero
#English to Spanish translator

#Dictionary of most common parts of speech (English words, excluding pronouns, articles, verbs, etc)
translation_list = {
    "hello" : "hola",
    "yes" : "si",
    "cat" : "gato",
    "dog" : "perro",
    "time" : "tiempo",
    "person" : "persona",
    "year" : "año",
    "day" : "día",
    "thing" : "cosa",
    "man" : "hombre",
    "woman" : "mujer",
    "world" : "mundo",
    "hand" : "mano",
    "child" : "niño",
    "eye": "ojo",
    "place" : "lugar",
    "week" : "semana",
    "number" : "numero",
    "work" : "trabajo",
    "please" : "por favor",
    "thank you" : "gracias",
}

def translation(): #This fucntion is reponsible for both ensuring that the input is in the dictionary, as well as actually translating the word
    word = input("Please enter any of the following english words (hello,yes,cat, dog, time, person, year, day,thing, man, woman,world,hand,child,eye,place,week,number,work,please, or thank you: ")
    if word in translation_list:
        translate = translator(word)
        print(f"The translation of your word is: {translate}")
    else:
        print("Your word is not on the list, please try again.")

def translator(word): #This function obtains the word from the dictinary
    return translation_list.get(word)

translation() #This is how we initiliaze the program