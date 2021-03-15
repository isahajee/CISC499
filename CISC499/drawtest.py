import drawSvg as draw

d = draw.Drawing(100, 100, origin='center', displayInline=False)


# Draw an irregular polygon


d.append(draw.Rectangle(0,0,10,10,stroke_width=1,stroke='black',fill='none'))
d.append(draw.Rectangle(0,0,50,50,stroke_width=1,stroke='red',fill='none'))
##d.append(draw.Rectangle(
d.saveSvg('test.svg')
