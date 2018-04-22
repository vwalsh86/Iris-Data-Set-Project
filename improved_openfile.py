# Valerie Walsh
# Content for this file taken from https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# Load dataset, clearer looking output to Week 5 attempt 'openfile.py'

import pandas
open = "iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(open, names=names)

print(dataset)