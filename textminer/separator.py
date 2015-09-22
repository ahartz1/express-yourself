import re
import textminer.validator as v


def words(s):
    if not v.words(s):
        return None
    ret = []
    word_list = re.split(r' ', s)
    for word in word_list:
        if v.words(word):
            ret.append(word)
    return ret


def phone_number(s):
    if v.phone_number(s):
        ret = {}
        p_num = re.sub(r'[^0-9]', '', s)
        ret['area_code'] = p_num[:3]
        ret['number'] = p_num[3:6] + '-' + p_num[6:]
        return ret
    else:
        return None


def money(s):
    if v.money(s):
        ret = {}
        dollars = re.sub(r'[\$,]', '', s)
        ret['currency'] = '$'
        ret['amount'] = float(dollars)
        return ret
    else:
        return None























#
