import csv

def read_csv(file_path):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def calculate_average_age(data):
    total_age = 0
    for entry in data:
        total_age += int(entry['age'])
    average_age = total_age / len(data)
    return average_age

def main():
    file_path = 'data/sample.csv'
    data = read_csv(file_path)
    print("Data:", data)
    
    average_age = calculate_average_age(data)
    print("Average Age:", average_age)

if __name__ == "__main__":
    main()
