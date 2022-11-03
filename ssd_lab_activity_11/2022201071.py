import csv

headers = []
data = []

# import csv file
with open("lab_11_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)

    for row in csv_reader:
        data.append(row)

# drop last 6 columns
headers = headers[:-6]
for i in range(len(data)):
    data[i] = data[i][:-6]

# drop rows with % change less than -3
data = list(filter(lambda li: float(li[-1]) >= -3, data))

# calculate average of open, high and low
open_list = list(map(lambda row: float(row[1].replace(",", "")), data))
high_list = list(map(lambda row: float(row[2].replace(",", "")), data))
low_list = list(map(lambda row: float(row[3].replace(",", "")), data))

avg_list = [str(sum(open_list) / len(data)) + "\n", str(sum(high_list) / len(data)) + "\n", str(sum(low_list) / len(data)) + "\n"]
# write avg_list in avg_output.txt
out_file = open("avg_output.txt", "w")
out_file.writelines(avg_list)

char = input()
data = list(filter(lambda row: row[0].startswith(char), data))

# print data
print(headers)
for row in data:
    print(row)

# write data in stock_output.txt
out_file = open("stock_output.txt", "w")
data_str = list(map(lambda row: " ".join(map(str, row)) + "\n", data))

out_file.writelines(data_str)
