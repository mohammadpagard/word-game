text = "hEllO My FriEnDs!!! thIS i$s A tE%sT For your #p#r#o#b#l#e#m a"

def words_check(text):
    length_bad_letters = 0
    half_word_length = 0
    words = []

    words = text.split(' ')
    for word in words:
        bad = [i for i in word if not i.isalpha()]
        if bad != []:
            bad_letters = ''.join(bad).strip()
            length_bad_letters = len(bad_letters)
        if not word.isalpha(): # get bad words 
            if len(word)/2 <= length_bad_letters:
                words.remove(word)

    text = ' '.join(words)

    for word in words:
        bad = [i for i in word if not i.isalpha()]
        if bad != []:
            bad_letters = ''.join(bad).strip()
            length_bad_letters = len(bad_letters)
        if not word.isalpha(): # get bad words
            for i in word: # bad word items
                if i in bad_letters:    # get bad letters
                    text = text.replace(i, '')  # remove bad letters
                    text = text.title()    # clean the text

    return text

def clean_text(text):
    bad = [i for i in text if not i.isalpha()]
    bad_letters = ''.join(bad).strip()
    words = []

    words = text.split(' ')
    for i in words:
        if not i.isalpha(): # get bad words
            for j in i: # bad word items
                if j in bad_letters:    # get bad letters
                    text = text.replace(j, '')  # remove bad letters
                    text = text.title()    # clean the text
    return text

print(words_check(text=text))

# A For Friends Hello Is My Test This Your
