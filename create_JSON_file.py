import json

ref_code_dict = {
    '1968 Building Code' : {
        'Railing' : {'height' : 42, 'space': 3 },
        'Balcony' : {'height' : 42},
        'Parapet' : {'height' : 42}
    },

    '2008 Building Code' : {
        'Railing' : {'height' : 42, 'space': 3 },
        'Balcony' : {'height' : 42},
        'Parapet' : {'height' : 42},
    },

    '2014 Construction Code' : {
        'Railing' : {'height' : 42, 'space': 3},
        'Balcony' : {'height' : 42},
        'Parapet' : {'height' : 42}
    }
}
with open("construction_code_compliance.json", 'w') as outfile:
    json.dump(ref_code_dict, outfile)

facade_defect_dict = {
    'brick masonry' : {
        'material loss' : ['crazing', 'crack', 'spall', 'erosion', 'peeling', 'hole', 
        'missing', 'repair failure','seperation of brick masonry-outer wythe', 'hollow', 'loose', 'fasterner failed', 'lath failed', 'checking'],
        'deformation' : ['bowing', 'bulging', 'rolling block', 'displacement'],
        'surface color/texture change' : ['leackage', 'soiling', 'lime run', 'efflorescence']
    },

    'stone' : {
        'material loss' : ['crack', 'gypsum crust', 'erosion', 'peeling', 'repair failure', 'missing', 
        'coating failure', 'surface decay', 'hole', 'spall', 'hollow', 'loose'],
        'deformation' : ['bulging', 'bowing', 'displacement', 'leaning'],
        'surface color/texture change' : ['leakage', 'soiling']
    },

    'concrete' : {
        'material loss' : ['crack', 'corrosion', 'delamination', 'scaling', 'honeycomb', 'coating failure', 
        'missing', 'repair failure', 'spall', 'opening', 'expansion joint', 'broken', 'hollow', 'loose'],
        'deformation' : ['slippage', 'displacement', 'bowing', 'leaning'],
        'surface color/texture change' : ['leakage', 'soiling']
    }
}
with open("facade_based_defects.json", 'w') as outfile1:
    json.dump(facade_defect_dict, outfile1)

comp_defect_dict = {
    'terra cotta' : {
        'material loss' : ['loss of glaze', 'chipping', 'spall', 'crack', 'crazing', 'hollow'
        'missing', 'broken', 'coating failed', 'repair failure', 'hole', 'expansion joint', 'loose'],
        'deformation' : ['bowing', 'bulging', 'leaning', 'displacement'],
        'surface color/texture change' : ['leackage', 'soiling']
    },

    'metal' : {
        'material loss' : ['crack', 'connection failed', 'depression', 'repair failure', 'missing','spall', 
        'hole', 'coating failure', 'corrosion', 'loose'],
        'deformation' : ['bulging', 'bowing', 'displacement', 'leaning'],
        'surface color/texture change' : ['leakage', 'soiling']
    },

    'brownstone' : {
        'material loss' : ['disaggregation', 'exfoliation', 'scaling', 'sagging', 'coating failed']
    },    

    'glass' : {
        'material loss' : ['crack', 'missing', 'repair failure', 'putty failed', 'loose'],
        'deformation' : ['bulging'],
        'surface color/texture change' : ['soiling']
    }     
}
with open("component_based_defects.json", 'w') as outfile2:
    json.dump(comp_defect_dict, outfile2)