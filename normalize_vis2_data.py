f = open('data/vis2_data.csv', 'r')

f.readline()

lines = f.readlines()

rows = []
normalized_rows = []

for line in lines:
    rows.append(line.replace('\n', '').split(','))

for row in rows:
    normalized_row = []
    normalized_row.append(float(row[0]))
    f1 = float(row[1])
    f2 = float(row[2])
    f3 = float(row[3])
    m1 = float(row[4])
    m2 = float(row[5])
    m3 = float(row[6])
    f_sum = f1 + f2 + f3
    m_sum = m1 + m2 + m3
    normalized_row.append(100 * (f1 / f_sum))
    normalized_row.append(100 * (f2 / f_sum))
    normalized_row.append(100 * (f3 / f_sum))
    normalized_row.append(100 * (m1 / m_sum))
    normalized_row.append(100 * (m2 / m_sum))
    normalized_row.append(100 * (m3 / m_sum))
    normalized_rows.append(normalized_row)

f = open('vis2_normalized_data.csv', 'w')

f.write('institution,femaleDifferent,femaleSame,femaleLeft,maleDifferent,maleSame,maleLeft\n')
for nr in normalized_rows:
    f.write(str(int(nr[0])) + ',' + str(nr[1:]).replace('[', '').replace(']', '').replace(' ', '') + '\n')
