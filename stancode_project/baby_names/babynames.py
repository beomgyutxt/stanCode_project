"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

The program constructs a new database which stores popular baby name
and their rank in each year by reading txt files.
User can search for some interested words(target) in these database
and the program will return a list names that contain the target.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    if name not in name_data:  # add new name
        name_data[name] = {year: rank}
    else:
        if year not in name_data[name]:  # add new year(rank)
            name_data[name][year] = rank
        else:
            if int(rank) < int(name_data[name][year]):  # store lower rank
                name_data[name][year] = rank


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    with open(filename, 'r') as f:  # read a file
        for line in f:
            if line[0:4].isdigit() and line[0:4] != '1000':
                year = line[0:4]   # the year of the file (at the first line)
            else:
                # construct a list and put elements into variables
                # [rank, boy name, girl name] --> rank, name_1, name_2
                rank_name = line.split(',')
                rank = rank_name[0]
                rank = rank.strip()
                name1 = rank_name[1]
                name1 = name1.strip()
                name2 = rank_name[2]
                name2 = name2.strip()

                # add these variables into name_data(dict)
                add_data_for_name(name_data, year, rank, name1)
                add_data_for_name(name_data, year, rank, name2)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}                     # construct a new dict
    for i in range(len(filenames)):    # read files, respectively
        filename = filenames[i]
        add_file(name_data, filename)  # add the data from files into name_data(dict)
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    target.lower()                         # target --> case-insensitive
    names = []                             # a list storing names that contain the target string
    for key, value in name_data.items():
        searched_name = key.lower()        # names --> case-insensitive
        if target in searched_name:
            names.append(key)              # add names into the list
    return names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
