from extract_data import *
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

# Main
if __name__ == '__main__':
    dictX = get_dict_caraX('interest.acl94.txt')
    dictY = get_dictY('interest.acl94.txt')
    dictXbis = get_dict_motX('interest.acl94.txt')
    X, y = get_mot('interest.acl94.txt', 1, dictXbis, dictY, True)
    # X, y = get_carac_mot('interest.acl94.txt', 3, dictX, dictY, False)

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)

    for hid in [50, (30, 20, 30), 10]:
        for act in ['relu']:
            moyenne = 0
            nb_iter = 0
            for i in range(0, 5):
                multi_layer = MLPClassifier(hidden_layer_sizes=hid, activation=act)
                fit_NB = multi_layer.fit(X_train, y_train)
                moyenne += fit_NB.score(X_test, y_test)
                nb_iter += 1
            print('Couche de neurones :', hid)
            print('Fonction d\'activation :', act)
            print('Nombre de train : ', len(X_train))
            print('Nombre de tests :', len(X_test))
            print('Bonne réponse :', round(moyenne * len(X_test) / nb_iter))
            print('Moyenne de bonne réponse :', round(moyenne / nb_iter * 100), '%')
            print('\n')
