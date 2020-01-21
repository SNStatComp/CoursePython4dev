#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import sys

def read_csv_column(filename, column_name):
    with open(filename, newline = "") as f:
        reader = csv.DictReader(f)
        
        return [ row[column_name] for row in reader ]
    
def plot_histogram(categories):
    counts = {}
    for category in categories:
        counts[category] = counts.get(category, 0) + 1
        
    for label, count in counts.items():
        print(f"{label[:20]:20} | " + "*" * count)


# In[3]:

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: plot_histogram.py <filename> <column_name>")
        exit(1)

    filename = sys.argv[1]
    colname = sys.argv[2]

    column = read_csv_column(filename, colname)
    plot_histogram(column)

