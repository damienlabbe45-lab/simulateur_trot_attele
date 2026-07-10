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