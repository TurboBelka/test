#!encoding=utf-8
import re


def numb(currentNum):
    arraySimpleNum = []
    for curNum in xrange(1, currentNum + 1):
        for tmpNum in xrange(2, curNum):
            if not (curNum % tmpNum):
                break
        else:
            arraySimpleNum.append(curNum)
    return arraySimpleNum


arr = numb(10)
print(arr)

str_tmp = u"привет мой друг, мой маленький друг"
count = 2


def find(str_tmp, count):
    res_list = []
    words = re.findall(u'[а-яёЁА-Яa-zA-Z]+', str_tmp, re.UNICODE)
    print(','.join(words))
    for curWord in words:
        if curWord not in res_list:
            tmp_count = words.count(curWord)
            if tmp_count >= count:
                res_list.append(curWord)
    return res_list


res = find(str_tmp, 2)
print(','.join(res))


def reverse_num(num):
    flag1 = False

    if num < 0:
        num = 0 - num
        flag1 = True

    res = 0
    p = num

    while p > 0:
        mod1 = p % 10
        p /= 10
        res = res * 10 + mod1

    if flag1:
        res = 0 - res
    return res


res_num = reverse_num(-24)
print res_num


def all_func_of_module(tmp_module):
    for elem in dir(tmp_module):
        tmp = getattr(tmp_module, elem)
        print elem
        if callable(tmp):
            print tmp.__doc__


all_func_of_module(re)
