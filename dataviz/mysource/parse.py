import csv

MY_FILE = "../data/sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-line object."""

    # Open CSV file
    opened_file = open(raw_file)

    # Read CSV file
    csv_data = csv.reader(opened_file, delimiter=delimiter)
    
    # Build a data structure to return parsed_data
    parsed_data = []

    # Skip over the first line of the file for the headers
    # .next() is replaced by __next__() in python
    fields = csv_data.__next__()

    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # Close CSV file
    opened_file.close()
    
    return save_data(parsed_data)

def save_data(data):
    file = open('file.txt', 'w')
    file.write(str(data))
    file.close()
    return file

def main():
    new_data = parse(MY_FILE, ",")

if __name__ == '__main__':
    main()
