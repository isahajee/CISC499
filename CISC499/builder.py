import drawSvg as draw
import math
from svgpathtools import Path,parse_path, svg2paths


## ratio likely not needed/ needs to be changed



## sides are passed in pixel lengths



    

def build(sides,thickness):

    print(sides)

    thickness = 5

    '''
    sides: the sidelengths from input, used to preserve sidelength ratios,

    '''
    ## svg shouldnt be too big for efficiencys sake
    ## only needs to be cx+ 2*flaplength(=cx*0.15) ...
    
    
    cy = sides[0][1]
    cx = sides[0][0]

    flap = (round(0.15*(cx/4),4))
    ## canvas object,
    '''
    cx+flap because it shouldnt be huge, canvas is only as large as it needs to be+ 30 px for margin
    '''
    ##print(cx+(2*flap)+30)
    ##print(cy+(2*flap)+30)
    d= draw.Drawing(700,700,
                    origin='center',
                    displayInline=False)

    maxX = 600/2
    maxY = 600/2
    linex =  -flap 
    xval = -maxX + flap + 15 ## 30 is margin..

    initPos = xval - linex
    initNeg= xval +linex
    inter_pts=[]


    d.append(draw.Line(initNeg,-flap,initNeg, cy/4+(2*flap),stroke='black'))

    finalPos = xval - linex
    finalNeg = xval +linex

    animIter = 1

    tooth_coords=[]
    for s in sides:
        

        
        ## ratio * any width = the same rectangle proportionally
        ##ratio = get_side_ratio(s)

       #3 s = (384,649)
       ## print(s)
        w,h = s
        w = w/4
        h = h/4

        ## xval, 0 = BOTTOM LEFT CORNER OF RECT
        ## draw 4 main recs, use as a guide for building
        '''
        d.append(draw.Rectangle(xval,
                       0,
                       w,
                       h,
                       stroke_width=1,
                       stroke='white',
                       fill='red'))
        '''

        ## add top-notches (NOT FLESHED OUT, only placeholders)

        ## bottom triangles
        d.append(draw.Line(xval,0,initPos, -flap,stroke='black'))
        d.append(draw.Line(xval,0,initNeg, -flap,stroke='black'))



        ## add tooth above triangle

        d.append(draw.Line(xval-(0.5*thickness),h, xval-(0.5*thickness),h+flap*2,stroke = 'black'))
        d.append(draw.Line(xval+(0.5*thickness),h, xval+(0.5*thickness),h+flap*2,stroke = 'black'))

        ## connect bottom triangles
        ##d.append(draw.Line(initPos,-flap,init, cy/4+(2*flap),stroke='black'))
        d.append(draw.Line(initPos,-flap,initPos+w-(flap*2), -flap,stroke='black'))

        xval+= w
        initPos += w
        initNeg += w

        ##print(xval)

        d.saveSvg('anim'+str(animIter)+'.svg')
    
        animIter+=1
        ##d.append(draw.Line(initPos,-flap,initPos+w-(flap), -flap,stroke='black'))
    
    
    ## add far left flap


    topLeft = cy/4+(2*flap)

    ##xvalOrig = -maxX + flap + 15 
    d.append(draw.Line(initPos-(flap*2),
                       -flap,
                       initPos-(flap*2)+flap,
                       0,stroke='black'))

    ## connect FL flap to top
    d.append(draw.Line(initPos-(flap*2)+flap,
                       0,
                       initNeg+flap,
                       cy/4+(2*flap),stroke='black'))

    ## TOP LINE, need to break up into peices

    d.append(draw.Line(finalNeg,topLeft,initNeg+flap,topLeft,stroke='black'))
    
    d.saveSvg('ex.svg')



## size as a percent of surface
##def get_flap_size(size):


def get_side_ratio(dim):
     ## rectangular
    ratio = dim[1]/dim[0]
    return ratio


## give it the x,y of the bottom of the teeth lines that were drawn, it will give the dimensions to draw at
def build_tooth(x1,x2, mirror):
    line1=[(9.06,17.27),(14.16,13.65)]
    line2 =[(14.16)]


##build([(384.0, 649.0), (361.0, 649.0), (384.0, 649.0), (361.0, 649.0)], 1.6901041666666667, 11.5)
