from extract_data import *
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB

import random

# Main
if __name__ == '__main__':
    dictX = get_dict_caraX('interest.acl94.txt')
    dictY = get_dictY('interest.acl94.txt')
    dictX_bis = get_dict_motX('interest.acl94.txt')
    vectorized = True
    len_sac_mot = 2

    X, y = get_mot('interest.acl94.txt', len_sac_mot, dictX_bis, dictY, vectorized)
    # X, y = get_carac_mot('interest.acl94.txt', len_sac_mot, dictX, dictY, vectorized)

    moyenne_multinomial = 0
    moyenne_gaussian = 0
    moyenne_aleatoire = 0
    nb_train = 0
    nb_tests = 0
    nb_iter = 0
    for i in range(0, 100):
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)
        nb_tests = len(X_test)
        nb_train = len(X_train)
        naives_bayes_multinomial = MultinomialNB()
        naives_bayes_gaussian = GaussianNB()

        fit_NB_multinomial = naives_bayes_multinomial.fit(X_train, y_train)
        fit_NB_gaussian = naives_bayes_gaussian.fit(X_train, y_train)

        prediction_multinomial = fit_NB_multinomial.predict(X_test)
        prediction_gaussian = fit_NB_gaussian.predict(X_test)

        # Test pour comparer avec l'aléatoire
        y_test_aleatoire = []
        for i in range(0, len(X_test)):
            y_test_aleatoire.append(random.choice(['1', '2', '3', '4', '5', '6']))

        moyenne_multinomial += (prediction_multinomial == y_test).sum() / len(X_test)
        moyenne_gaussian += (prediction_gaussian == y_test).sum() / len(X_test)
        moyenne_aleatoire += (prediction_multinomial == y_test_aleatoire).sum() / len(X_test)
        nb_iter += 1

    print('Nombre d\'entrainements : ', nb_train)
    print('Nombre de tests : ', nb_tests)
    print('Nombre de bonne réponses avec multinomial : ', round(moyenne_multinomial * nb_tests / nb_iter))
    print('Moyenne de bonne réponse avec multinomial : ', round(moyenne_multinomial), '%')
    print('Nombre de bonne réponses avec gaussian : ', round(moyenne_gaussian * nb_tests / nb_iter))
    print('Moyenne de bonne réponse avec gaussian : ', round(moyenne_gaussian), '%')
    print('Moyenne de bonne réponse aléatoire : ', round(moyenne_aleatoire), '%')