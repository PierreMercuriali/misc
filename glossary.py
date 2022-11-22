"""
	glossary.py 
	glossary system with multiple definitions
"""

def addToDict(dictionary, element, content):
	if element in dictionary.keys():
		dictionary[element].append(content)
	else:
		dictionary[element] = [content]

#load glossaries from files 
glossary = {}

print("Loading aioa...")
with open("aioa.txt", "r", encoding="utf-8") as f:
	data = [l.rstrip() for l in f.readlines()]
for line in data:
	if '–' in line:
		name = line.split("–")[0].lower().rstrip()
		content = [line.split("–")[1], "https://www.archaeological.org/programs/educators/introduction-to-archaeology/glossary/"]
		addToDict(glossary, name, content)
print("\t", len(glossary.keys()), "total entries")

print("Loading manitoba...")
with open("manitoba.txt", 'r', encoding='utf-8') as f:
	data = [l.rstrip() for l in f.readlines()]
for line in data:
	if '.' in line:
		name = line.split('.')[0].lower().rstrip()
		content = ["".join(line.split('.')[1:]), "https://www.umanitoba.ca/faculties/arts/anthropology/manarchnet/appendices/glossary.html"]
		addToDict(glossary, name, content)
print("\t", len(glossary.keys()), "total entries")