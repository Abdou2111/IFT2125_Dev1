# Nom(s) étudiant(s) / Name(s) of student(s):
# Abdelghafour Rahmouni
# Marc Olivier Jean Paul
import sys

# Espace pour fonctions auxillaires :
# Space for auxilary functions :
def get_mediane(list, n):
    # Si pair
    if n % 2 == 0:
        return (list[n // 2 - 1] + list[n // 2]) / 2

    # Si impair
    return list[n // 2]


# Fonction à compléter / function to complete:
def solve(numbers):
    n = len(numbers)
    if n == 0:
        return []
    median = get_mediane(numbers, n)    # O(1)

    left = 0
    right = n - 1

    seen_pairs = set()

    while left < right:
        # O(n), pire cas, on parcourt tout le tableau
        # càd on rentre tjrs soit dans elif soit dans else
        somme = numbers[left] + numbers[right]
        if somme == median:
            pair = (numbers[left], numbers[right])
            seen_pairs.add(pair)
            left += 1
            right -= 1
        elif somme < median:
            left += 1
        else:
            right -= 1

    return list(seen_pairs)


# Ne pas modifier le code ci-dessous :
# Do not modify the code below :

def process_numbers(input_file):
    try:
        # Read integers from the input file
        with open(input_file, "r") as f:
            content = f.read()
        
        # Convert content into a list of integers
        numbers = list(map(int, content.split()))

        pairs = solve(numbers)

        return(len(pairs))

    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python Q3.py <input_file>")
        return

    input_file = sys.argv[1]

    print(f"Input File: {input_file}")
    res = process_numbers(input_file)
    print(f"Result: {res}")

if __name__ == "__main__":
    main()