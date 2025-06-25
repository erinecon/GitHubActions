import datefinder

class ChangelogEntry:

    def __init__(self):
        self.month = month
        self.year = year
        self.items = [] # list of items in the entry

month = "05"
year = "2025"
major_item = "major"
minor_item = "minor"
dep_item = "deprecated"

# first get the line numbers we care about
line_numbers_of_all_entries = []
line_numbers_we_care_about = []

entries: list[ChangelogEntry] = []

f = open("changelog.md")

with f:
    for num, line in enumerate(f, 0):
        matches = list(datefinder.find_dates(line))
        bool0 = "##" in line
        print(line)
        if bool0 == True and len(matches) > 0:
            # we have an entry!
            #print("\tEntry: " + str(line))
            entry = ChangelogEntry() 
            entry.month = matches[0].month
            entry.year = matches[0].year
            # now I want to get all the items until the next date
            for num2, line2 in enumerate(f, num):
                if "##" in line2:
                    break
                else:
                    #print(line2)
                    entry.items.append(line2)


""" 
with f:
    for num, line in enumerate(f, 0):
        bool0 = "##" in line
        if bool0 == True:
            print("Entry: " + str(line))
            line_numbers_of_all_entries.append(num)
            entry = ChangelogEntry() 
            matches = list(datefinder.find_dates(line))
            if len(matches) > 0:
                entry.month = matches[0].month
                entry.year = matches[0].year
            # now I want to get all the items until the next date
            for num2, line2 in enumerate(f, num):
                if "##" in line2:
                    break
                else:
                    print(line2)
"""

# then need to loop over the line numbers we care about
# for num in line_numbers_of_all_entries:
    # print("hello " + str(num))
    

    # get the items under that entry
    # and see whether major, minor, or dep show up

# then need to use the template 
# create a new file
# and use the major, minor, or dep items to fill in details

f.close()