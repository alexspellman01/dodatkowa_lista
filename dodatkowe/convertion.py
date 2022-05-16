import pandas as pd
data = ""
# with open("logs.txt") as file:
#      data = file.read().replace("?","0")

# with open("final_logs.txt","w") as file:
#      file.write(data)
     

df = pd.read_csv('final_logs.txt',delimiter="|")
df.to_csv('logs_converted_final.csv', 
                  index = False)