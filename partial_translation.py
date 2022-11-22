#vocabulary learning app that changes words in a text into their translation
import nltk
import random

#test EN to NL

amount = 1 #amount of translation to be used



input = """
A man in health, who is both vigorous and his own master, should be under no obligatory rules, and have no need, either for a medical attendant, or for a rubber and anointer.​1 His kind of life should afford him variety; he should be now in the country, now in town, and more often about the farm; he should sail, hunt, rest sometimes, but more often take exercise; for whilst inaction​2 weakens the body, work strengthens it; the former brings on premature old age, the latter prolongs youth.

2 [Legamen ad versionem Latinam]It is well also at times to go to the bath, at times to make use of cold waters;​3 to undergo sometimes inunction, sometimes to neglect that same; to avoid no kind of food in common use; to attend at times a banquet, at times to hold aloof; to eat more than sufficient at one time, at another no more; to take food twice rather than once a day, and always as much as one wants provided one digests it. 3 [Legamen ad versionem Latinam]But whilst exercise and food of this sort are necessities, those of the athletes are redundant; for in the one class any break in the routine of exercise, owing to necessities of civil life, affects the body injuriously, and in the other, bodies thus fed up in their fashion age very quickly and become infirm.4

4 [Legamen ad versionem Latinam]Concubitus indeed is neither to be desired overmuch, nor overmuch to be feared; seldom used it  p45 braces the body, used frequently it relaxes. Since, however, nature and not number should be the standard of frequency, regard being had to age and constitution, concubitusº can be recognized as harmless when followed neither by languor nor by pain. The use is worse in the day-time, and safer by night; but care should be taken that by day it be not immediately followed by a meal, and at night not immediately followed by work and watching. Such are the precautions to be observed by the strong, and they should take care that whilst in health their defences against ill-health are not used up.
"""

rules = {
	"and":"en",
	"or":"of",
	"man":"mensen"
}


result = """
<html>
<body style="margin:10px;">
"""

tokens = nltk.word_tokenize(input)

for t in tokens:
	if t in rules.keys():
		result+="""<span style="background-color:powderblue;">"""+rules[t]+"</span>"
	else:
		result+=" "+t

result+="</body></html>"

filename = "".join([random.choice("1234567890") for i in range(16)])+".html"
with open(filename, 'w', encoding="utf-8") as f:
	f.write(result)