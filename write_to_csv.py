import csv

def write_to_csv(filename, fieldNames, data):
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldNames)
        writer.writeheader()
        writer.writerows(data)

# fn to get the mapped data in-form of [{'sku': 'fdfsdg'}]
def getMappedData(sku_list = []):
    return list(map(lambda item: {'sku': item}, sku_list))


if __name__=='__main__':
    filename = 'products.csv'
    csvFieldNames = ['sku', 'price', 'availability']
    # data = [
    #     {"sku": "B0BM5LV5JK"},
    #     {"sku": "B0BM9S7LM1"},
    #     {"sku": "B09VBZ6PP8"},
    #     ]
    sku_list = ['B084HDTG6R', 'B072VHGQJK']
    data = getMappedData(sku_list)
    write_to_csv(filename,csvFieldNames, data)