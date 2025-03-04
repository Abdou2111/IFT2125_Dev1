# Marc Olivier Jean Paul: 20241763
# Abdelghafour Rahmouni: 20246224

import sys

# Espace pour fonctions auxillaires :
# Space for auxilary functions :

# Cette fonction prend en paramètre deux tableaux d'entiers et retourne
# un tableau trié contenant les éléments des deux tableaux.
# Complexité recherchée: O(log(n+m))
# Complexitée obtenue: O(n+m)
def tri(nums1, nums2):
    tab = []                                    # O(1)
    i = 0                                       # O(1)                 
    j = 0
    while i < len(nums1) and j < len(nums2):    # O(n+m)
        if nums1[i] < nums2[j]:                 # O(1)
            tab.append(nums1[i])                # O(1)
            i += 1                              # O(1)
        else:
            tab.append(nums2[j])                # O(1)
            j += 1                              # O(1)
    while i < len(nums1):                       # O(n)
        tab.append(nums1[i])                    # O(1)
        i += 1                                  # O(1)
    while j < len(nums2):                       # O(m)
        tab.append(nums2[j])                    # O(1)
        j += 1                                  # O(1)
    return tab                                  # O(1)

# Fonction à compléter / function to complete:

# Cette fonction prend en paramètre deux tableaux d'entiers et retourne
# la valeur médiane des deux tableaux
# Complexité recherchée: O(log(n+m))
# Complexité obtenue: O(n+m)
def solve(nums1,nums2):
    num = tri(nums1, nums2)                                     # O(n+m)          
    # Cas ou la taille du tableau est paire                                       
    if len(num) % 2 == 0:                                       # O(1)        
        return (num[len(num)//2] + num[len(num)//2 - 1]) / 2    # O(1)
    # Cas ou la taille du tableau est impaire
    else:                                                       # O(1)
        return num[len(num)//2]                                 # O(1)
    

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