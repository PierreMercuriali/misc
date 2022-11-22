from PIL import Image

colors = [u'⬛',
          u'🟧',
          u'🟥',
          u'🟦',
          u'🟫',
          u'🟪',
          u'⬜',
          u'🟨',
          u'🟩'
          ]

#black, orange, red, blue, brown, violet, white, yellow, green

rule = {
    '000':'1',
    '001':'0',
    '010':'1',
    '011':'1',
    '100':'0',
    '101':'1',
    '110':'1',
    '111':'0'
}


def pprint(d):
    r = ''
    for e in d:
        if e=='0':
            r+='⬛'
        else:
            r+='⬜'
    print(r)

m = 50

first = '000000000010000000000'*2

output = Image.new(size = (m, len(first)), mode='RGB')
l = len(first)
for i in range(m):
    #save line to image
    pprint(first)
    for j in range(l):
        if first[j]=='0':
            output.putpixel((i,j), (0,0,1))
        else:
            output.putpixel((i,j), (1,0,0))
    #update
    new = ''
    for j in range(l):
        slic = first[(j-1)%l]+first[(j)%l]+first[(j+1)%l]
        new+= rule[slic]
    first = new
output.save("test.png")

