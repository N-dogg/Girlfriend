"""
Returns the number of compatible people
"""

#variables for population
population = None
gender = None
location = None
age = None/population
education = None
attractive = None

#additional variables
reciprocal = None
single = None
match = None

if __name__ == '__main__':
    initial = population*gender*(location/population)*age*education*attractive
    print('Initial estimation: ', round(initial,2))
    refined = initial*reciprocal*single*match
    print('Refined estimation: ', round(refined,2))
    print('Percentage of location: ', refined/population*100,'%')
