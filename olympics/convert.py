'''
conver.py
Rodrick Lankford

'''
import csv
#increments gold medal count in noc.csv by 1
def add_gold(noc,dic):
    for n in dic:
        if n == noc:
            key = noc
            dic[key] += 1
    return dic


def main():
    #dictonary of noc regions with gold medal values
    noc_dict = {}
    with open('noc_regions.csv', mode='r') as infile2:
            reader2 = csv.reader(infile2)
            next(reader2)
            for row in reader2:  
                noc_dict[row[0]] = 0

    #writes info from big athlete csv file to smaller two seperate files
    with open('athlete.csv', 'w', newline='') as f1:
            with open('event.csv', 'w', newline='') as f2:
                    with open('athlete_events.csv', mode='r') as infile:
                        reader = csv.reader(infile)
                        csvwriter1 = csv.writer(f2) #write to event file
                        csvwriter2 = csv.writer(f1) #write to athlete file
                        next(reader)
                        cnt = 1
                        for row in reader: 
                            name = row[1].split(' ')
                            last = name[-1]
                            first = name[0]
                            if row[4] == 'NA':
                                row[4] = 0
                            if row[5] == 'NA':
                                row[5] = 0
                            if row[3] == 'NA':
                                row[3] = 0
                            if row[14] == 'Gold':
                                add_gold(row[7], noc_dict)
                            if int(row[0]) == cnt:
                                csvwriter2.writerow([row[0]] + [first] + [last] + [row[2]])
                                cnt = cnt + 1                          
                            csvwriter1.writerow([row[0]] + [row[3]] + [row[4]] + [row[5]] + [row[6]] + [row[7]] + [row[8]] + [row[9]]  + [row[10]] + [row[11]] + [row[12]] + [row[13]] + [row[14]])
                           
    f1.close()
    f2.close()
    infile.close()
    #read from big noc file and write to a smaller file
    with open('noc.csv', 'w', newline='') as f3:
            with open('noc_regions.csv', mode='r') as infile2:
                reader2 = csv.reader(infile2)
                csvwriter3 = csv.writer(f3)
                next(reader2)
                cnt = 1
                for row in reader2:  
                    csvwriter3.writerow([str(cnt)]  + [row[0]] + [row[1]] + [noc_dict[row[0]]])
                    cnt = cnt + 1
    f3.close()
    infile2.close()

                
if __name__ == "__main__":
    main()
        


