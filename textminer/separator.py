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


def zipcode(s):
    if v.zipcode(s):
        ret = {}
        ret['zip'] = s[:5]
        if len(s) == 10:
            ret['plus4'] = s[6:]
        else:
            ret['plus4'] = None
        return ret
    else:
        return None


def date(s):
    if v.date(s):
        ret = {}
        parsed = re.split(r'[/-]', s)
        if len(parsed[0]) == 4:
            ret['year'] = int(parsed[0])
            ret['month'] = int(parsed[1])
            ret['day'] = int(parsed[2])
        else:
            ret['month'] = int(parsed[0])
            ret['day'] = int(parsed[1])
            ret['year'] = int(parsed[2])
        return ret
    else:
        return None
