from pandas import DataFrame
from secrets import SystemRandom



"""Ce fichier servira pour la simulation du trot. la constante RESULT_SPEED est la version en DataFrame du tableau 1 de l'exercice 2
la constante SPEED_DIST représenta la distance parcourue en 10 secondes en fonction de la vitesse"""

RESULTS_SPEED = DataFrame(data = [[0, 1, 1, 1, 2, 2], [0, 0, 1, 1, 1, 2], [0, 0, 1, 1, 1, 2], [-1, 0, 0, 1, 1, 1], 
                                  [-1, 0, 0, 0, 1, 1], [-2, -1, 0, 0, 0, 1], [-2, -1, 0, 0, 0, "DQ"]], columns = list(range(1,7)))

SPEED_DIST = [0, 23, 46, 69, 92, 115, 138]



def input_number_horse() -> int:
    """cette fonction permet de connaître le nombre de chevaux souhaités par l'utilisateur"""
    number_horse = None
    while number_horse is None:
        input_user = input("Veillez indiquer s'il vous plaît un nombre de chevaux entre 12 et 20")
        if input_user.isdigit():
            input_user = int(input_user)
            if 12 >= input_user and input_user<= 20:
                number_horse = input_user
    if isinstance(number_horse , int):
        return number_horse
    

def input_type_run() -> int:
    """cette fonction permet de connaître le type de ccourse souhaités par l'utilisateur"""
    type_run = None
    while type_run is None:
        input_user = input("Veillez indiquer s'il vous plaît le type de course en mettant 3 pour un tiercé, 4 pour un quarté et 5 pour un quinté")
        if input_user == "3"or input_user == "4" or input_user == "5":
                type_run = int(input_user)
    if isinstance(type_run , int):
        return type_run
    

def input_user() -> None:
    """fonction servant juste à avancer la course de 10 secondes pour l'utilisateur"""
    input("veillez appuyer pour faire avancer de 10 secondes la sourse")


def generate_run() -> dict[str, list[int]]:
    """fonction générant un dictionnaire ou la clé est un cheval (horse en aglais signifie cheval) associé 
    à sa distance (la valeur indice 0 en python) et à sa vitesse (valeur indice 1 en python)"""
    number_horse = input_number_horse()
    dict_horse = {}
    for horse in range(1,number_horse + 1):
        dict_horse[f"horse {horse}"] = [0,0]
    return dict_horse



