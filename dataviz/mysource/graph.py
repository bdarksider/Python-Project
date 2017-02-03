from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from parse import parse

MY_FILE = "../data/sample_sfpd_incident_all.csv"

def visualize_days():
    """Visualize data by day of week"""

    # parse data
    data_file = parse(MY_FILE, ",")
    counter = Counter([item["DayOfWeek"] for item in data_file])

    data_list = [
                counter["Monday"],
                counter["Tuesday"],
                counter["Wednesday"],
                counter["Thursday"],
                counter["Friday"],
                counter["Saturday"],
                counter["Sunday"]
                ]                

    day_tuple = ("Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun")

    plt.plot(data_list)
    plt.xticks(range(len(day_tuple)), day_tuple)

    plt.savefig("Days.png")

    plt.clf()

def visualize_type():
    """Visualize data by category in a bar graph"""
    data_file = parse(MY_FILE, ",")
    counter = Counter(item["Category"] for item in data_file)

    labels = tuple(counter.keys())

    plt.figure(figsize=(12, 4))

    xlocations = np.arange(len(labels)) + 0.5 

    width = 0.5

    plt.bar(xlocations, counter.values(), width=width)

    plt.xticks(xlocations + width // 2, labels, rotation=90)

    plt.subplots_adjust(bottom=0.5)

   

    plt.savefig("Type.png")

    plt.clf()
    print(xlocations)

def main():
    visualize_type()

if __name__ == "__main__":
    main()
