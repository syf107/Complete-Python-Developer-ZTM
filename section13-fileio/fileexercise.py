from translate import Translator

trans = Translator(to_lang="de")

with open("test.txt", mode="r") as sentences:
    text = sentences.read()
    translated = (trans.translate(text))
    with open("test-de.txt", mode="w") as sentences2:
        sentences2.write(translated)



