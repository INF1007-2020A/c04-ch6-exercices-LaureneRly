#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values=[]

        while len(values) < 10:
                values.append(int(input('Entrer un seul element:\n' )))
    sorted_list = sorted(values)
    print(sorted_list)
    return sorted_list

def anagrams(words: list = None) -> bool:
    if words is None:
        words=[]
        while len(words) < 2:
            words.append((input('Entrer un seul mot en minuscule svp:\n' )))

        # TODO: demander les mots ici

    return sorted(words[0]) == sorted(words[1])


def contains_doubles(items: list) -> bool:
    ensemble = set(items)
    return len(set(items)) != len(items)



def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
       best_student = dict()
       for key, value in student_grades.items():
           avg = sum(value) / len(value)

           if len(best_student) == 0 or list(best_student.values())[0] < avg:
              best_student = {key: avg}

       return best_student


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    frequency = dict()

    for letter in sentence :
        frequency[letter] = sentence.count(letter)

    sorted_keys = sorted(frequency, key=frequency.__getitem__, reverse=True)

    for key in sorted_keys:
        if frequency[key] > 5:
            print("Le caractère {0} revient {1} fois.".format(key, frequency[key]))

    return frequency


def get_recipes(dico):
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    name = input("Entrez le nom de votre recette.\n")
    ingredients = input("Entrez la liste d'ingrédients de la recette, svp séparer les ingrédients par une virgule.\n")
    dico[name] = ingredients
    return dico



def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    name = input("Entrez le nom d'une recette.\n")

    if name in ingredients:
        print(ingredients[name])
    else:
        print("La recette n'existe pas!\n")
        print(f"Les recettes existentes sont: {list(ingredients.keys())}")
        print_recipe(ingredients)



def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes({})
    recipes = get_recipes(recipes)

    print("On affiche une recette au choix...")
    print_recipe(recipes)
    print_recipe(recipes)


if __name__ == '__main__':
    main()
