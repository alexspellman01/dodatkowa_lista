import pandas as pd
with open("logs.txt","r") as f:
    with open("wynik.txt","a") as w:
        plik = f.readlines()
        i = 0
        new_line = ""
        for line in plik:
            
            print(line)
            line = line.split("|")
            value_23 = line[23]
            if i ==1:
                non_repeated_line=line
            elif i ==0:
                columns = line
                # df = pd.DataFrame() dodane
                # df.to_csv("wynik_csv.csv",columns=line,index=False)
            else:
                if line[0] == non_repeated_line[0]:
                    non_repeated_line[23] = value_23
                    non_repeated_line[3]=float(line[3]) +float(non_repeated_line[3]) #duaration 
                    non_repeated_line[4] = float(line[4]) +float(non_repeated_line[4]) #cCount
                    # non_repeated_line[5] = float(line[]) +float(non_repeated_line[])
                    # non_repeated_line[] = float(line[]) +float(non_repeated_line[])
                    # non_repeated_line[] = float(line[]) +float(non_repeated_line[])
                    print(non_repeated_line)

                    
            
            i+=1
            if i>10:
                break
                
        print(new_line)

     