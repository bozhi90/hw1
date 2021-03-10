# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061130.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.

## 訂定目標的字典，儲存[累積值, 數量]
target = {"C0A880":[0, 0], "C0F9A0":[0, 0], "C0G640":[0, 0], "C0R190":[0, 0], "C0X260":[0, 0]}
for row in data:                                      # 跑過所有資料
   if row['station_id'] in target:                    # 若此資料是目標
      PRES = float(row['PRES'])                       # 儲存PRES值
      if PRES != -999.000 and PRES != -99.000:        # 若PRES值為有效資料
         target[row['station_id']] = [target[row['station_id']][0] + PRES, target[row['station_id']][1] + 1]   # 儲存數據
## 整理輸出
target_data = []
for dat in target:                                    # 跑過目標字典中所有目標 
   if target[dat][1] != 0:                            # 若有有效數據
      target_data += [[dat, target[dat][0] / target[dat][1]]]  # 新增至輸出，輸出平均
   else:
      target_data += [[dat, None]]                    # 若無數據，輸出名字與None
#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#========================================