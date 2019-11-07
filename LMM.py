import gspread
from oauth2client.service_account import ServiceAccountCredentials
from random import shuffle


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open_by_url('timetable url').worksheet("Timetable")

# Extract and print all of the values
list_of_hashes = sheet.get_all_values()

name_of_people = [name[0] for name in list_of_hashes if name[0] != "Mo's"]

for col in range(2,9):
    list_of_jobs = ["Contributor","Contributor","Contributor","Recruiter","Recruiter","Recruiter"]
    shuffle( list_of_jobs )
    for row,job in zip( range( 2,len(name_of_people) + 2 ),list_of_jobs  ):
        print(row,col,job)
        sheet.update_cell(row,col,job)
    print("\n")

# for row in range( 2 , len( list_of_hashes ) + 1):
#     list_of_jobs = ["Contributer","Contributer","Contributer","Contributer","Contributer","Recruiter","Recruiter"]
#     shuffle( list_of_jobs )
#     for col,job in zip(range( 2 , len(list_of_hashes[row - 1]) + 1),list_of_jobs):
#         sheet.update_cell(row,col,job)
