import os
import io
import pandas as pd

path_file = os.path.join('SMSSpamCollection.txt')
file = io.open(path_file, encoding='utf-8')


def Gen_file():
    num_ham = 0
    num_spam = 0
    for line in file:
        if 'ham\t' in line:
            f = io.open('ham/' + str(num_ham)+'.txt', 'w', encoding='utf-8')
            f.write(line[line.find('\t') + 1:])
            num_ham += 1
            print('message processed - ', num_ham + num_spam)
        else:
            f = io.open('spam/' + str(num_spam) + '.txt', 'w', encoding='utf-8')
            f.write(line[line.find('\t') + 1:])
            num_spam += 1
            print('message processed - ', num_ham + num_spam)

def anls_task1():

    min_len = 100
    max_len = 0
    arr_len = 0
    dirs = ['ham/', 'spam/']
    for dir in dirs:
        list_dir = os.listdir(dir)
        for dir_text in list_dir:
            text = io.open(dir + dir_text, 'r', encoding='utf-8')
            L = len(text.read())
            if L > max_len:
                max_len = L
            if L < min_len:
                min_len = L
            arr_len += L
    arr_len = arr_len / (len(os.listdir('ham/')) + len(os.listdir('spam/')))
    print("max = {} \nmin = {} \narr = {}".format(max_len, min_len, arr_len))

def anls_task2():
    all_text = ''
    dirs = ['ham/', 'spam/']
    for dir in dirs:
        list_dir = os.listdir(dir)
        for dir_text in list_dir:
            text = io.open(dir + dir_text, 'r', encoding='utf-8')
            all_text += text.read() + " "

    d = pd.Series(list(all_text)).value_counts()[:25]
    print(d)

def anls_task3():
    all_text = ''
    dirs = ['ham/', 'spam/']
    for dir in dirs:
        list_dir = os.listdir(dir)
        for dir_text in list_dir:
            text = io.open(dir + dir_text, 'r', encoding='utf-8')
            all_text += text.read() + " "
    all_text = all_text.replace('.', '')
    all_text = all_text.replace(',', '')
    all_text = all_text.replace('!', '')
    all_text = all_text.replace('?', '')
    all_text = all_text.replace(':', '')
    all_text = all_text.replace(';', '')
    all_text = all_text.replace('(', '')
    all_text = all_text.replace(')', '')
    d = pd.Series(all_text.split()).value_counts()[:25]
    print(d)


anls_task3()