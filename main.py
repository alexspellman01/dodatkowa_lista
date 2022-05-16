import pandas as pd
pd.options.mode.chained_assignment = None
dane = pd.read_csv("logs_converted_final.csv")

wynik = []
# wynik.append(dane.columns)
dane_poczatkowe = dane
kolumny = []
i = 0
non_repeated_line = dane_poczatkowe.loc[2]

for line in dane_poczatkowe:
    if i ==0:
        kolumny.append(line)
    elif i ==1:
        non_repeated_line ==line
            
for i in range(1,len(dane_poczatkowe)):
    if non_repeated_line["sessionNo"] ==dane_poczatkowe.loc[i]["sessionNo"]:
        non_repeated_line["duration"] = float(non_repeated_line["duration"]) + float(dane_poczatkowe.loc[i]["sessionNo"])
        non_repeated_line["cCount"] = float(non_repeated_line["cCount"]) + float(dane_poczatkowe.loc[i]["cCount"])
        non_repeated_line["cMinPrice"] = min(float(non_repeated_line["cMinPrice"]),float(dane_poczatkowe.loc[i]["cMinPrice"]))
        non_repeated_line["cMaxPrice"] = max(float(non_repeated_line["cMaxPrice"]),float(dane_poczatkowe.loc[i]["cMaxPrice"]))
        non_repeated_line["cSumPrice"] = float(non_repeated_line["cSumPrice"])+float(dane_poczatkowe.loc[i]["cSumPrice"])
        non_repeated_line["bCount"] = float(non_repeated_line["bCount"])+float(dane_poczatkowe.loc[i]["bCount"])
        non_repeated_line["bMinPrice"] = min(float(non_repeated_line["bMinPrice"]),float(dane_poczatkowe.loc[i]["bMinPrice"]))
        non_repeated_line["bMaxPrice"] = max(float(non_repeated_line["bMaxPrice"]),float(dane_poczatkowe.loc[i]["bMaxPrice"]))
        non_repeated_line["bSumPrice"] = float(non_repeated_line["bSumPrice"])+float(dane_poczatkowe.loc[i]["bSumPrice"])
        non_repeated_line["bStep"] = int(non_repeated_line["bStep"])+int(dane_poczatkowe.loc[i]["bStep"])

        if non_repeated_line["onlineStatus"] =="y" or dane_poczatkowe.loc[i]["onlineStatus"] == "y":
            non_repeated_line["onlineStatus"] = "y"
        else:
            non_repeated_line["onlineStatus"] = "n"
        if non_repeated_line["availability"] =="completely orderable" or dane_poczatkowe.loc[i]["availability"] == "completely orderable":
            non_repeated_line["availability"] = "completely orderable"
        else:
            non_repeated_line["availability"] = "0"

        non_repeated_line["maxVal"] = max(float(non_repeated_line["maxVal"]),float(dane_poczatkowe.loc[i]["maxVal"]))
        non_repeated_line["payments"] = float(non_repeated_line["payments"])+float(dane_poczatkowe.loc[i]["payments"])

        if non_repeated_line["order"] =="y" or dane_poczatkowe.loc[i]["order"] == "y":
            non_repeated_line["order"] = "y"
        else:
            non_repeated_line["order"] = "n"
    else:
        wynik.append(non_repeated_line)
        non_repeated_line = dane_poczatkowe.loc[i]
    
wynik_df = pd.DataFrame(wynik)
wynik_df.to_csv('wynik_final.csv',index=False,sep='|')
