from ctypes.util import find_library

import pandas as pd

find_library('geos_c')
from building import *
from facade import *
from facade_component import *
from floor import *
# from exterior_vertical_enclosure import *


from geometry_representation import *
from ref_con_code_enum import *
from direction_enum import *
# temp disabled due to error # from read_mapping import *
import numpy as np
import re
from facade_section import *
import json
# import inspect
import pyclbr
import os

from all_class_declaration import *
from enum import *

###imp! exec() does not run in def. must run as raw script
###rebranched from test_place_modified(11.14.22(2)).py, those further along the branch are to be deemed failed


columns_array = []
allfloors = []
allcolumns = []
floor_coordinates_array = []
columns_array = []

floors_or_columns = ""
number_of_columns = 1  # this is to prevent errors

metadata_array = {}
windows_array = {}
floors_array = {}
window_frame_array = {}
window_panel_array = {}

comparison_list = {}

currentcomponent = ""

#data_frame_columns = ["potential_defects", "components", "checked", "hierarchy", "floor/column",
#                      "level", "compType", "subcomps", "class"]




#data_frame_columns = ["potential_defects", "components", "checked", "hierarchy1", "hierarchy2", "hierarchy3","hierarchy4","floor/column",
#                      "level", "compType", "subcomps", "class"]

data_frame_columns = ["potential_defects", "components", "checked", "hierarchy1", "hierarchy2", "hierarchy3","hierarchy4","floor/column",
                      "level", "compType", "subcomps", "class", "compName"]

globals()['df'] = pd.DataFrame(columns=data_frame_columns)
globals()['defect_df'] = pd.read_csv('Defect matrix.csv')
globals()['hierarchy_df'] = pd.read_csv('Comprehensive lists_withEdits.csv')



def add_enum(component_script):
    print("error occured for component: " + component_script)
    add_new_enum = input(
        "your component does not seem to have an existing enum. would you like to add a new enum? [y/n]")

    if add_new_enum == 'y':
        enum_to_be_added = input(
            "input the enum name here, it is assumed that properties will be defined in test_bed")
        exec_str = enum_to_be_added + " = \"" + enum_to_be_added + "\""

        exec(exec_str, globals())
        enumDataset = open("facadeMaterialDataset.txt", "a")

        enumDataset.write("\n\n")
        enumDataset.write(exec_str)
        # at the end of "classDataset.txt, never leave an empty line!

        enumDataset.close()

    else:
        print("component", "'" + component_script + "'", "cannot be added.")



def add_defect():
    add_new_defect = input(
        "add_new_defect? [y/n]")

    if add_new_defect == 'y':
        lev_1 = input(
        "lev1?")
        lev_2 = input(
        "lev2?")
        defect = input(
        "defect")
        materials = input(
        "materials?")
        component = input(
        "component?")
        related = input(
        "related?")

        final_line = ','.join([lev_1, lev_2, defect, materials, component, related])

        defectDataset = open("Defect matrix.csv", "a")

        defectDataset.write("\n")
        defectDataset.write(final_line)
        # at the end of "classDataset.txt, never leave an empty line!

        defectDataset.close()

    else:
        return





def add_component(possible_component_types, component_script):
    print("error occured for component: " + component_script)

    add_new_class = input(
        "your component does not seem to have an existing class. would you like to add a new class? [y/n]")

    if add_new_class == 'y':
        class_to_be_added = input(
            "input the class name here")

        if class_to_be_added in possible_component_types:
            #if class is pre-existing, just replace first few attributes and
            #exec_str = class_to_be_added + " = " + component_script[component_script.find("("):]

            #print(exec_str)

            print("class already exists")

        else:
            exec_str = class_to_be_added + " = type(\"" + class_to_be_added + "\", (FacadeComponent, ), {\"__init__\": comp_init})"

            hierarchy_done = False

            hierarchy_list = []

            while not hierarchy_done:
                class_cache = class_to_be_added
                class_to_be_added = input(
                    "input hierarchies for new components, starting from highest level, and input done when done")
                if class_to_be_added == 'done':
                    hierarchy_done = True
                    class_to_be_added = class_cache
                    continue

                hierarchy_list.append(class_to_be_added)

            hierarchy_string = ','.join(hierarchy_list)

            hierarchyDataset = open("Comprehensive lists_withEdits.csv", "a")

            hierarchyDataset.write("\n" + hierarchy_string)
            # at the end of "classDataset.txt, never leave an empty line!

            hierarchyDataset.close()

        exec(exec_str, globals())

        classDataset = open("classDataset.txt", "a")

        classDataset.write("\n" + class_to_be_added)
        # at the end of "classDataset.txt, never leave an empty line!

        classDataset.close()



        possible_component_types.append(class_to_be_added)

        exec(component_script, globals())

        #return hierarchy_list


    else:
        print("component", "'" + component_script + "'", "cannot be added.")






