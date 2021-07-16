# read & write in csv file

from csv import DictReader, DictWriter
with open('csvfile.csv','r') as rf:
    with open('csvfile2.csv','w') as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf,fieldnames=['first_name','country_name'])
        csv_writer.writeheader()
        for row in csv_reader:
           name, country =  row['name'],row['country']
           csv_writer.writerow({
               'first_name':name.upper(),
               'country_name':country.upper(),
               
           })