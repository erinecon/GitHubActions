import datefinder

class ChangelogEntry:

    def __init__(self):
        self.month = month
        self.year = year
        self.linenum = num
        self.items = [] # list of items in the entry

month = "05"
year = "2025"
major_item = "major"
minor_item = "minor"
dep_item = "deprecated"
changelogname = "/Users/econley/GitHubActions/changelog.md"

# first get the line numbers we care about
line_numbers_of_all_entries = []

entries: list[ChangelogEntry] = []

with open(changelogname) as f:
    for num, line in enumerate(f):
        matches = list(datefinder.find_dates(line))
        bool0 = "##" in line
        if bool0 == True and len(matches) > 0:
            entry = ChangelogEntry() 
            entry.month = matches[0].month
            entry.year = matches[0].year
            entry.linenum = num
            entries.append(entry)

f = open(changelogname)
lines = f.readlines()
total_num_entries = len(entries)
for num, entry in enumerate(entries):
    if(num == total_num_entries-1):
        # keep items in last entry
        for i in range(entry.linenum, len(lines)):
            entry.items.append(lines[i])
        break
    else:
        # keep items in all other entries
        for i in range(entry.linenum+1, entries[num+1].linenum):
            entry.items.append(lines[i])
    
f.close()

# then need to use the template 
# create a new file
# loop over the entries
# check whether the date is appropriate
# check all the items and see if they have the right tags
# items with right tags fill in details of the template