def get_hierarchy(component, level):



    level_num = int(level[5])

    component_type = component
    for index in range(1, len(component)):
        if component[index].isupper():
            component_type = component[:index] + " " + component[index:].lower()



    hierarchy = globals()['hierarchy_df'][globals()['hierarchy_df'][level].str.contains(component_type, na=False)]
    hierarchy = hierarchy.iloc[0, 0:level_num]
    hierarchy = hierarchy.values.tolist()
    print(99012, len(hierarchy))
    if len(hierarchy) >= 4:
        pass
    else:
        while not len(hierarchy) == 4:
            hierarchy.append(0)




    return hierarchy



def get_defects_from_comp(components_list):
    directory = os.getcwd()
    # directory = '/Users/youngjun/Documents/GitHub/Checklist_Generation/'
    json_file_name = 'component_based_defects.json'
    folder_name = 'ChecklistImplementation'
    # temp_testbed_path = os.path.join(directory, folder_name)
    json_path = os.path.join(directory, json_file_name)

    with open(json_path) as json_file:
        defects_list = json.load(json_file)

    defectdict = {}


    for components in components_list:

        for defects_categories in list(defects_list[components].keys()):

            if defects_categories not in defectdict:
                defectdict[defects_categories] = []

            for defects in defects_list[components][defects_categories]:
                if defects not in defectdict[defects_categories]:
                    defectdict[defects_categories].append(defects)





    return defectdict



def get_all_possible_components():

    # edit component_module_file_list as needed

    # component_module_file_list = ['exterior_vertical_enclosure', 'superstructure', 'exterior_horizontal_enclosure']
    component_module_file_list = ['all_class_declaration']
    all_possible_components = []

    import importlib, inspect

    for file_name in component_module_file_list:
        for name, cls in inspect.getmembers(importlib.import_module(file_name), inspect.isclass):
            all_possible_components.append(name)

    all_possible_components.append("Floor")
    # Because floor class cannot be declared in all_class_declaration(due to having different attributes),
    # I must append "Floor" as a possible_component while not adding it to classDataset.txt

    return all_possible_components

#make a function such that:
#it receives the "allcomponents" dictionary

# -> and then, it adds an entry to the pandas for each
# component in each level

# -> it recurses until it reaches another dict, in which the process
# is repeated

# -> until it reaches no more lists

# in the pandas list, it adds the level of component, the variable floor, variable type, variable subcomps, etc using
# function attributes


def add_pandas(container, level, floor):
    if type(container) == list and container:
        for comp_dict in container:
            try:
                comp_var = globals()[list(comp_dict.keys())[0]]
                if comp_var.__class__.__name__ == 'Floor':
                    component_type = comp_var.__class__.__name__

                    hierarchy_list = get_hierarchy(component_type, "Level"+str(level))

                    globals()['df'].loc[len(globals()['df'].index)] = [None, None, 1,
                                                                       hierarchy_list[0], hierarchy_list[1], hierarchy_list[2], hierarchy_list[3],
                                                                       list(comp_dict.keys())[0], level, Floor, "None",
                                                                       component_type, "None"]
                    add_pandas(comp_dict, level + 1, list(comp_dict.keys())[0])
                else:
                    comp_list = []
                    for component in comp_var.materials:
                        comp_list.append(str(component)[18:])
                    component_type = comp_var.__class__.__name__

                    hierarchy_list = get_hierarchy(component_type, "Level" + str(level))

                    globals()['df'].loc[len(globals()['df'].index)] = [get_defects_from_comp(comp_list), comp_list, 1, hierarchy_list[0],
                                                                       hierarchy_list[1], hierarchy_list[2], hierarchy_list[3], floor, level, comp_var.compType, ",".join(comp_var.subComp),
                                                                       component_type, "None"]
                    add_pandas(comp_dict, level+1, floor)

            except AttributeError:
                comp_var = globals()[comp_dict]
                comp_list = []
                for component in comp_var.materials:
                    comp_list.append(str(component)[18:])
                component_type = comp_var.__class__.__name__

                hierarchy_list = get_hierarchy(component_type, "Level" + str(level))

                globals()['df'].loc[len(globals()['df'].index)] = [get_defects_from_comp(comp_list), comp_list, 1,
                                                                   hierarchy_list[0], hierarchy_list[1],
                                                                   hierarchy_list[2], hierarchy_list[3],

                                                                   floor, level, comp_var.compType, ",".join(comp_var.subComp),
                                                                   component_type, str(comp_dict)]

                globals()["max_levels"] = level




    elif type(container) == dict and container:
        #for array in container.values():
        #print(list(container.values()))
        add_pandas(list(container.values())[0], level, floor)




