def int_func(word):
    return word.capitalize()

usr_text="1"
while not usr_text.isalpha():
    usr_text = input("input text")
usr_text = usr_text.split()
for i, word in enumerate(usr_text):
    usr_text[i] = int_func(word)

print(f"Capitalized text {' '.join(usr_text)}")
