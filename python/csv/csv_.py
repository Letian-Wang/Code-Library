''' https://realpython.com/python-csv/ '''

''' Read '''
import csv
with open('read.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {",".join(row)}')
            print('Column names are {}'.format(",".join(row)))
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print('Processed {} lines.'.format(line_count))

''' CSV Read into dictionary (first line is the names)'''
import csv
with open('read.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Column names are {}'.format(",".join(row)))
            line_count += 1
        # print(row.keys())
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}')
        line_count += 1
    print(f'Processed {line_count} lines.')

''' Writing '''
import csv
with open('writing.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

''' Writing a dictionary into csv '''
import csv
with open('writing_a_dictionary.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})

''' Reading with pandas (first line is the names)'''
import pandas
# df = pandas.read_csv('read_pandas.csv')
# df = pandas.read_csv('read_pandas.csv', index_col='Name') # change col
df = pandas.read_csv('read_pandas.csv', index_col='Name', parse_dates=['Hire Date'])    # convert date
df = pandas.read_csv('read_pandas.csv', index_col='Employee', parse_dates=['Hired'], header=0,  # header=0 for ignoring existing column names
                        names=['Employee', 'Hired', 'Salary', 'Sick Days']) # overwrite the column names
print(df)

''' Writing with pandas '''
import pandas
df = pandas.read_csv('read_pandas.csv', index_col='Employee', parse_dates=['Hired'], header=0, names=['Employee', 'Hired', 'Salary', 'Sick Days'])
df.to_csv('write_pandas.csv')