# initially, for floors/columns, floor and hierarchy are set to 0 because they have no such thing
def get_levels_of_components(initial_dict, level, floor, hierarchy):
    if not (('level_%s_components' % (level))) in globals():
        globals()['level_%s_components' % (level)] = []
    # print('level_%f_components' % (level))
    # print(90903)

    cache_floor = floor
    cache_hierarchy = hierarchy

    for subdict in initial_dict:
        try:
            if cache_floor == 0:
                cache_floor = list(subdict.keys())[0]

            if cache_hierarchy == 0:
                cache_hierarchy = list(subdict.keys())[0]

            else:
                cache_hierarchy += " " + list(subdict.keys())[0]
            globals()['%s_dict' % (list(subdict.keys())[0])] = {}
            globals()['%s_dict' % (list(subdict.keys())[0])]['%s_dict' % (list(subdict.keys())[0])] = [cache_floor,
                                                                                                       cache_hierarchy]
            globals()['level_%s_components' % (level)].append(globals()['%s_dict' % (list(subdict.keys())[0])])
            #print(list(subdict.keys()))

            #print(globals()['%s_dict' % (list(subdict.keys())[0])])

            get_levels_of_components(subdict[list(subdict.keys())[0]], level + 1, cache_floor, cache_hierarchy)

            cache_floor = floor
            cache_hierarchy = hierarchy



        except AttributeError:
            for components in initial_dict:
                cache_hierarchy = hierarchy
                cache_hierarchy += " " + components
                globals()['%s_dict' % (components)] = {}
                globals()['%s_dict' % (components)]['%s_dict' % (components)] = [floor, cache_hierarchy]
                globals()['level_%s_components' % (level)].append(globals()['%s_dict' % (components)])
                #print(globals()['%s_dict' % (components)])
                # globals()['level_%s_components' % (level)].append(components)

            globals()["max_levels"] = level
            return


def import_test_bed():
    # imports a .txt file from the folder of ChecklistImplementation,
    # and then returns it as variable "txt_file_itself"

    print("What is the file directory of the test_bed? Input the entire directory including txt file name.")

    testbed_path = input(
        "for example: /Users/youngjun/PycharmProjects/DjangoImplementation/ChecklistImplementation/test_bed_1.txt \n").strip()

    # directory = os.getcwd()
    # txt_file_name = 'test_bed_1.txt'
    # folder_name = 'ChecklistImplementation'
    # testbed_path = os.path.join(directory, txt_file_name)

    txt_separating_bounds = []
    txt_file_itself = []

    with open(testbed_path, "r") as dataskim:
        for line in dataskim:
            txt_file_itself.append(line)

    return txt_file_itself


# ^^^ source: https://stackoverflow.com/questions/7974849/how-can-i-make-one-python-file-run-another


