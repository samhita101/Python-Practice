import csv

with open("/Users/vivekgadiraju/Downloads/Python-Masterclass-remastered-shared/Hands_On_Challenges/CSV Files/covid_impact_on_airport_traffic.csv") as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    airports_list = []

    for line in csv_reader:
        airports_list.append(line[3])
        set_list = []

        set_list = set(airports_list)

        for i in set_list:
            set_list.add(i)

print(len(set_list), "is the number of unique airports in the data file.")
