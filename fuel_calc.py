# Name: Miranda Towne
# Description: A basic fuel cost calculater

# Brief description of program
print('Automobile Fuel Cost Calculator')
print('Use this program to help you calculate your monthly fuel cost')

# Input from user
mpg = float (input("Please enter the car's MPG (miles per gallon): "))
aMiles = int(input('Please enter the average number of miles driven per month: '))
pGallon = float(input('Please enter the cost of fuel per gallon: '))

# User input summarized
print("\n"'Given price of fuel at' + " $" + str(pGallon) + '/gallon and' + " " + str(aMiles) + " " + 'miles/month traveled: ')

# Gallons per month
gal_per_month =  aMiles / mpg
print("\n"'Gallons used each month: {0:.1f} gallons'.format(gal_per_month))

# Cost of fuel per month
fuel_cost = gal_per_month * pGallon
print("\n"'Monthly cost of fuel: ${0:.2f}'.format(fuel_cost))
