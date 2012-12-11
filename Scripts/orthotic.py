from manipulations import *

#############################################

hardOffset = [0,0,0]
mediumOffset = [0,0,3]
softOffset = [0,0,20]



hardID = 1
mediumID = 2
softID = 3

padTranslate = [0,-40,0]
padID = softID

clearance=10
clearanceSpeed=10

manips={}
manips[hardID] = hardOffset
manips[mediumID] = mediumOffset
manips[softID] = softOffset

def process(fabTree):
    fabTree = sortIntoLayers(fabTree)
    #TRANSLATE
    for id in manips.keys():
        t = manips[id]
        fabTree = translate(fabTree,t[0],t[1],t[2],id)
        
    fabTree = parity(fabTree)
    fabTree = translate(fabTree,padTranslate[0],padTranslate[1],padTranslate[2],padID)
    fabTree = setClearance(fabTree,clearance, clearanceSpeed)
       
    return fabTree
    
    
    
if __name__ == '__main__':
    import sys
    
    fabTree = ElementTree(file = sys.argv[1])
    for el in fabTree.iter(): el.tag = el.tag.lower()
    
    process(fabTree)
    
    if len(sys.argv)>2: writeTree(sys.argv[2],fabTree)
    else: writeTree(sys.argv[1],fabTree)
    
    
    