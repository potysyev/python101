from googletrans import Translator

translator = Translator()

try:
    with open("ex4.txt", "r", encoding='utf-8') as f_obj, open("ex4_out.txt", "w", encoding='utf-8') as w_obj:
        for line in f_obj:
            result = translator.translate(line, dest="ru", src="en").text
            w_obj.write(result + "\n")

except IOError:
    print("Impossible to read file")
