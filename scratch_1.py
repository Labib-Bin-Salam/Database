import csv
import pandas as pd
df = pd.read_csv('database.csv', header=None)
df.to_csv("database.csv", header=["TaskID", 'Priority', 'Category', 'Details', 'Date of entry', 'Deadline', 'Status'], index=False)
tasks = ['TaskID', 'Priority', 'Category', 'Details', 'Date of entry', 'Deadline', 'Status']
database ='database.csv'

def menu():
    print('>>> Welcome To The LSBU Database System <<<')
    print('1.Create')
    print('2.View Data')
    print('3.Search')
    print('4.Update')
    print('5.Delete')
    print('6.Quit')

def create():
    print('... Create Data ...')
    global tasks
    global database

    data = []
    for field in tasks:
        value = input('Enter' + field+ ': ')
        data.append(value)

    with open(database, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([data])
    print('Data saved successfully!')
    input('... Press any key to continue ...')
    return

def view_data():
    global tasks
    global database

    print('>>> DATA RECORD <<<')
    with open(database, 'r', newline='') as file:
        reader = csv.reader(file)
        for x in tasks:
            print(x,end=' | ')

        for row in reader:
            for item in row:
                print(item,end = ' | ')
            print('\n')
    input('... Press any key to continue ...')

def search():
    global tasks
    global database
    TaskID = input("Enter the TaskID: ")
    with open(database, 'r', newline='') as file:
        reader= csv.reader(file)
        for row in reader:
            if len(row) > 0:
                if TaskID == row[0]:
                    print('>>> Data Found! <<<')
                    print('TaskID:', row[0])
                    print('Priority:', row[1])
                    print('Category:', row[2])
                    print('Details:', row[3])
                    print('Date of entry:',row[4])
                    print('Deadline:', row[5])
                    print('Status:', row[6])
                    break
            else:
                print('>>> TaskID not found in Database <<<')
    input('... Press any key to Continue ...')

def update():
    global tasks
    global database

    taskID = input('Enter the TaskID to update: ')
    index_data = None
    updated_data = []
    with open(database, 'r', newline='') as file:
        reader = csv.reader(file)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if taskID == row[0]:
                    index_data = counter
                    #print('Data Found: at index', index_data)
                    data = []
                    for field in tasks:
                        value = input('Enter' + field + ': ')
                        data.append(value)
                    updated_data.append(data)
                else:
                    updated_data.append(row)
                counter +=1
    if index_data is None:
        with open(database, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_data)
    else:
        print('>>> TaskID not found in Database! <<<')
    input('... Press any key to continue ...')

def delete():
    global tasks
    global database

    taskID = input('Enter the TaskID to Update: ')
    data_found = False
    updated_data = []
    with open(database, 'r', newline='') as file:
        reader = csv.reader(file)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if taskID != row[0]:
                    updated_data.append(row)
                    counter +=1
                else:
                    data_found = True
    if data_found is True:
        with open(database, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_data)
            print('Deleted successfully!')
    else:
        print('>>> TasID not found in Database! <<<')
    input('... Press any key to continue ...')

while True:
    menu()

    choice = input('Enter the number to continue: ')
    if choice == '1':
        create()
    elif choice == '2':
        view_data()
    elif choice == '3':
        search()
    elif choice == '4':
        update()
    elif choice == '5':
        delete()
    else:
        break

