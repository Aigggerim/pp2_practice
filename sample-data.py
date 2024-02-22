import json

# Load JSON data from file
with open('sample-data.json', 'r') as file:
    data = json.load(file)

# Create the desired output structure
output = {
    "totalCount": str(len(data['imdata'])),
    "imdata": []
}                                                                                           

# Продолжение итерации по каждому элементу в списке 'imdata'
for item in data['imdata']:
    l1_phys_if_attributes = item['l1PhysIf']['attributes']

    # Формирование строки для каждого интерфейса
    interface_info = "{:<50} {:<20} {:<8} {:<6}".format(
        l1_phys_if_attributes['dn'],
        l1_phys_if_attributes['descr'],
        l1_phys_if_attributes['speed'],
        l1_phys_if_attributes['mtu']
    )

    # Вывод строки
    print(interface_info)

# Вывод общего количества интерфейсов
print("=" * 80)
print(f"Total Count: {output['totalCount']}")
