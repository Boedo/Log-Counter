import glob # Directory Reader module
import xlwt #Excel Writer module
import re # RegEx module
from datetime import datetime
startTime = datetime.now()

################################################################################################

folder = 'C:\\Users\\nicol\\Downloads\\logs/*.log'

####################################### Tag Count ###############################################
print "Starting Tag View Script"

startTimeAdView = datetime.now()

row_Ad = 1
tag_count = 0
Parameters = []

for file in glob.iglob(folder): #iterate through files in the directory
    substr = "substring" # Substring to look for

    with open (file, 'rt') as in_file: # Read file
        for line in in_file: # Read each line in the file
            if all(s in line for s in Parameters):

                str = line # store the line in a variable
                index = 0 # Initiates index as the start of each line

                while index < len(str):
                    index = str.find(substr, index)

                    # if substring isn't found in the line, stop searching and go to next instructions (restart process on next log entry)
                    if index == -1:
                        break

                    else:
                        tag_count += 1
                        print tag_count
                        print line

                        row_Ad += 1
                        index += len(str)

print datetime.now() - startTimeAdView
#################################################################################################################

print "The Final Result is:"
print tag_count

print datetime.now() - startTime
