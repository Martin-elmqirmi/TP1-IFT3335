from sklearn.feature_extraction.text import CountVectorizer
import re

# Description de la fonction dans le fichier pdf
def get_mot(path, len_sac_mots, dictX, dictY, vectorize):
    tab_X = []
    tab_y = []
    interest = re.compile('interest[s]*_[1-6]{1,1}')
    type_egal = re.compile('=+')
    with open(path, encoding="utf8", errors='ignore') as fichier:
        for line in fichier:
            if line != '$$\n':
                new_line = line.replace('[ ', '').replace(' ]', '').split(' ')
                new_tab_int = []
                new_tab_mot = []
                index_interest = 0
                for mot in new_line:
                    if not type_egal.match(mot):
                        new_mot = mot[0:mot.find('/')]
                        if interest.match(new_mot):
                            new_tab_int.append(dictY[new_mot])
                            new_tab_mot.append(new_mot)
                            index_interest = new_tab_mot.index(new_mot)
                        else:
                            new_tab_int.append(dictX[new_mot])
                            new_tab_mot.append(new_mot)
                index_low = index_interest - len_sac_mots
                index_low_temp = index_low
                index_up = index_interest + len_sac_mots + 1
                index_up_temp = index_up
                len_tab = len(new_tab_int)
                if index_low < 0:
                    index_low = 0
                if index_up > len(new_tab_int) - 1:
                    index_up = len(new_tab_int) - 1
                new_tab_int = new_tab_int[index_low:index_up]
                while index_low_temp < 0:
                    new_tab_int.insert(0, 0)
                    index_low_temp += 1
                while index_up_temp > len_tab - 1:
                    new_tab_int.append(0)
                    index_up_temp -= 1
                y = new_tab_int.pop(len_sac_mots)
                X = new_tab_int
                tab_X.append(X)
                tab_y.append(y)
    if vectorize:
        X = tab_X
        vectorizer = CountVectorizer()

        idx = 0
        for item in X:
            X[idx] = ' '.join(str(i) for i in item)
            idx += 1

        X = vectorizer.fit_transform(X)
        X = X.toarray()
        return X, tab_y
    else:
        return tab_X, tab_y


# Description de la fonction dans le fichier pdf
def get_carac_mot(path, len_sac_mots, dictX, dictY, vectorize):
    tab_X = []
    tab_y = []
    interest = re.compile('interest[s]*_[1-6]{1,1}')
    type_egal = re.compile('=+')
    with open(path, encoding="utf8", errors='ignore') as fichier:
        for line in fichier:
            if line != '$$\n':
                new_line = line.replace('[ ', '').replace(' ]', '').split(' ')
                new_tab_int = []
                new_tab_mot = []
                index_interest = 0
                for mot in new_line:
                    if not type_egal.match(mot):
                        new_mot = mot[0:mot.find('/')]
                        if interest.match(new_mot):
                            new_tab_int.append(dictY[new_mot])
                            new_tab_mot.append(new_mot)
                            index_interest = new_tab_mot.index(new_mot)
                        else:
                            new_mot = mot[mot.find('/') + 1:len(mot)]
                            new_tab_int.append(dictX[new_mot])
                            new_tab_mot.append(new_mot)
                index_low = index_interest - len_sac_mots
                index_low_temp = index_low
                index_up = index_interest + len_sac_mots + 1
                index_up_temp = index_up
                len_tab = len(new_tab_int)
                if index_low < 0:
                    index_low = 0
                if index_up > len(new_tab_int) - 1:
                    index_up = len(new_tab_int) - 1
                new_tab_int = new_tab_int[index_low:index_up]
                while index_low_temp < 0:
                    new_tab_int.insert(0, 0)
                    index_low_temp += 1
                while index_up_temp > len_tab - 1:
                    new_tab_int.append(0)
                    index_up_temp -= 1
                y = new_tab_int.pop(len_sac_mots)
                X = new_tab_int
                tab_X.append(X)
                tab_y.append(y)
    if vectorize:
        X = tab_X
        vectorizer = CountVectorizer()

        idx = 0
        for item in X:
            X[idx] = ' '.join(str(i) for i in item)
            idx += 1

        X = vectorizer.fit_transform(X)
        X = X.toarray()
        return X, tab_y
    else:
        return tab_X, tab_y


# Description de la fonction dans le fichier pdf
def get_dictY(path):
    dict_cara = {}
    interest = re.compile('interest[s]*_[1-6]{1,1}')
    type_egal = re.compile('=+')
    with open(path, encoding="utf8", errors='ignore') as fichier:
        for line in fichier:
            if line != '$$\n':
                new_line = line.replace('[ ', '').replace(' ]', '').split(' ')
                for mot in new_line:
                    if not type_egal.match(mot):
                        new_mot = mot[0:mot.find('/')]
                        if interest.match(new_mot):
                            index = new_mot[len(new_mot) - 1:len(new_mot)]
                            if not (new_mot in dict_cara):
                                dict_cara[new_mot] = index
    return dict_cara


# Description de la fonction dans le fichier pdf
def get_dict_motX(path):
    dict_mot = {}
    type_egal = re.compile('=+')
    with open(path, encoding="utf8", errors='ignore') as fichier:
        for line in fichier:
            if line != '$$\n':
                new_line = line.replace('[ ', '').replace(' ]', '').split(' ')
                for mot in new_line:
                    if not type_egal.match(mot):
                        new_mot = mot[0:mot.find('/')]
                        if not (new_mot in dict_mot):
                            dict_mot[new_mot] = len(dict_mot) + 1
    return dict_mot


# Description de la fonction dans le fichier pdf
def get_dict_caraX(path):
    dict_cara = {}
    type_egal = re.compile('=+')
    with open(path, encoding="utf8", errors='ignore') as fichier:
        for line in fichier:
            if line != '$$\n':
                new_line = line.replace('[ ', '').replace(' ]', '').split(' ')
                for mot in new_line:
                    if not type_egal.match(mot):
                        new_mot = mot[mot.find('/') + 1:len(mot)]
                        if not (new_mot in dict_cara):
                            dict_cara[new_mot] = len(dict_cara) + 1
    return dict_cara