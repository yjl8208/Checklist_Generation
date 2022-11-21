"""
Read mapping csv to hashmap
"""
import collections
import numpy as np

mapDict = {}

def readMap(path, col:set):

#  """ # TODO: Define functions to loop through all facade materials"""
    with open(path, encoding = 'utf-8') as f:
        file = np.loadtxt(path, delimiter = ",", dtype = str, usecols = col, unpack = True)
#     print(file)
    [comp, defect] = file
    maps = collections.defaultdict(list)
    #-->Add rank for defect
    for i in range (1, len(comp)):
        maps[comp[i]].append(defect[i])
    return maps

"""
Set up the list of facade materials 
"""
facadeMaterials = ['Brick_masonry', 'Concrete', 'Stone_limestone', 'Metal_and_glass', 'Glass']

for material in facadeMaterials:
    #path: lab desktop: "C:/Users/zs1110/OneDrive - nyu.edu/Report analysis/mapping_result/%s_pair_frequency.csv" % (material)
    #path: my PC: "C:/Users/59896/OneDrive - nyu.edu/Report analysis/mapping_result/%s_pair_frequency.csv" % (material)
    path = "/Users/joryashi/OneDrive - nyu.edu/RQ1/mapping_result/%s_pair.csv" % (material)
#     material+ '_Map' = readMap(path, (0, 1))
    locals()[material + '_Map'] = readMap(path, (0, 1))
    mapDict[material] = locals()[material + '_Map'] 

#TODO: Add function to allow user define mapping for new material/component
