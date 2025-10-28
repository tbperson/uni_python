from random import randint as roll

combinations = {}


# Roll 2 die 10 thousand times
def generate_combinations():
    for i in range(10000):
        die1 = roll(1, 6)
        die2 = roll(1, 6)
        die3 = roll(1, 6)
        total = die1 + die2 + die3
        if total not in combinations:
            combinations[total] = []
        combinations[total].append((die1, die2, die3))

def check_frequency():
    max_freq = 0
    for total in sorted(combinations.keys()):
        freq = len(combinations[total])
        if freq > max_freq:
            max_freq = freq
            most_frequent_total = total

    print(f"Most frequent total: {most_frequent_total}, Frequency: {max_freq}")

if __name__ == "__main__":
    generate_combinations()
    check_frequency()

### Most likely outcome of 2 die is 7, of 3 die is 11, 