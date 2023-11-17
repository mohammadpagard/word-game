class WordsCheck:
    def __init__(self, text):
        self.text = text

    def words_check(self):
        length_bad_letters = 0
        words = []
        words = self.text.split(' ')

        for word in words:
            bad = [i for i in word if not i.isalpha()]
            if bad != []:
                bad_letters = ''.join(bad).strip()
                length_bad_letters = len(bad_letters)
            if not word.isalpha(): # get bad words 
                if len(word)/2 <= length_bad_letters:
                    words.remove(word)

        self.text = ' '.join(words)

        for word in words:
            bad = [i for i in word if not i.isalpha()]
            if bad != []:
                bad_letters = ''.join(bad).strip()
                length_bad_letters = len(bad_letters)
            if not word.isalpha(): # get bad words
                for i in word: # bad word items
                    if i in bad_letters:    # get bad letters
                        self.text = self.text.replace(i, '')  # remove bad letters
                        self.text = self.text.title()    # clean the text

        word_lines = self.text.splitlines()
        self.text = ' '.join(word_lines)
        counter = {}
        text_words = self.text.split(' ')
        for word in sorted(text_words):
            if word not in counter:
                counter[word] = 1
            else:
                counter[word] += 1

        counter.pop('', None)

        return counter

    def clean_text(self):
        bad = [i for i in self.text if not i.isalpha()]
        bad_letters = ''.join(bad).strip()
        words = []

        words = self.text.split(' ')
        for i in words:
            if not i.isalpha(): # get bad words
                for j in i: # bad word items
                    if j in bad_letters:    # get bad letters
                        self.text = self.text.replace(j, '')  # remove bad letters
                        self.text = self.text.title()    # clean the text
        return self.text
