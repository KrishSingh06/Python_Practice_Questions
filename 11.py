#  create set of fruit and   
#  create another set of another fruit  and that are available only in summmer season 
#  create a another set of fruit which are available only in winter season 
#  now perform the following operation these sets 
# 1. print the name of all fruits in 3 sets
# 2. print name of fruit that present in fruits and winter fruits
# 3. print the name of fruits that present in fruits and summer fruits but not in fruits
# 4. print the name of fruits present in  summer fruit , winter fruit but not in fruits
# 5. find whether orange is present in fruits or not
# 6. find which set pine apple is present

fruits = {"apple", "banana", "orange", "grape", "mango", "kiwi", "pear", "peach", "plum", "cherry"}

summer_fruits = {"watermelon", "pineapple", "mango", "peach", "plum"}

winter_fruits = {"grape", "orange", "kiwi", "pear", "cherry"}

Totalfruits = fruits.union(summer_fruits).union(winter_fruits)
print("All fruits in three sets:", Totalfruits)

common_fruits = fruits.intersection(winter_fruits)
print("Fruits present in both fruits and winter season:", common_fruits)

summer_only = summer_fruits - fruits
print("Fruits present only in summer season:", summer_only)

summer_winter = summer_fruits.intersection(winter_fruits) - fruits
print("Fruits present in both summer and winter seasons but not in all fruits:", summer_winter)

if "orange" in fruits:
    print("Orange is present in the fruits set.")
else:
    print("Orange is not present in the fruits set.")

search_fruit = "pineapple"

if search_fruit in summer_fruits:
    print(search_fruit, "is present in the summer fruits set.")
elif search_fruit in winter_fruits:
    print(search_fruit, "is present in the winter fruits set.")
elif search_fruit in fruits:
    print(search_fruit, "is present in the fruits set.")
else:
    print(search_fruit, "is not present in any of the sets.")