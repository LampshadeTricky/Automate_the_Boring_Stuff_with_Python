#! python3

import os, openpyxl, pprint

os.chdir('C:\\Users\\jonat\\Documents\\Python\\Sandbox')

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
ws = wb['Population by Census Tract']

countyData = {}

print('Reading rows...')
for row in range(2, ws.max_row + 1):
    # each row in the spreadsheet has data for one census tract.
    state = ws['B' + str(row)].value
    county = ws['C' + str(row)].value
    pop = ws['D' + str(row)].value

    # Make sure the key for this state exists.
    countyData.setdefault(state, {})
    # Make sure the key for this county in this state exists.
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # Each row represents one census tract, so increment by one.
    countyData[state][county]['tracts'] += 1
    # Increase the county pop by the pop in this census tract.
    countyData[state][county]['pop'] += int(pop)

# Open a new text file and write the contents of countyData to it.
print('Writing results...')
resultFile = open('census2010.py','w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')

print('Closing workbook')
wb.close()