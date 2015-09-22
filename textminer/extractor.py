import re
import textminer.validator as v

def phone_numbers(s):
    word_list = re.split('[\)]\s', s)
    print(word_list)
    ret = []
    for word in word_list:
        if phone_number(word):
            ret.append(word)
