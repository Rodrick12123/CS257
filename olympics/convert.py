#read csv files
import csv
# class convert:
#     def __intit__(self):
        
        # with open('athlete.csv', 'w') as f2:
        #     with open('athele_events.csv', mode='r') as infile:
        #         reader = csv.reader(infile)
        #         for row in reader:  # content is all the other lines
        #             f2.write(row)  # writing line without last comma
                

        # with open('athele_events.csv', mode='r') as infile:
        #     reader = csv.reader(infile)
        #     for row in reader:
        #         print(row)
    

def main():
    #writes info from big athlete csv file to smaller one
    with open('athlete.csv', 'w') as f2:
            with open('athlete_events.csv', mode='r') as infile:
                reader = csv.reader(infile)
                next(reader)
                for row in reader:  # content is all the other lines
                    #print(row[0])
                    f2.write(row[0] + ',' + row[1] + ',' + row[2] + ',' + row[3] + ',' + row[4] + ',' + row[5] + ',' + row[6] + ',' + row[7] + ',' + row[8] + ',' + row[9]  + ',' + row[10] + ',' + row[11] + ',' + row[12] + ',' + row[13] + ',' + row[14] + '\n')
    
    #writes info from big noc csv file to smaller one
    with open('noc.csv', 'w') as f3:
            with open('noc_regions.csv', mode='r') as infile2:
                reader2 = csv.reader(infile2)
                next(reader2)
                for row in reader2:  # content is all the other lines
                    #print(row[0])
                    f3.write(row[0] + ',' + row[1] + ',' + row[2] + '\n')

if __name__ == "__main__":
    main()
        


