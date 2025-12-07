def stem_leaf(data_list):

    sort_data_list = sorted(data_list)

    count = 0
    count1 = 0

    stem_all = []
    leaf = []
    leaf_all = []

    range_list = len(sort_data_list)

    for i in range(range_list):
        com_1_str_sort_data_list = str(sort_data_list[i])

        com_1_range_sort_data_list = len(com_1_str_sort_data_list)
    
        stem1 = com_1_range_sort_data_list - 1
    
        com_1 = com_1_str_sort_data_list[0 : stem1]
        leaf_value = com_1_str_sort_data_list[stem1]

        stem_all.append(com_1)
        leaf_all.append(leaf_value)


    stem = []
    for i in range(range_list - 1):
        com_1_str_sort_data_list = str(sort_data_list[i])
        com_2_str_sort_data_list = str(sort_data_list[i + 1])

        com_1_range_sort_data_list = len(com_1_str_sort_data_list)
        com_2_range_sort_data_list = len(com_2_str_sort_data_list)
    
        stem1 = com_1_range_sort_data_list - 1
        stem2 = com_2_range_sort_data_list - 1
    
        com_1 = com_1_str_sort_data_list[0 : stem1]
        com_2 = com_2_str_sort_data_list[0 : stem2]
    
        if i == 0 :
            stem.append(com_1)

        if com_1 != com_2:
            stem.append(com_2)


    leaf = []
    current_leaf_loop = []
    stem_index = 0
    for i in range(range_list):
        if stem_all[i] == stem[stem_index]: 
            current_leaf_loop.append(leaf_all[i])
        else:
            leaf.append(current_leaf_loop)
            current_leaf_loop = [leaf_all[i]]
            stem_index += 1

    leaf.append(current_leaf_loop)

    print("---------------------------------------------------------")
    print("|\tstem\t\t|\t\tleaf\t\t|")
    print("---------------------------------------------------------")
    for i in range(len(leaf)):
        print(f"\t {stem[i]}\t\t|\t\t{(leaf[i])}\t\t")



if __name__ == "__main__":
    data_list1 = [
        1115, 1567, 1223, 1782, 1055,
        1310, 1883, 375 , 1522, 1764, 
        1540, 1203, 2265, 1792, 1330, 
        1502, 1270, 1910, 1000, 1608, 
        1258, 1015, 1018, 1820, 1535, 
        1315, 845 , 1452, 1940, 1781, 
        1085, 1674, 1890, 1120, 1750, 
        798 , 1016, 2100,  910, 1501, 
        1020, 1102, 1594, 1730, 1238, 
        865 , 1605, 2023, 1102,  990, 
        2130,  706, 1315, 1578, 1468, 
        1421, 2215, 1269,  758, 1512, 
        1109,  785, 1260, 1416, 1750,
        1481,  885, 1888, 1560, 1642
    ]

    data_list2  = [
        34.2, 33.6, 33.8, 34.7, 
        33.1, 34.7, 34.2, 33.6, 
        34.5, 35.0, 33.4, 32.5, 
        35.6, 35.4, 34.7, 34.1, 
        36.3, 36.2, 34.6, 35.1, 
        35.1, 36.8, 35.2, 36.8, 
        34.7, 35.1, 35.0, 37.9, 
        33.6, 35.3, 34.9, 36.4, 
        37.8, 32.6, 35.8, 34.6, 
        36.6, 33.1, 37.6, 33.6, 
        35.4, 34.6, 37.3, 34.1, 
        34.6, 35.9, 34.6, 34.7, 
        33.8, 34.7, 35.5, 35.7, 
        37.1, 33.6, 32.8, 36.8, 
        34.0, 32.9, 32.1, 34.3, 
        34.1, 33.5, 34.5, 32.7
    ]

    stem_leaf(data_list1)
    print("_________________________________________________________________________________________________________________________________________________________________")
    stem_leaf(data_list2)
