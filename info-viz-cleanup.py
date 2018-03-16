import csv
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

csv_file = open('data/NCWIT_DataV2_RawData.csv', 'r')
csvreader = csv.reader(csv_file)

headers = csvreader.__next__()
headers[0] = 'Record#'

data = defaultdict(dict)
for row in csvreader:
    record_num = row[0]
    for val, title in zip(row, headers):
        data[record_num][title] = val

def viz1_female():
    query1 = ['Totals, Female: Asian (Tot. F)', 'Totals, Female: Black/African American (Tot. F)', 'Totals, Female: Hispanics of any race (Tot. F)', 'Totals, Female: American Indian/Alaska Native (Tot. F)', 'Totals, Female: Native Hawaiian/Other Pacific Islander (Tot. F)', 'Totals, Female: Two or more races (Tot. F)', 'Totals, Female: White (Tot. F)']

    clean_query1 = defaultdict(list)
    years = []
    institutions = []
    for subject in data.values():
        is_clean = True
        for header in query1:
            if subject[header] == '':
                is_clean = False

        if is_clean:
            years.append(subject['School Year'])

            clean_query1[subject['Institution']].append(subject)




    # years = [int(year.split('-')[0]) for year in years]
    # plt.hist(years)
    # plt.show()
    result = defaultdict(dict)

    for name, val in clean_query1.items():
        temp = defaultdict(list)

        for row in val:
            if row['School Year'] == '2016-2017' or row['School Year'] == '2015-2016' or row['School Year'] == '2014-2015' or row['School Year'] == '2013-2014' or row['School Year'] == '2012-2013':
                temp[row['School Year']].append(row)

        if len(list(temp.keys())) == 5:
            for year_num, year_data in temp.items():
                institution = year_data[0]['Institution']
                query_sums = [0]*len(query1)

                for major in year_data:
                    for index, header in enumerate(query1):
                        query_sums[index] += int(major[header])

                result[year_num][institution] = np.array(query_sums)





    for year,vals in result.items():
        temp = np.array([0]*len(query1))
        for institution in vals.values():
            temp = np.add(temp, institution)

        for num, header in zip(temp, ['Asian', 'Black', 'Hispanic', 'Native American','Pacific', 'White']):
            print(year, ',',header,',' ,num)


def viz1_male():
    query1 = ['Totals, Male: Asian (Tot. M)', 'Totals, Male: Black/African American (Tot. M)', 'Totals, Male: Hispanics of any race (Tot. M)', 'Totals, Male: American Indian/Alaska Native (Tot. M)', 'Totals, Male: Native Hawaiian/Other Pacific Islander (Tot. M)', 'Totals, Male: Two or more races (Tot. M)', 'Totals, Male: White (Tot. M)']

    clean_query1 = defaultdict(list)
    years = []
    institutions = []
    for subject in data.values():
        is_clean = True
        for header in query1:
            if subject[header] == '':
                is_clean = False

        if is_clean:
            years.append(subject['School Year'])

            clean_query1[subject['Institution']].append(subject)




    # years = [int(year.split('-')[0]) for year in years]
    # plt.hist(years)
    # plt.show()
    result = defaultdict(dict)

    for name, val in clean_query1.items():
        temp = defaultdict(list)

        for row in val:
            if row['School Year'] == '2016-2017' or row['School Year'] == '2015-2016' or row['School Year'] == '2014-2015' or row['School Year'] == '2013-2014' or row['School Year'] == '2012-2013':
                temp[row['School Year']].append(row)

        if len(list(temp.keys())) == 5:
            for year_num, year_data in temp.items():
                institution = year_data[0]['Institution']
                query_sums = [0]*len(query1)

                for major in year_data:
                    for index, header in enumerate(query1):
                        query_sums[index] += int(major[header])

                result[year_num][institution] = np.array(query_sums)





    for year,vals in result.items():
        temp = np.array([0]*len(query1))
        for institution in vals.values():
            temp = np.add(temp, institution)

        for num, header in zip(temp, ['Asian', 'Black', 'Hispanic', 'Native American','Pacific', 'White']):
            print(year, ',',header,',' ,num)



