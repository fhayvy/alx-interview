#!/usr/bin/python3
"""Prime Game"""


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def play_game(n):
    move_count = 0
    

def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        current_set = set(range(1, n+1))

        isMariaTurn = True
        is_game_over = False

        while not is_game_over:
            prime_set = []
            for x in current_set:
                if isPrime(x):
                    prime_set.append(x)

                    

                if not prime_set:
                    is_game_over = True




isWinner(5, [2, 5, 1, 4, 3])