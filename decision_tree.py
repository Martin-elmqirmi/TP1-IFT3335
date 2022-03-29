from extract_data import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import random

# Main
if __name__ == '__main__':
    dictX = get_dict_caraX('interest.acl94.txt')
    dictY = get_dictY('interest.acl94.txt')
    dictXbis = get_dict_motX('interest.acl94.txt')
    # X, y = get_mot('interest.acl94.txt', 5, dictXbis, dictY, False)
    X, y = get_carac_mot('interest.acl94.txt', 3, dictX, dictY, False)

    moyenne = 0
    moyenne_aleatoire = 0
    nb_tests = 0
    nb_train = 0
    nb_iter = 0
    for i in range(0, 100):
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)
        nb_tests = len(X_test)
        nb_train = len(X_train)

        decision_tree = DecisionTreeClassifier()

        fit_NB = decision_tree.fit(X_train, y_train)

        prediction = fit_NB.predict(X_test)

        # Test pour comparer avec l'aléatoire
        y_test_aleatoire = []
        for i in range(0, len(X_test)):
            y_test_aleatoire.append(random.choice(['1', '2', '3', '4', '5', '6']))

        moyenne += (prediction == y_test).sum() / len(X_test)
        moyenne_aleatoire += (prediction == y_test_aleatoire).sum() / len(X_test)
        nb_iter += 1

    print('Nombre d\'entrainements : ', nb_train)
    print('Nombre de tests : ', nb_tests)
    print('Nombre de bonne réponses : ', round(moyenne * nb_tests / nb_iter))
    print('Moyenne obtenue avec arbre de décision : ', round(moyenne), '%')
    print('Moyenne aléatoire obtenue : ', round(moyenne_aleatoire), '%')
    # print("NB tests :", len(X_test))
    # print("Bonne réponse :", (prediction == y_test).sum())
    # print("Moyenne :", (prediction == y_test).sum() / len(X_test))

    # test naives bayes avec des sens du mot aléatoire
    # print("Bonne réponse aléatoire :", (prediction == y_test_aleatoire).sum())
    # print("Moyenne aléatoire :", (prediction == y_test_aleatoire).sum() / len(X_test))