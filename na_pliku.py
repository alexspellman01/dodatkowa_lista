import pandas as pd
with open("logs.txt","r") as f:
    with open("wynik.txt","a") as w:
        plik = f.readlines()
        i = 0
        new_line = ""
        for line in plik:
            line = line.split("|")
            
            if i ==1:
                non_repeated_line=line
            elif i ==0:
                columns = line
                # df = pd.DataFrame() dodane
                # df.to_csv("wynik_csv.csv",columns=line,index=False)
            else:
                if line[0] == non_repeated_line[0]:
                    non_repeated_line[3]=float(line[3]) +float(non_repeated_line[3]) #duaration 
                    print(non_repeated_line)
                    
            
            i+=1
            if i>10:
                break
                
        print(new_line)

     