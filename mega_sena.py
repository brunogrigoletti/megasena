lottery = {}

def read_data():
    try:
        with open('mega_sena.csv', 'r') as file:
            print("Reading data from 'mega_sena.csv'...")
            return file.readlines()
    except FileNotFoundError:
        print("File not found. Please ensure 'mega_sena.txt' exists.")
        return []
    
def process_data(data):
    for i, line in enumerate(data):
        if i == 0:
            continue
        numbers = line.strip().split(";")
        if len(numbers) == 8:
            lottery[numbers[0]] = numbers[2:8]
            # print(f"{numbers[0]}: {', '.join(numbers[2:8])}")
        else:
            print("Invalid line:", line.strip())

def count_frequency(lottery, number, ball):
    count = 0
    if ball == -1:
        for numbers in lottery.values():
            count += numbers.count(number)
    else:
        for numbers in lottery.values():
            if len(numbers) >= ball and numbers[ball - 1] == number:
                count += 1
    return count

def count_all_frequencies(lottery):
    frequency = {}
    for numbers in lottery.values():
        for n in numbers:
            frequency[n] = frequency.get(n, 0) + 1
    return frequency

def export_frequencies():
    with open('frequencies.txt', 'w') as file:
        for number in sorted(frequency, key=lambda x: int(x)):
            general = frequency[number]
            file.write(f"Number {number}:\n")
            file.write(f"  General frequency: {general}\n")
            file.write(f"  Position-based frequencies:\n")
            for pos in range(1, 7):
                freq_pos = count_frequency(lottery, number, pos)
                file.write(f"    Position {pos}: {freq_pos}\n")
            file.write("\n")
    print("All frequencies exported to 'frequencies.txt'!")
    
def main():
    global frequency

    data = read_data()
    if not data:
        return
    
    process_data(data)

    frequency = count_all_frequencies(lottery)
    highest_freq = max(frequency, key=frequency.get)
    print(f"Number with highest frequency: {highest_freq} ({frequency[highest_freq]} times)")
    lowest_freq = min(frequency, key=frequency.get)
    print(f"Number with lowest frequency: {lowest_freq} ({frequency[lowest_freq]} times)")

    export_frequencies()

if __name__ == "__main__":
    main()