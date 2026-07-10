from pandas import DataFrame



"""Ce fichier servira pour la simulation du trot. la constante RESULT_SPEED est la version en DataFrame du tableau 1 de l'exercice 2"""

RESULTS_SPEED = DataFrame(data = [[0, 1, 1, 1, 2, 2], [0, 0, 1, 1, 1, 2], [0, 0, 1, 1, 1, 2], [-1, 0, 0, 1, 1, 1], 
                                  [-1, 0, 0, 0, 1, 1], [-2, -1, 0, 0, 0, 1], [-2, -1, 0, 0, 0, "DQ"]], columns = list(range(1,7)))



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
