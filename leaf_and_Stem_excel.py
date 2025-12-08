import pandas as pd

def stem_leaf_dataframe(data_list):
    # Sort data
    sort_data = sorted(data_list)

    stem_all = []
    leaf_all = []

    for v in sort_data:
        s = str(v)

        # Decimal case (e.g., 34.2)
        if "." in s:
            whole, decimal = s.split(".")
            stem_all.append(whole)
            leaf_all.append(decimal)
        else:
            stem_all.append(s[:-1])   # stem = all but last digit
            leaf_all.append(s[-1])    # leaf = last digit

    # Build dictionary stem → leaves
    stems = sorted(list(set(stem_all)))
    stem_leaf_dict = {st: [] for st in stems}

    for st, lf in zip(stem_all, leaf_all):
        stem_leaf_dict[st].append(lf)

    # Build DataFrame rows
    max_leaf_count = max(len(v) for v in stem_leaf_dict.values())
    rows = []

    for st in stems:
        leaves = stem_leaf_dict[st]
        row = [st] + leaves + [""] * (max_leaf_count - len(leaves))
        rows.append(row)

    # Create DataFrame
    col_names = ["stem"] + [f"leaf{i+1}" for i in range(max_leaf_count)]
    df_stem = pd.DataFrame(rows, columns=col_names)

    # Add sorted raw data
    df_data = pd.DataFrame({"data": sort_data})

    return pd.concat([df_data, df_stem], axis=1)


# ------------------------------------------------------
# NEW FUNCTION — only one input list
# ------------------------------------------------------
def create_excel(data_list, file_name="stem_leaf_form_python.xlsx"):
    df = stem_leaf_dataframe(data_list)

    with pd.ExcelWriter(file_name, engine="xlsxwriter") as writer:
        df.to_excel(writer, sheet_name="stem_leaf_form_python", index=False)

    print(f"Excel created successfully: {file_name}")


if __name__ == "__main__":
    data_list1 = [
        1115, 1567, 1223, 1782, 1055, 1310, 1883, 375, 1522, 1764,
        1540, 1203, 2265, 1792, 1330, 1502, 1270, 1910, 1000, 1608,
        1258, 1015, 1018, 1820, 1535, 1315, 845, 1452, 1940, 1781,
        1085, 1674, 1890, 1120, 1750, 798, 1016, 2100, 910, 1501,
        1020, 1102, 1594, 1730, 1238, 865, 1605, 2023, 1102, 990,
        2130, 706, 1315, 1578, 1468, 1421, 2215, 1269, 758, 1512,
        1109, 785, 1260, 1416, 1750, 1481, 885, 1888, 1560, 1642
    ]


    create_excel(data_list1)
