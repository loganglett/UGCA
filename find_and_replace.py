#!/usr/bin/python2.7
from tempfile import NamedTemporaryFile
import shutil
import csv
import re

# replace this csv file with the filename you want to store the modified data in
filename1 = 'short_aspirational_dataset.csv'

# replace this csv with the filename which you want to read and replace the words in it
filename = 'edmunds.csv'
tempfile = NamedTemporaryFile(delete=False)

with open(filename, 'rb') as csvFile, tempfile:
    reader = csv.reader(csvFile, delimiter=str(','), quotechar=str('"'))
    writer = csv.writer(tempfile, delimiter=str(','), quotechar=str('"'))

    for row in reader:

        #this item is the forum post
        item = row[2]
        #replace this csv file with the file where you have stored words, modified words
        with open('models_and_brands.csv', 'rb') as csvfile:
            read = csv.reader(csvfile, delimiter=str(','), quotechar=str('|'))
            for row2 in read:
                row[2] = re.sub(r"\b%s\b" % row2[0].lower(),row2[1].lower(), row[2].lower() )

        writer.writerow(row)

shutil.move(tempfile.name, filename1)
print("Written to file", filename1)
