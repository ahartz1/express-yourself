import re
# import textminer.validator as v
# import textminer.separator as s


def phone_numbers(s):
    word_list = re.split('[,.]?\s', s)
    print(word_list)
    ret = []
    word_count = len(word_list)
    for n, word in enumerate(word_list):
        if re.match(r'[\(]?\d{3}[\)]?', word):
            if n < (word_count - 1) and \
               re.match(r'\d{3}\-\d{4}', word_list[n + 1]):
                ret.append('(' + re.sub(r'[\(\)]', '', word) + ')'
                           + ' ' + word_list[n + 1])
    return ret
