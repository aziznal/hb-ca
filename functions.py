
def save_as_csv(data, col_names, filename, overwrite=False):
    """
    Take in data as a list of dictionaries
    and save it as a csv
    """

    column_names = ",".join(col_names)

    with open(filename, "w" if overwrite else "a") as file:
        file.write(column_names + "\n")

        for entry in data:
            for key in entry.keys():
                file.write(f"{unidecode(str(entry[key]))},")

            file.write('\n')

