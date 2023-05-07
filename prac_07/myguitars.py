import csv


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        return f"{self.name} ({self.year}): ${self.cost:.2f}"

    def __lt__(self, other):
        return self.year < other.year


def read_guitars_from_file(filename):
    guitars = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, year, cost))
    return guitars


def write_guitars_to_file(filename, guitars):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def add_new_guitar(guitars):
    name = input("Enter guitar name: ")
    year = input("Enter guitar year: ")
    cost = input("Enter guitar cost: ")
    guitars.append(Guitar(name, year, cost))
    print("Guitar added successfully.")


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


filename = 'guitars.csv'
guitars = read_guitars_from_file(filename)

print("All guitars:")
display_guitars(guitars)

add_new_guitar(guitars)
write_guitars_to_file(filename, guitars)

print("All guitars after adding new one:")
display_guitars(guitars)

guitars.sort()
print("All guitars sorted by year:")
display_guitars(guitars)
