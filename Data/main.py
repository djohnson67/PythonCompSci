import csv
import sys
#
# Reads and writes from the aws billing file

def main():

    filters = [
        "GB data transfer out (Canada)",
        "GB data transfer out (United States)",
        "GB data transfer out (Europe)",
        "GB - next 40 TB / month data transfer out",
        "GB - next 100 TB / month data transfer out",
        "GB - next 150 TB / month data transfer out",
        "GB - greater than 150 TB / month data transfer out",
        "GB - first 10 TB / month data transfer out beyond the global free tier",
        "GB - first 50 TB / month of storage used",
        "GB - next 450 TB / month of storage used"
    ]

    fileSource = open(sys.argv[1], "r")
    fileDestination = open(sys.argv[2], "w+")

    delim = ","

    reader = csv.reader(fileSource, delimiter=delim)
    fieldNames = next(reader)
    fileDestination.write(delim.join(fieldNames) + "\n")
    
    for row in reader:
        if not row:
            continue
        
        itemDescription = row[13]
        for filter in filters:
            if filter in itemDescription:
                fileDestination.write(delim.join(row) + "\n")
                break

if __name__ == "__main__":
    main()