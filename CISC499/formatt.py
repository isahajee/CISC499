
from svgpathtools import svg2paths

import os.path
from os import path
import sys


## THIS DOES ALL THE PREPROCESSING FOR THE CONSTRUCTOR,
## REMOVES TOP AND BOTTOM (NOT NEEDED) AND CREATES THE PATH SVG FILES FOR CONSTRUCTION


def format_svg(svg_location):
    ## from makercase, every 3rd path is a top/bottom. ONLY WORKS FOR MAKERCASE NOW
    ## WILL MAKE MORE RIGOROUS
    ## find the 2 different sides and label them in a triple
    ## ONLY NEED SIDES, ignore top/bottom

    ## returns the list of path objects and the dimensions
    
    
    if path.exists(svg_location):
        ##print('yes') 
        paths, attributes = svg2paths(svg_location)

        ## [0] = paths, not entirely sure what the other attrs do but im sure its something

    elif not svg_location.endswith('.svg'):
        sys.exit("invalid filename or extension")

   ## print(paths)


    side_dims=[]
    side_paths=[]
    for p in paths:


        ## top or bottom, dont count
        if p==paths[2] or p==paths[5]:
           ## print('caught')
            continue

        xmin, xmax, ymin, ymax = p.bbox()
        width = round((xmax - xmin),3)
        height = round((ymax - ymin),3)
        dim_t = (round(cm2px(width),0),round(cm2px(height),0))

        ##print('yuh')
        side_dims.append(dim_t)
        side_paths.append(p)
        

    ##print(side_dims)

    ratio = get_side_ratio(side_dims[0])
    thickness = get_mat_thickness(side_dims)
    ## all sides should be identical, only need 1

    ##print(outp)
    return (side_dims,thickness)

      


## ratio of large side to small side, can be used to infer sidelengths later on

## multiply any arbitrary length to get a scaled rectangle
def get_side_ratio(dim):
     ## rectangular
    ratio = dim[1]/dim[0]

    
    return ratio

def get_mat_thickness(dims):
    # thickness = dims[
    x1,y1 = dims[0]
    x2,y2 = dims[1]

    interx = x1-x2
    intery = y1-y2

    
    thicknessx = interx/2
    ##print(thicknessx)
    thicknessy = intery/2

   
    return round(thicknessx,3)


def cm2px(cm):
    px = cm*38
    return px

## input sidelengths as cm, thickness could probably be omitted, this will be how toothed boxes will be handled
## for now...



def input_2_sides(length,width,height,thickness):
    '''
    takes user input (from flask) and creates an equivalent sides array


    sides needed: 2 of size l x h
                  2 of size w x h
                  ** dont need l x w side since the bottom/top isnt needed
    '''
    l = cm2px(length)
    w = cm2px(width)
    h = cm2px(height)

    ## subtract 2*thickness from a side (doesnt matter which) because it needs the ability to lock the sides together
    ## one sides need to overlap by 1*thickness for each side (therefore 2*thickness)
    
    s1 = (l-(thickness),h)
    s2 = (w,h)
    
    side_dims= []

    side_dims.append(s2)
    side_dims.append(s2)
    side_dims.append(s1)
    side_dims.append(s1)

    out = [side_dims,thickness]
        
    return out

        
        

        

        
    
    
    
