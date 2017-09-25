# Import pickle package
import pickle

# Open pickle file and load data: d
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))

# <script.py> output:
#   {'Mar': '84.4', 'June': '69.4', 'Airline': '8', 'Aug': '85'}
#   <class 'dict'>
