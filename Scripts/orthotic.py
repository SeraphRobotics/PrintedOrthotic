from manipulations import *

#############################################

hardOffset = [0,0,5]
mediumOffset = [0,0,3]
softOffset = [0,-40,20]

hardID = 3
mediumID = 1
softID = 2

clearance=10
clearanceSpeed=10

manips={}
manips[hardID] = hardOffset
manips[mediumID] = mediumOffset
manips[softID] = softOffset

def process(fabTree):
    fabTree = sortIntoLayers(fabTree)
    #TRANSLATE
    for id in manips.keys();
        t = manips[id]
        fabTree = translate(fabTree,t[0],t[1],t[2],id)
    fabTree = setClearance(fabTree,clearance, clearanceSpeed)
    fabTree = parity(fabTree)
    return fabTree
    
    
    
if __name__ == '__main__':
    import sys
    todo = sys.argv[1]
    
    fabTree = ElementTree(file = sys.argv[2])
    for el in fabTree.iter(): el.tag = el.tag.lower()
    
    process(fabTree)
    writeTree(sys.argv[2],fabTree)
    
    
    