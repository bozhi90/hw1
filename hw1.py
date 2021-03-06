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

## 訂定目標的字典，儲存[最大值, 最小值]，預設為[-99, -99]
traget = {"C0A880":[-99,-99], "C0F9A0":[-99,-99], "C0G640":[-99,-99], "C0R190":[-99,-99], "C0X260":[-99,-99]}
for row in data:                                      # 跑過所有資料
   if row['station_id'] in traget:                    # 若此資料是目標
      WSDS = float(row['WDSD'])                       # 儲存WSDS值
      if WSDS != -999.000 and WSDS != -99.000:        # 若WSDS值為有效資料
         if traget[row['station_id']] == [-99,-99]:   # 儲存第一筆數據
            traget[row['station_id']] = [WSDS, WSDS]
         if WSDS > traget[row['station_id']][0]:      # WSDS值若大於目標之最大值，儲存至最大值
            traget[row['station_id']][0] = WSDS
         if WSDS < traget[row['station_id']][1]:      # WSDS值若小於目標之最小值，儲存至最小值
            traget[row['station_id']][1] = WSDS
## 整理輸出
target_data = []
for dat in traget:                                    # 跑過目標字典中所有目標 
   if traget[dat] != [-99,-99]:                       # 若有數據更新最大最小值
      target_data += [[dat, traget[dat][0] - traget[dat][1]]]  # 新增至輸出，輸出名字與最大最小值的差
   else:
      target_data += [[dat, None]]                    # 若無數據，輸出名字與None
#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#========================================