def exec_each_row_as_python_code(txt_file_itself):
    # now, this function receives data from import_test_bed() and replace_slashes(), and uses
    # the python command of exec() to execute each row in "txt_file_itself" as raw python.
    possible_component_types = get_all_possible_components()

    component_types_and_their_count_dictionary = {}

    all_current_variables = list(globals())
    for i in txt_file_itself:
        # source: https://stackoverflow.com/questions/41100196/exec-not-working-inside-function-python3-x
        try:
            exec(i, globals())

        except NameError:

            class_name = i[(i.find("=")+1):i.find("(")].strip()
            error_resolved = False

            while not error_resolved:

                if class_name in possible_component_types:
                    add_enum(i)

                else:
                    add_component(possible_component_types, i)

                try:
                    exec(i, globals())
                    error_resolved = True
                except NameError:
                    continue

    all_current_variables_2 = list(globals())
    # print(all_current_variables_2)

    newly_declared_variables = [e for e in all_current_variables_2 if e not in all_current_variables]

    for possible_component in possible_component_types:
        globals()['%s_list' % (possible_component)] = []
        for i in newly_declared_variables:
            try:
                globals()[i].comPlane
                if globals()[i].__class__.__name__ == possible_component:
                    globals()['%s_list' % (possible_component)].append(i)
            except AttributeError:
                continue

        component_types_and_their_count_dictionary[possible_component] = globals()[
            '%s_list' % (possible_component)]

        # source ^^: https://stackoverflow.com/questions/5008828/convert-a-python-type-object-to-a-string

    component_types_and_their_count_dictionary = {k: v for k, v in component_types_and_their_count_dictionary.items() if
                                                  v}

    # ^^^ source: https://stackoverflow.com/questions/14813396/python-an-elegant-way-to-delete-empty-lists-from-python-dictionary


    # core assumptions:
    # 1. all component names start from 0
    # 2. all floors/columns start from 1
    # 3. all component names, if there are "n" of them, will be populated from 0 ~ (n-1)

    return component_types_and_their_count_dictionary
    # source: https://stackoverflow.com/questions/59806654/delete-matching-elements-in-two-arrays-python


# ^^^ source: https://stackoverflow.com/questions/6181935/how-do-you-create-different-variable-names-while-in-a-loop
#           https://python.plainenglish.io/how-to-dynamically-declare-variables-inside-a-loop-in-python-21e6880aaf8a


# modify sort_all so that each work package only receives one unique iteration of a component type

def sort_all(component_types_and_their_count_dictionary):
    # first, sort by subcomponents.
    # all subcomponents of any component including windows, will be removed in lieu of
    # the subcomponent attribute of the component

    for h in component_types_and_their_count_dictionary:
        for q in component_types_and_their_count_dictionary[h]:
            globals()['%s_contains' % (q)] = {}
            globals()['%s_contains' % (q)][q] = []

    for component_types in component_types_and_their_count_dictionary:
        for component in component_types_and_their_count_dictionary[component_types]:
            try:
                subcomps_array = globals()['%s' % (component)].subComp

                for subcomps in subcomps_array:
                    for component_types in component_types_and_their_count_dictionary:
                        for component1 in component_types_and_their_count_dictionary[component_types]:
                            if subcomps == component1:
                                component_types_and_their_count_dictionary[component_types].remove(subcomps)
                                globals()['%s_contains' % (component)][component].append(subcomps)
            except AttributeError:
                continue

    for k in component_types_and_their_count_dictionary:
        for t in component_types_and_their_count_dictionary[k]:


            for p in component_types_and_their_count_dictionary:
                for n in component_types_and_their_count_dictionary[p]:
                    if globals()[t].comPlane == globals()[n].comPlane:
                        # can substitute with "if t ==n" if there aren't any components with duplicate comPlanes
                        continue
                    else:
                        if isinstance(globals()[t].comPlane[0], tuple) and isinstance(globals()[n].comPlane[0], tuple):
                            if Polygon(globals()[t].comPlane).overlaps(Polygon(globals()[n].comPlane)) and Polygon(
                                    globals()[n].comPlane).area < Polygon(globals()[t].comPlane).area and type(
                                globals()[n]) != type(globals()[t]):
                                globals()['%s_contains' % (t)][t].append(globals()['%s_contains' % (n)])
                        elif not isinstance(globals()[t].comPlane[0], tuple) and isinstance(globals()[n].comPlane[0],
                                                                                            tuple):
                            if Polygon(globals()[t].comPlane[0]).overlaps(Polygon(globals()[n].comPlane)) and Polygon(
                                    globals()[n].comPlane).area < Polygon(globals()[t].comPlane[0]).area and type(
                                globals()[n]) != type(globals()[t]):
                                globals()['%s_contains' % (t)][t].append(globals()['%s_contains' % (n)])
                        elif isinstance(globals()[t].comPlane[0], tuple) and not isinstance(globals()[n].comPlane[0],
                                                                                            tuple) and type(
                            globals()[n]) != type(globals()[t]):
                            if Polygon(globals()[t].comPlane).overlaps(Polygon(globals()[n].comPlane[0])) and Polygon(
                                    globals()[n].comPlane[0]).area < Polygon(globals()[t].comPlane).area:
                                globals()['%s_contains' % (t)][t].append(globals()['%s_contains' % (n)])
                        else:
                            if Polygon(globals()[t].comPlane[0]).overlaps(
                                    Polygon(globals()[n].comPlane[0])) and Polygon(
                                globals()[n].comPlane[0]).area < Polygon(globals()[t].comPlane[0]).area and type(
                                globals()[n]) != type(globals()[t]):
                                globals()['%s_contains' % (t)][t].append(globals()['%s_contains' % (n)])

            # if components of a lower degree overlap with each other, this may lead to potential error.
            # Should we assume the user will always input correctly, and how should it be handled?
            # if say a small balcony and a large window overlapped,
            # how can we prevent the array window_n_contains from containing the balcony?

            # code is made like this because window_frame types have multiple coordinates, while
            # other types of components have only one set of coordinates

            ########change so interchangable with columns
            if isinstance(globals()[t], Floor):
                allfloors.append(globals()['%s_contains' % (t)])

    # get_unique_instances(allfloors)

    return allfloors


