month = "05"
year = "2025"
major_item = "major"
minor_item = "minor"
dep_item = "dep"

# first get the line numbers we care about
line_numbers_of_entries = []
line_numbers_we_care_about = []

with open("changelog.md") as f:
    for num, line in enumerate(f, 0):
        bool0 = "##" in line
        if bool0 == True:
            line_numbers_of_entries.append(num)
        bool1 = month in line and year in line
        if bool1 == True:
            line_numbers_we_care_about.append(num)

# then need to loop over the line numbers we care about
# get the items under that entry
# and see whether major, minor, or dep show up

# then need to use the template 
# create a new file
# and use the major, minor, or dep items to fill in details

