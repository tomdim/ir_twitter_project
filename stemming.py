# -*- coding: cp1253 -*-

##�������� ������� ������������ - ��������� ������� ������������
##�������� �������: HOU-CS-UGP-2013-18
##"���������� ���������� �������� ��������������� ��� ��������������� �������� ���� �������� ������"
##���������� ���������
##��������� ���������: ������ �����������, ����� ��������� �/� & ������������, ������������ ������

##Implementation in Python of the greek stemmer presented by Giorgios Ntais during his master thesis with title
##"Development of a Stemmer for the Greek Language" in the Department of Computer and Systems Sciences
##at Stockholm's University / Royal Institute of Technology.

##The system takes as input a word and removes its inflexional suffix according to a rule based algorithm.
##The algorithm follows the known Porter algorithm for the English language and it is developed according to the
##grammatical rules of the Modern Greek language.

VOWELS = [u'�', u'�', u'�', u'�', u'�', u'�', u'�', u'�', u'�', u'�', u'�', u'�', u'�', u'�', u'�', u'�']

def ends_with(word, suffix):
    return word[len(word) - len(suffix):] == suffix

def stem(word):
    initial = word
    done = len(word) <= 3
    
    ##rule-set  1
    ##���������->����, ������->����
    if not done:
        for suffix in [u'�����', u'����', u'����']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                remaining_part_does_not_end_on = True
                for s in [u'��', u'���', u'���', u'�����', u'�����', u'����', u'�����', u'���', u'���', u'�����']:
                    if ends_with(word, s):
                        remaining_part_does_not_end_on = False
                        break
                if remaining_part_does_not_end_on:
                    word = word + u'��'
                done = True
                break

    ##rule-set  2
    ##�������->���, �������->�����
    if not done:
        for suffix in [u'����', u'����']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                for s in [u'��', u'��', u'���', u'��', u'���', u'���', u'�����', u'���']:
                    if ends_with(word, s):
                        word = word + u'��'
                        break
                done = True
                break

    ##rule-set  3
    ##���������->����, ��������->������
    if not done:
        for suffix in [u'�����', u'�����']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                for s in [u'���', u'������', u'�����', u'���', u'����', u'��', u'�', u'��', u'��', u'���', u'����', u'��', u'��', u'����', u'��']:
                    if ends_with(word, s):
                        word = word + u'���'
                        break
                done = True
                break

    ##rule-set  4
    ##���������->������, ����->��
    if not done:
        for suffix in [u'���', u'���']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                for s in [u'�', u'�', u'��', u'���', u'�', u'�', u'��', u'���']:
                    if ends_with(word, s):
                        word = word + u'�'
                        break
                done = True
                break

    ##rule-set  5
    ##������->����, �������->�����
    if not done:
        for suffix in [u'��', u'���', u'���']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                for s in VOWELS:
                    if ends_with(word, s):
                        word = word + u'�'
                        break
                done = True
                break

    ##rule-set  6
    ##���������->������, ��������->������
    if not done:
        for suffix in [u'���', u'����', u'����', u'����', u'���', u'���']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'��', u'��', u'���', u'����', u'�������', u'��', u'����', u'�����', u'���', u'����', u'���', u'����', u'����',
                            u'������', u'�����', u'����', u'����', u'�������', u'����', u'����', u'���', u'���', u'�������', u'����', u'����',
                            u'������', u'������', u'����', u'�������', u'������', u'����', u'�����', u'����', u'����', u'�����', u'�����',
                            u'���']:
                    word = word + u'��'
                else:
                    for s in VOWELS:
                        if ends_with(word, s):
                            word = word + u'��'
                            break
                done = True
                break

    ##rule-set  7
    ##���������->����, �������->������
    if not done:
        if word == u'�����': word = 2*word
        for suffix in [u'�������', u'�����', u'�����', u'������', u'�����']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'�']:
                    word = word + u'����'
                done = True
                break
        if not done and ends_with(word, u'���'):
            word = word[:len(word) - len(u'���')]
            if word in [u'����', u'����', u'����', u'�����', u'����', u'���', u'���', u'���', u'����', u'���', u'���', u'�']:
                word = word + u'��'
            done = True

    ##rule-set  8
    ##���������->����, �������->������
    if not done:
        for suffix in [u'��������', u'�������', u'�������', u'�������', u'������', u'������', u'������', u'�����', u'�����',
                       u'�����', u'�����']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'��', u'��', u'�']:
                    word = word + u'����'
                done = True
                break
        if not done and ends_with(word, u'���'):
            word = word[:len(word) - len(u'���')]
            if word in [u'�����', u'�����', u'�����', u'�', u'�������', u'�', u'�������', u'������', u'������', u'�����', u'������', u'�',
                        u'��������', u'�', u'���', u'�', u'�����', u'��', u'�����', u'������', u'��������', u'�����', u'�������', u'���',
                        u'�����', u'����', u'��������', u'�', u'������', u'��', u'���', u'���', u'���', u'���', u'����', u'��������', u'���',
                        u'���', u'������', u'�', u'����', u'��', u'����', u'���', u'���', u'������', u'�����', u'���', u'���', u'��', u'����',
                        u'����', u'����', u'�', u'��', u'����', u'�����', u'����', u'����', u'�����', u'����', u'����', u'������', u'���',
                        u'����', u'�������', u'������', u'������', u'����', u'����', u'�����', u'���', u'�����������', u'�������', u'����',
                        u'�������', u'���', u'�����������', u'�����������', u'����', u'��������', u'��������', u'������', u'�������',
                        u'�����', u'������', u'����', u'�������', u'�������', u'����', u'���', u'���', u'������', u'������', u'���������',
                        u'�������']:
                word = word + u'��'
            else:
                for s in VOWELS:
                    if ends_with(word, s):
                        word = word + u'��'
                        break
            done = True

    ##rule-set  9
    ##���������->����, ������->�����
    if not done:
        if ends_with(word, u'�����'):
            word = word[:len(word) - len(u'�����')]
            done = True
        elif ends_with(word, u'���'):
            word = word[:len(word) - len(u'���')]
            if word in [u'����', u'���', u'����', u'���', u'��', u'��', u'��', u'���', u'�����', u'���', u'��', u'���', u'����', u'���', u'���',
                        u'�������', u'����', u'����', u'����', u'���', u'�', u'�', u'��', u'����', u'�']:
                word = word + u'��'
            else:
                for s in [u'��', u'���', u'���', u'���', u'����', u'��', u'���', u'���', u'���', u'�����', u'���', u'���', u'���', u'��', u'���',
                          u'���', u'����', u'���', u'����', u'���', u'���', u'��', u'���', u'���', u'���', u'���', u'���', u'���', u'���', u'���',
                          u'����'] + VOWELS:
                    if ends_with(word, s):
                        word = word + u'��'
                        break
            done = True

    ##rule-set 10
    ##���������->����, ����������->�������
    if not done:
        for suffix in [u'�����', u'�����']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'���']:
                    word = word + u'���'
                elif word in [u'�����', u'���']:
                    word = word + u'���'
                done = True
                break

    ##rule-set 11
    ##�����������->����, ��������->�������
    if not done:
        for suffix in [u'�������', u'������']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'��']:
                    word = word + u'�����'
                done = True
                break

    ##rule-set 12
    ##���������->����, ������->�����
    if not done:
        for suffix in [u'�����']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'�', u'��', u'����', u'�����', u'�����', u'������']:
                    word = word + u'����'
                done = True
                break
    if not done:
        for suffix in [u'����']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'��', u'��', u'�����', u'�', u'�', u'�', u'�������', u'��', u'���', u'���']:
                    word = word + u'���'
                done = True
                break

    ##rule-set 13
    ##��������->�����, ��������->������
    if not done:
        for suffix in [u'�����', u'������', u'�����']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                done = True
                break
    if not done:
        for suffix in [u'���', u'����', u'���']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'����', u'�', u'���������', u'�����', u'����']:
                    word = word + u'��'
                else:
                    for suffix in [u'����', u'�����', u'����', u'��', u'��', u'���']:
                        if ends_with(word, suffix):
                            word = word + u'��'
                            break
                done = True
                break
            
    ##rule-set 14
    ##���������->����, ��������->������
    if not done:
        for suffix in [u'����', u'�����', u'����']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'������', u'���', u'���', u'�����', u'����', u'�����', u'������', u'���', u'�', u'���', u'�', u'�', u'���', u'�����',
                            u'�������', u'��', u'���', u'����', u'������', u'��������', u'��', u'��������', u'�������', u'���', u'���']:
                    word = word + u'���'
                else:
                    for s in [u'�����', u'����', u'������', u'����', u'������', u'����', u'�����', u'���', u'���', u'���', u'��', u'����'] + VOWELS:
                        if ends_with(word, s):
                            word = word + u'���'
                            break
                done = True
                break

    ##rule-set 15
    #��������->����, ��������->�����
    if not done:
        for suffix in [u'���', u'����', u'���']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'�����', u'�����', u'����', u'����', u'�', u'���', u'��', u'����', u'������', u'�����', u'����', u'�����', u'����',
                            u'������', u'������', u'���', u'����', u'�����', u'����', u'����', u'�����', u'��������', u'����', u'����', u'�',
                            u'����', u'���', u'����', u'������', u'����', u'����', u'�����', u'����', u'��', u'����', u'��������', u'�������',
                            u'�', u'���', u'�����', u'���', u'�', u'��', u'�']:
                    word = word + u'��'
                else:
                    for s in [u'��', u'���', u'����', u'��', u'��', u'��', u'��', u'���', u'����']:
                        # ����������: '��'
                        if ends_with(word, s):
                            if not word in [u'���', u'������']:
                                word = word + u'��'
                            break
                done = True
                break

    ##rule-set 16
    ##�������->����, �����->���
    if not done:
        for suffix in [u'���', u'����', u'���']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'�', u'������', u'�������', u'������', u'�������', u'�����', u'������']:
                    word = word + u'��'
                done = True
                break
            
    ##rule-set 17
    ##��������->����, ������->�����
    if not done:
        for suffix in [u'����']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'���', u'��', u'���', u'��', u'���', u'�����', u'�����', u'����', u'�������', u'������']:
                    word = word + u'���'
                done = True
                break
            
    ##rule-set 18
    ##��������->����, �������->������
    if not done:
        for suffix in [u'����', u'������', u'������']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'�', u'�', u'���', u'�����������', u'���������', u'����']:
                    word = word + u'OYN'
                done = True
                break
            
    ##rule-set 19
    ##��������->����, �����->����
    if not done:
        for suffix in [u'����', u'������', u'������']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'��������', u'�', u'�', u'������', u'��', u'��������', u'�����']:
                    word = word + u'���'
                done = True
                break
            
    ##rule-set 20
    ##������->���, ������->�����
    if not done:
        for suffix in [u'����', u'�����', u'�����']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                word = word + u'�'
                done = True
                break
            
    ##rule-set 21
    if not done:
        for suffix in [u'���������', u'��������', u'��������', u'��������', u'��������', u'�������', u'�������', u'�������', u'�������',
                       u'�������', u'�������', u'�������', u'�������', u'�������', u'�������', u'�������', u'������', u'������', u'������',
                       u'������', u'������', u'������', u'������', u'������', u'������', u'������', u'������', u'�����', u'�����', u'�����',
                       u'�����', u'�����', u'�����', u'�����', u'�����', u'�����', u'�����', u'�����', u'�����', u'�����', u'�����',
                       u'�����', u'�����', u'�����', u'�����', u'����', u'����', u'����', u'����', u'����', u'����', u'����', u'����',
                       u'����', u'����', u'����', u'����', u'����', u'����', u'����', u'����', u'���', u'���', u'���', u'���', u'���',
                       u'���', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'�', u'�', u'�', u'�',
                       u'�', u'�', u'�']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                break

    ##rule-set 22
    ##������������->�����, ����������->�����, ���������->����
    if not done:
        for suffix in [u'�����', u'�����', u'����', u'����', u'����', u'����', u'����', u'����']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                break

    return word

