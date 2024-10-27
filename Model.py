from textblob import TextBlob
from gingerit.gingerit import GingerIt

class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")
        self.grammar_check = GingerIt()

    def correct_spell(self, text):
        # Split the input text into words and correct each one
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)

    def correct_grammar(self, text):
        try:
            # Parse the text and get the corrected result
            corrected_result = self.grammar_check.parse(text)
            corrected_text = corrected_result['result']
            return corrected_text
        except Exception as e:
            # Handle any errors that occur during parsing
            return f"An error occurred during grammar checking: {e}"

if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "Hello world. I like mashine learning. appple. bananana"
    print("Corrected Spelling:", obj.correct_spell(message))
    print("Corrected Grammar:", obj.correct_grammar(message))

