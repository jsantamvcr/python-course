# # #List
# # list_numbers = [1, 2, 3, 4, 5]
# # print(list_numbers)
# # #List with different data types
# # list_mixed = [1, "Hello", 3.14, True]
# # print(list_mixed)
# # #Accessing elements in a list
# # print(list_numbers[0])  # Output: 1
# # print(list_mixed[1])   # Output: Hello
# # #Modifying elements in a list
# # list_numbers[2] = 10
# # print(list_numbers)  # Output: [1, 2, 10, 4

# # #List USA states
# # usa_states = ["California", "Texas", "Florida", "New York", "Illinois"]
# # print(usa_states)

# # # all conutries in America Continet
# # america_countries = ["United States", "Canada", "Mexico"]
# #list all America countries not just USA, CAnadad and Mexico
# # america_countries = ["United States", "Canada", "Mexico", "Brazil", "Argentina", "Colombia", "Chile", "Peru", "Venezuela", "Ecuador", "Bolivia", "Paraguay", "Uruguay", "Guyana", "Suriname", "French Guiana"]
# # print(america_countries)

# #list contries central america
# central_america_countries = []

# #test add several countries to the list
# for country in ["Belize", "Costa Rica", "El Salvador", "Guatemala", "Honduras", "Nicaragua"]:
#     central_america_countries.append(country)
    
# print(central_america_countries)

# central_america_countries = ['uno','dos']

# #extend the list with more countries
# central_america_countries.extend(["Panama", "Costa Rica"])
# print(central_america_countries[456])

#dirty dozen list
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])