def viz2():
    query1 = ['Totals, Female: Enrolled in DIFFERENT MAJOR (Tot. F)',
              'Totals, Female: Enrolled in SAME MAJOR (Tot. F)',
              'Totals, Female: Left Institution (not graduated) (Tot. F)',
              'Totals, Male: Enrolled in DIFFERENT MAJOR (Tot. M)',
              'Totals, Male: Enrolled in SAME MAJOR (Tot. M)',
              'Totals, Male: Left Institution (not graduated) (Tot. M)']

    clean_query1 = defaultdict(list)
    for subject in data.values():
        is_clean = True
        for header in query1:
            if subject[header] == '':
                is_clean = False

        if is_clean:
            clean_query1[subject['Institution']].append(subject)


    result = defaultdict(dict)
    print('Institution#, Female Different, Female Same, Female Left, Male Different, Male Same, Male Left')
    for institution, rows in clean_query1.items():
        query_sums = [0] * len(query1)
        for row in rows:
            for index, header in enumerate(query1):
                query_sums[index] += int(row[header])

        row_string = institution
        for num in query_sums:
            row_string += ', '+str(num)
        print(row_string)

def viz3():
    query1 = ['Enroll, Female: Average HS GPA (Enrl F)',
              'Enroll, Male: Average HS GPA (Enrl M)',
              'Enroll, Female: Avg. ACT Math Score (Enrl F)',
              'Enroll, Male: Avg. ACT Math Score (Enrl M)',
              'Enroll, Female: New Enrollments (Enrl F)',
              'Enroll, Male: New Enrollments (Enrl M)']

    print('Institution#, Female HS GPA, Male HS GPA, Females Enrolled')
    clean_query1 = defaultdict(list)
    for subject in data.values():
        is_clean = True
        for header in query1:
            if subject[header] == '':
                is_clean = False

        if is_clean and subject['School Year'] == '2014-2015':
            clean_query1[subject['Institution']].append(subject)

            row_string = subject['Institution']
            for header in query1:
                if header != 'Enroll, Female: New Enrollments (Enrl F)' and header != 'Enroll, Male: New Enrollments (Enrl M)' and header != 'Enroll, Female: Avg. ACT Math Score (Enrl F)' and header != 'Enroll, Male: Avg. ACT Math Score (Enrl M)':
                    row_string += ', '+subject[header]
            row_string += ', '+str(float(subject['Enroll, Female: New Enrollments (Enrl F)'])/(float(subject['Enroll, Female: New Enrollments (Enrl F)'])+ float(subject['Enroll, Male: New Enrollments (Enrl M)'])))
            print(row_string)

    print()
    print('Institution#, FemaleACTMath, MaleACTMath, Females Enrolled')
    clean_query1 = defaultdict(list)
    for subject in data.values():
        is_clean = True
        for header in query1:
            if subject[header] == '':
                is_clean = False

        if is_clean and subject['School Year'] == '2014-2015':
            clean_query1[subject['Institution']].append(subject)

            row_string = subject['Institution']
            for header in query1:
                if header != 'Enroll, Female: New Enrollments (Enrl F)' and header != 'Enroll, Male: New Enrollments (Enrl M)' and header != 'Enroll, Male: Average HS GPA (Enrl M)' and header != 'Enroll, Female: Average HS GPA (Enrl F)':
                    row_string += ', ' + subject[header]
            row_string += ', ' + str(float(subject['Enroll, Female: New Enrollments (Enrl F)']) / (
            float(subject['Enroll, Female: New Enrollments (Enrl F)']) + float(
                subject['Enroll, Male: New Enrollments (Enrl M)'])))
            print(row_string)






############################################main
# viz1_female()
# viz1_male()
# viz2()
viz3()








