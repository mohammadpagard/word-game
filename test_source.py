import pytest
import time
from source import WordsCheck


class TestWordsGame:
    @pytest.fixture
    def setup(self):
        self.word1 = WordsCheck("hEllO My FriEnDs!!! thIS i$s A tE%sT For your #p#r#o#b#l#e#m a")
        self.word2 = WordsCheck('''hEllO My FriEnDs!!!
                                            thIS is A tEsT For your #p#r#o#b#l#e#m''')
        self.word3 = WordsCheck('''HeLLLO_O My________________FRIEND
                                            HOW ARE YOUUUUU?___?
                                            I Don'T KNow Y_O_U_R_N_A_M_E yet !!!!!!!!''')
        yield 'setup'
        time.sleep(1)

    def test_words_check(self, setup):
        assert self.word1.words_check() == {'A': 2, 'For': 1, 'Friends': 1, 'Hello': 1, 'Is': 1, 'My': 1, 'Test': 1, 'This': 1, 'Your': 1}
        assert self.word2.words_check() == {'A': 1, 'For': 1, 'Friends': 1, 'Hello': 1, 'Is': 1, 'My': 1, 'Test': 1, 'This': 1, 'Your': 1}
        assert self.word3.words_check() == {'Are': 1, 'Dont': 1, 'Hellloo': 1, 'How': 1, 'I': 1, 'Know': 1, 'Yet': 1, 'Yourname': 1, 'Youuuuu': 1}

    def test_clean_text(self, setup):
        assert self.word1.clean_text() == 'Hello My Friends This Is A Test For Your Problem A'
        assert self.word2.clean_text() == 'Hello My Friends                                            This Is A Test For Your Problem'
