# string question

# text = "Python Programing"
# consider the given stringg 
# 1.display python
# 2.display programming
# 3`find whether java is present in the string or not if not then include java in betwwen python and programming
# 4. find the length of the new string
# 5. count the number of words in the new string
# 6. Capitalize each word in the new string
# 7. remove all the spaces from the new string and print the new string
# 8. print the frequency of "A","P","R","M"


text = "Python Programing"

print(text[0:6])

print(text[7:18])

if "java" not in text:
    text = text[:6] + " java " + text[6:]
print("New string after including 'java':", text)

print("Length of the new string:", len(text))

word_count = len(text.split())
print("Number of words in the new string:", word_count)

capitalized_text = text.title()
print("Capitalized new string:", capitalized_text)

removed_spaces_text = text.replace(" ", "")
print("New string without spaces:", removed_spaces_text)

print("Frequency of 'A':", text.count("A"),"Frequency of 'P':", text.count("P"), "Frequency of 'R':", text.count("R"), "Frequency of 'M':", text.count("M"))