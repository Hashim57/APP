import os
import csv

def read_rows(filename):
    rows = []
    try:      
        with open(filename) as csvfile:       
            reader = csv.reader(csvfile)      
            for row in reader:       
                rows.append(row)
    except FileNotFoundError:
        print(f"Failed to load {filename}")

    
    return rows


def write_prefs(file_name, prefs, fields):

      with open(file_name, 'w', newline='\n') as csvfile:

          writer = csv.writer(csvfile)

          for pref in prefs.values():

              writer.writerow([pref.person.id, pref.drink.id])

def build_row(row, fields):
        data = []
        for field in fields:
            data.append(getattr(row, field))
        return data


def write_row(file_name, rows, fields):

    

    with open(file_name, 'w', newline='\n') as csvfile:
        writer = csv.writer(csvfile)

        for row in rows:
            writer.writerow(build_row(row, fields))

