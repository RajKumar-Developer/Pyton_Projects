# Enter the input as Word or Number to convert it into MassCode
#try this it would be more funny work to play with massCode's 
# i had done this with dictonary

mass_code = {
    "a": "._",
    "b": "_...",
    "c": "_._.",
    "d": "_..",
    "e": ".",
    "f": ".._.",
    "g": "__.",
    "h": "....",
    "i": "..",
    "j": ".___",
    "k": "_._",
    "l": "._..",
    "m": "__",
    "n": "_.",
    "o": "___",
    "p": ".__.",
    "q": "__._",
    "r": "._.",
    "s": "...",
    "t": "_",
    "u": ".._",
    "v": "..._",
    "w": ".__",
    "x": "_.._",
    "y": "_.__",
    "z": "__..",
    "1": ".____",
    "2": "..___",
    "3": "...__",
    "4": "...._",
    "5": ".....",
    "6": "_....",
    "7": "__...",
    "8": "___..",
    "9": "____.",
    "0": "_____",
    "@": "@"
}
print("\n\n\n\n\n1. The duration of the dash is 3 times of dot\n"
      "2. Each dot of the dash is followed by the black period which equals to the dot\n"
      "3. space between letter is 3 dots duration \n"
      "4. space between words is 7 dots duration \n"
      "5. The most frequently occurring letter has shorter expression than others.......\n"
      "\t\t\tdon't use any symbols in it\t\t\t")
initial = input("\n\tEnter any word for convert into code:")
word = initial.lower()
result = ""
for letter in word:
    result += mass_code.get(letter, "          ") + "  "
print(result)
