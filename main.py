"Module pour vérifier si une chaîne de caractères est un palindrome."
import re
from unidecode import unidecode

#### Fonction secondaire
def ispalindrome(p:str)->bool:
    "fonction qui a pour but de vérifier si une chaine de caractère est un palindrome ou pas"

    #on enleve les caractères spéciaux et les majuscules deviennent des minuscules
    p = unidecode(p)
    p = re.sub(r'[^a-zA-Z0-9]', '', p)
    p = p.lower()  # Met tout en minuscules


    #on inverse la chaine
    s_inverse = p[::-1]

    #on vérifie que la chaine soit un palindrome
    return p==s_inverse

#### Fonction principale
def main():
    "cette fonction teste une liste de caractere"

    test_cases = [
        "radar",
        "kayak",
        "level",
        "rotor",
        "deified",
        "Bonjour",
        "A man a plan a canal Panama",
        "civique"
    ]
    for s in test_cases:
        result = ispalindrome(s)
        if result:
            print(f"Le mot '{s}' est un palindrome.")
        else:
            print(f"Le mot '{s}' n'est pas un palindrome.")


if __name__ == "__main__":
    main()
