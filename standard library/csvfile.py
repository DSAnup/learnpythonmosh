import csv

working_dir = "learnpythonmosh/standard library/ecommerce/"

with open(working_dir + "data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["TransactionId", "ProductionID", "Price"])
    writer.writerow([100, 1, 20])
    writer.writerow([101, 1, 50])


with open(working_dir + "data.csv", "r") as file:
    reader = csv.reader(file)
    # print(list(reader))

    for row in reader:
        print(row)
