#This is intended to accompany my math paper.

def rcmcn(cyclesize1, cyclesize2 = 'default'):
    """R(Cm,Cn) takes two cycle sizes and calculates their ramsey number"""
    if cyclesize2 == 'default':
        cyclesize2 = cyclesize1
        
    mincycle = min(cyclesize1, cyclesize2)
    maxcycle = max(cyclesize1, cyclesize2)

    if mincycle < 3:
        print('rcmcn error: small cycle less than 3')
        return(-1)

    if maxcycle in(3,4) and mincycle == maxcycle:
        return(6)

    if mincycle % 2 == 1:   #mincycle is odd 
        return(2 * maxcycle - 1)
    else:                   #mincycle is even
        optiona = maxcycle + mincycle / 2

    if maxcycle % 2 == 0:   #maxcycle is even
        return(optiona - 1)
    else:                   #maxcylce is odd
        return(max(optiona, 2 * mincycle) - 1)  #Yes, supposed to be mincycle.

    
def rtlb2(graphdata):
    """ramsey trivial lower bound from listed [[graph order, parity]...]"""
    """enter 2, 2-tuples with size and parity of graph as isgraphbipartite"""
#To work on arbitrary graphs, I need the order of their bipartites parts.
#input: [[graph1 bipartite1, g1b2],[g2b1,g2b2]]
    #when a graph isn't bipartite, just enter its [total]
    graphpair = graphdata[:] #this isn't deep enough to affect the graph rows
        
    if len(graphpair) == 1:
        graphpair.append(graphpair[0])


'''this is the version where I just use parity of the tadpole's cycle
    for x in range(2):
        length = len(graphpair[x])
        if length != 2:
            return('graph',x,'has',length,'but needs length 2 (order, parity)')
'''
#as silly as this is, I should turn the graphpair list into a cycle,
#to make the code simpler
    options = []
    if graphpair[0][1] == 1:
        options.append(
      
    return(graphpair)
"""
    minorder = min(graph1data[0], graph2data[0])
    maxorder = max(graph1data[0], graph2data[0])
    
    if minorder < 3:
        print('rcmcn error: small order less than 3')
        return(-1)
"""
# CHECK FOR INTEGER INPUTS (REPRESENTING orders)

    
""" DOUBT THIS APPLIES TO NON-TRIVIAL TADPOLES
    if maxorder in(3,4) and minorder == maxorder:
        return(6)
"""
# FIRST DETERMINE VALID ARRANGEMENTS, BASED ON PARITY
# THEN DETERMINE WHICH GIVES HIGHEST VALUE
"""
    if minorder % 2 == 1:   #minorder is odd 
        return(2 * maxorder - 1)
    else:                   #minorder is even
        optiona = maxorder + minorder / 2

    if maxorder % 2 == 0:   #maxorder is even
        return(optiona - 1)
    else:                   #maxcylce is odd
        return(max(optiona, 2 * minorder) - 1)  #Yes, supposed to be minorder.

    return(None)
"""


    
