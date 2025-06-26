import datefinder

class ChangelogEntry:

    def __init__(self):
        self.month = month
        self.year = year
        self.linenum = num
        self.items = [] # list of items in the entry

def substring_after(s, delim):
    return s.partition(delim)[2]

month = "5"
year = "2025"
major_item_tag = "major"
minor_item_tag = "minor"
dep_item_tag = "deprecated"
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

# sort the items into major, minor, deprecated
major_items = []
minor_items = []
deprecated_items = []

# loop over the entries
for entry in entries:
    # check whether the date is appropriate
    if str(entry.month) == month and str(entry.year) == year:
        # check all the items and see if they have the right tags
        for item in entry.items:
            # items with right tags fill in details of the template
            # rule: no item can have multiple tags (major, minor, deprecated)
            # start with major
            if major_item_tag in item:
                major_items.append(substring_after(item, "): "))
            elif minor_item_tag in item:
                minor_items.append(substring_after(item, "): "))
            elif dep_item_tag in item:
                deprecated_items.append(substring_after(item, "): "))


# then need to use the template 
# create a new file
release_notes_file_name = "release-notes-" + str(year) + "-" + str(month) + ".md"
with open("docs/"+release_notes_file_name, 'w') as outFile:
    with open("release-notes-template.md") as releaseNotesFile:
        for line in releaseNotesFile:
            outFile.write(line)
            if "What's new" in line.strip():
                # write all the major items under this section
                outFile.write("\n")
                for item in major_items:
                    outFile.write("### " + item)
                    outFile.write("\n<Engineers to add more context and information about the entry>\n\n")
            elif "Minor features" in line.strip():
                # write all minor items under this section
                outFile.write("\n")
                for item in minor_items:
                    outFile.write("### " + item)
                    outFile.write("\n<Engineers to add more context and information about the entry>\n\n")
            elif "Deprecated features" in line.strip():
                # write all minor items under this section
                outFile.write("\n")
                for item in deprecated_items:
                    outFile.write("### " + item)
                    outFile.write("\n<Engineers to add more context and information about the entry>\n\n")