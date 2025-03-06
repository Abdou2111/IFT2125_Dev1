# Marc Olivier Jean Paul: 20241763
# Abdelghafour Rahmouni: 20246224

import sys

# Espace pour fonctions auxillaires :
# Space for auxilary functions :

# Fonction à compléter / function to complete:

# Cette fonction prend en paramètre deux tableaux d'entiers et retourne
# la valeur médiane des deux tableaux
def solve(nums1,nums2):
    # On s'assure que nums1 est le plus petit tableau
    if len(nums1) > len(nums2):                                 # O(1)                    
        nums1, nums2 = nums2, nums1                             # O(1)
    # On récupère la taille des deux tableaux
    n = len(nums1)                                              # O(1)
    m = len(nums2)                                              # O(1)
    # On initialise les indices min et max
    imin = 0                                                    # O(1)
    imax = n                                                    # O(1)

    # On effectue une recherche dichotomique
    while imin <= imax:                                         # O(log(n+m))
        # On calcule les indices i et j avec j en fonction de i
        i = (imin + imax) // 2                                  # O(1)
        j = (n + m + 1) // 2 - i                                # O(1)

        # On récupère les valeurs max et min des deux tableaux
        if i == 0:                                              # O(1)
            max1 = float('-inf')                                # O(1)
        else:                                                   # O(1)
            max1 = nums1[i - 1]                                 # O(1)
        if i == n:                                              # O(1)
            min1 = float('inf')                                 # O(1)
        else:                                                   # O(1)
            min1 = nums1[i]                                     # O(1)
        
        if j == 0:                                              # O(1)
            max2 = float('-inf')                                # O(1)
        else:                                                   # O(1)
            max2 = nums2[j - 1]                                 # O(1)
        if j == m:                                              # O(1)
            min2 = float('inf')                                 # O(1)
        else:                                                   # O(1)
            min2 = nums2[j]                                     # O(1)

        # On vérifie le nombre d'éléments pour savoir quoi retourner
        if max1 <= min2 and max2 <= min1:                       # O(1)
            if (n + m) % 2 == 0:                                # O(1)
                return (max(max1, max2) + min(min1, min2)) / 2  # O(1)
            else:                                               # O(1)
                return max(max1, max2)                          # O(1)
        
        # on ajuste les indices selons les valeurs
        elif max1 > min2:                                       # O(1)
            imax = i - 1                                        # O(1)
        else:                                                   # O(1)
            imin = i + 1                                        # O(1)
    

# Ne pas modifier le code ci-dessous :
# Do not modify the code below :

# Ne pas modifier le code ci-dessous :

def process_numbers(input_file):
    try:
        # Read integers from the input file
        with open(input_file, "r") as f:
            lines = f.readlines() 
            l0 = list(map(int, lines[0].split()))    
            l1 = list(map(int, lines[1].split()))    

        return solve(l0,l1)
    
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python Q6.py <input_file>")
        return

    input_file = sys.argv[1]

    print(f"Input File: {input_file}")
    res = process_numbers(input_file)
    print(f"Result: {res}")

if __name__ == "__main__":
    main()