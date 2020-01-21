#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv

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


landing_outcomes = read_csv_column("../data/spacex_launch_data.csv", "Landing Outcome")
plot_histogram(landing_outcomes)

