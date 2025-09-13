# main.py
# // MY NAME

def collatz_sequence(n: int) -> list[int]:
    """
    Generates the Collatz sequence starting from the given number n
    until reaching 1.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer")

    sequence = [n]  # start with the input number
    while n != 1:
        if n % 2 == 0:  # if even
            n //= 2
        else:  # if odd
            n = 3 * n + 1
        sequence.append(n)
    return sequence


if __name__ == "__main__":
    number = int(input("Enter a positive integer: "))
    print("Collatz sequence:", collatz_sequence(number))
