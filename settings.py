# Some basic settings

# List of directories to backup along with some specs
# Each element of the SRC list is a 3-tuple containing:
#   1. the full path to the directory.
#   2. the mode of copying (whether 'tree' or 'dir').
#   3. a list of directory names or filenames to exclude.
# Ex:
#   ('C:/Python27', 'tree', ['Scripts', 'python.exe'])
SRC = [
    # uncomment the below line to add directory. 
    # ( u'', u'', u''),
    # ( u'', u'', u''),
    # ( u'', u'', u'')
    # add as many 3-tupls as you need.
]

# This is the full path to the Google Drive directory or 
# Full path to a folder in the Google Drive directory (recommended)
DST = u''