# def get_unique_instances(allfloors):
#    print(allfloors)


def setup_columns(columns_number):
    ###side step: setup for columns
    ###modification of Zhouya's method from geometry_representation.py

    number_of_columns = columns_number
    # this can be changed later! preferably by the user via a method, but it is not implemented yet.

    global columns_array
    columns_array = []

    # columns_array = facadePlane.seperatePlane(int(number_of_columns))

    y0 = facadePlane.getPolyCoord()[0][1]
    y1 = facadePlane.getPolyCoord()[1][1]
    columns_array = []
    inspectionRange = (facadePlane.getPolyCoord()[2][0] - facadePlane.getPolyCoord()[0][0]) / number_of_columns
    for i in range(0, number_of_columns):
        x0 = i * inspectionRange
        x1 = (i + 1) * inspectionRange
        # point1 = (x0, y0)
        # point2 = (x0, y1)
        # point3 = (x1, y1)
        # point4 = (x1, y0)
        # globals()['column' + str(i+1)] = Polygon([point1, point2, point3, point4])
        globals()['column_' + str(i + 1)] = Floor(y1, inspectionRange, (x0, 0.00), (i + 1))
        columns_array.append('column_' + str(i + 1))

    return columns_array






def main():
    add_defect()


    txt_file_itself = import_test_bed()

    component_types_and_their_count_dictionary = exec_each_row_as_python_code(txt_file_itself)

    floors_or_columns = input('floors_or_columns? [floors/columns]: ')
    min_x = int(facadePlane.polyCoord[0][0])
    max_x = int(facadePlane.polyCoord[2][0])
    xlength = max_x - min_x
    print(xlength)

    if floors_or_columns == "columns":
        if xlength <= 60:
            number_of_columns = 1
            component_types_and_their_count_dictionary['Column'] = setup_columns(int(number_of_columns))
        else:
            if (xlength / 60) != (xlength // 60):
                minimum_number_of_columns = (xlength // 60) + 1
            else:
                minimum_number_of_columns = (xlength / 60)
            number_of_columns = input(f"how many columns? [input a positive integer above {minimum_number_of_columns}]: ")
            while not number_of_columns.isdigit() or not int(number_of_columns) >= minimum_number_of_columns:
                number_of_columns = input(f"how many columns? [Please input a positive integer above {minimum_number_of_columns}!]: ")

            component_types_and_their_count_dictionary['Column'] = setup_columns(int(number_of_columns))

        del component_types_and_their_count_dictionary['Floor']











        allcolumns = sort_all(component_types_and_their_count_dictionary)

        add_pandas(allcolumns, 2, 0)











        #no_dupe_df = globals()['df'].drop_duplicates(subset=['floor/column', 'subcomps', 'class'])

        globals()['df'].to_csv('out4.csv')



        ###core assumption for a certain Window object (or any other object for that matter):
        ### no two objects will have the same subcomponent list.


        ##reference: https://www.statology.org/pandas-combine-rows-with-same-column-value/
        ###https://stackoverflow.com/questions/27298178/concatenate-strings-from-several-rows-using-pandas-groupby
        agg_functions = {"potential_defects": 'first', "components": 'first', "checked": 'first', "hierarchy1": 'first', "hierarchy2": 'first', "hierarchy3": 'first',"hierarchy4": 'first',"floor/column" : list,
                      "level" : 'first', "compType" : 'first', "subcomps" : 'first', "class" : 'first', "compName" : 'first'}

        df_new = globals()['df'].groupby(['subcomps', 'class', 'compName']).aggregate(agg_functions)

        df_new['liststring'] = [','.join(set(sorted(map(str, l)))) + "," for l in df_new['floor/column']]
        #because list is unhashable in pandas, turn the sorted list into a str for comparison


        #https://stackoverflow.com/questions/45306988/column-of-lists-convert-list-to-string-as-a-new-column
        #https://stackoverflow.com/questions/33198916/getting-attribute-error-map-object-has-no-attribute-sort


        #df_new.to_csv('out3.csv')

        #no_dupe_df = globals()['df'].drop_duplicates(subset=['floor/column', 'class'])

        print(df_new)

        #no_dupe_df = df_new.groupby(['liststring', 'class']).first()
        #https://www.geeksforgeeks.org/delete-duplicates-in-a-pandas-dataframe-based-on-two-columns/


        no_dupe_df = df_new.drop_duplicates(subset=['liststring', 'class'], keep='last')





        print(no_dupe_df)

        # no_dupe_df.to_csv('out.csv')
        # newdf1.to_csv('out.csv')
        # print("check folder")

        no_dupe_df.to_csv('out2.csv')

        select_by_columns = input('select by columns? [y/n]: ')
        if select_by_columns == 'y':

            cache_original_df = no_dupe_df

            no_dupe_df = pd.DataFrame(columns=data_frame_columns)

            selected_columns_array = []

            select_by_columns = input('which columns to be selected? enter until enter "done" ')
            while select_by_columns != 'done':
                if select_by_columns.isdigit():
                    selected_columns_array.append(select_by_columns)
                select_by_columns = input('which columns to be selected? enter until enter "done" ')



            new_list = []
            for num in range(int(number_of_columns) + 1):
                if num in selected_columns_array:
                    if num not in new_list:
                        new_list.append(num)


            select_by_columns = new_list



            ####add part to get only selected floors

            for column in selected_columns_array:
                # print(cache_original_df[cache_original_df['floor/column'] == ("floor_" + str(floor))])

                #no_dupe_df = pd.concat(
                #    [no_dupe_df, cache_original_df[cache_original_df['floor/column'] == (str(column))]])

                no_dupe_df = pd.concat([no_dupe_df, cache_original_df[cache_original_df['liststring'].str.contains(f"column_{str(column)},")]])
            no_dupe_df = no_dupe_df.drop_duplicates(subset=['liststring', 'class'], keep='last')

        ########start changing


    elif floors_or_columns == "floors":

        allfloors = sort_all(component_types_and_their_count_dictionary)

        add_pandas(allfloors, 2, 0)

        agg_functions = {"potential_defects": 'first', "components": 'first', "checked": 'first', "hierarchy1": 'first',
                         "hierarchy2": 'first', "hierarchy3": 'first', "hierarchy4": 'first', "floor/column": list,
                         "level": 'first', "compType": 'first', "subcomps": 'first', "class": 'first',
                         "compName": 'first'}

        df_new = globals()['df'].groupby(['subcomps', 'class', 'compName']).aggregate(agg_functions)

        df_new['liststring'] = [','.join(set(sorted(map(str, l)))) + "," for l in df_new['floor/column']]
        # because list is unhashable in pandas, turn the sorted list into a str for comparison

        # https://stackoverflow.com/questions/45306988/column-of-lists-convert-list-to-string-as-a-new-column
        # https://stackoverflow.com/questions/33198916/getting-attribute-error-map-object-has-no-attribute-sort

        # df_new.to_csv('out3.csv')

        # no_dupe_df = globals()['df'].drop_duplicates(subset=['floor/column', 'class'])

        print(df_new)

        # no_dupe_df = df_new.groupby(['liststring', 'class']).first()
        # https://www.geeksforgeeks.org/delete-duplicates-in-a-pandas-dataframe-based-on-two-columns/

        no_dupe_df = df_new.drop_duplicates(subset=['liststring', 'class'], keep='last')

        print(no_dupe_df)

        select_by_floors = input('select by floors? [y/n]: ')
        if select_by_floors == 'y':

            cache_original_df = no_dupe_df

            no_dupe_df = pd.DataFrame(columns=data_frame_columns)

            selected_floors_array = []

            select_by_floors = input('which floors to be selected? enter until enter "done" ')
            while select_by_floors != 'done':
                if select_by_floors.isdigit():

                    selected_floors_array.append(int(select_by_floors))

                select_by_floors = input('which floors to be selected? enter until enter "done" ')

            #print(selected_floors_array)


            max_floor_in_list = max(selected_floors_array)





            new_list = []
            for num in range(max_floor_in_list + 1):
                if num in selected_floors_array:
                    if num not in new_list:
                        new_list.append(num)

            select_by_columns = new_list

            #print(select_by_columns)

            ####add part to get only selected floors


            for floor in selected_floors_array:

                #print(cache_original_df[cache_original_df['floor/column'] == ("floor_" + str(floor))])

                no_dupe_df = pd.concat([no_dupe_df, cache_original_df[cache_original_df['liststring'].str.contains(f"floor_{str(floor)},")]])

                #temp_array = cache_original_df[cache_original_df['floor/column'].str.contains(str(floor))==True]

                #print(temp_array)

                #no_dupe_df  = pd.concat([no_dupe_df, temp_array])

            no_dupe_df = no_dupe_df.drop_duplicates(subset=['liststring', 'class'], keep='last')





            #get_levels_of_components(allfloors, 1, 0, 0)
            # remove dupes using a for loop and max_levels later


        elif select_by_floors == 'n':

            #get_levels_of_components(allfloors, 1, 0, 0)
            pass




















    #mainarray = defects_list

    ###source: https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html

    #print(no_dupe_df)



    user_levels = int(input("how many levels into component hierarchy? max level is " + str(globals()["max_levels"])))

    cache_original_df = no_dupe_df

    no_dupe_df = pd.DataFrame(columns=data_frame_columns)

    #floor starts at level 2

    for level in range(3, user_levels + 1):
        # print(cache_original_df[cache_original_df['floor/column'] == ("floor_" + str(floor))])

        no_dupe_df = pd.concat([no_dupe_df, cache_original_df[cache_original_df['level'] == level]])



    no_dupe_df.to_csv('out.csv')

    Func = open("checklist.html", "w")

    html_dictionary = {}

    level_3_rows = no_dupe_df.loc[no_dupe_df['level'] == 3]
    level_4_rows = no_dupe_df.loc[no_dupe_df['level'] == 4]

    level_3_rows.to_csv('level_3_rows.csv')

    for row in level_3_rows.index:

        if ((no_dupe_df['level'] == 4) & (no_dupe_df['liststring'] == level_3_rows['liststring'][row])).any():
            sub_comp_pandas = level_4_rows.loc[level_4_rows['liststring'] == level_3_rows['liststring'][row]]
            #print(sub_comp_pandas)


            Func.write(f"<p>{level_3_rows['class'][row]} ({level_3_rows['liststring'][row]}, {level_3_rows['subcomps'][row]})</p>")
            for subrow in sub_comp_pandas.index:
                Func.write(f"<p>&emsp;{sub_comp_pandas['class'][subrow]} ({sub_comp_pandas['liststring'][subrow]}, {sub_comp_pandas['subcomps'][subrow]})</p>")
                Func.write(f"<p>&emsp;&emsp;{sub_comp_pandas['potential_defects'][subrow]}</p>")

            Func.write("<hr>")
            #button1 = lev3 -> below, button2 = lev4 -> below, list of defects
        else:
            #print(0)
            Func.write(f"<p>{level_3_rows['class'][row]} ({level_3_rows['liststring'][row]}, {level_3_rows['subcomps'][row]})</p>")
            Func.write(f"<p>&emsp;{level_3_rows['potential_defects'][row]}</p>")
            #Func.write("<div class=\"collapsible\"><p>... text to be visible on page load ...</p><p>...</p><p>...</p><p>...</p></div>")
            Func.write("<hr>")

            #button1 = lev3 -> below, list of defects

    # Saving the data into the HTML file
    Func.close()

    #reference: https://www.geeksforgeeks.org/how-to-write-to-an-html-file-in-python/

main()










