import re
import textminer.validator as v

def words(s):
    ret = []
    word_list = re.split(r' ', s)
    for word in word_list:
        if v.words(word):
            ret.append(word)
    if len(ret) == 0:
        return None
    else:
        return ret

def phone_numbers(s):
    pass        























#
