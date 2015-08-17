"""

Code to help with making nice looking plots

Nick Gravish

"""




def expand_colormap(cgen, N):
    """
    Takes in a colormap spec, a list of RGB tuples, and 
    interpolates it to N points
    """
    R = [x[0] for x in cgen]
    G = [x[1] for x in cgen]
    B = [x[2] for x in cgen]
    
    R = np.interp(np.linspace(0,6,N), np.arange(0,6), R)
    G = np.interp(np.linspace(0,6,N), np.arange(0,6), G)
    B = np.interp(np.linspace(0,6,N), np.arange(0,6), B)
    
#     cgen = (R, G, B, Alpha)
    cgen = [(R, G, B, 1) for R,G,B in np.nditer([R,G,B])]
            
    return cgen