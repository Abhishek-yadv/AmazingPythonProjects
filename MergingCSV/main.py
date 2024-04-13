###################################################################
################################################### MergingCSV
###################################################################
# import neccesarry library
import os
import glob
import pandas as pd
directory_path = r"D:\Samplefile\csvfiles"

# directory_path = os.path.join("D:", "Samplefile", "csvfiles")
all_csv_files = glob.glob(directory_path + '\\*.csv')
print(type(all_csv_files))  # type '<class 'str'>'

# make dataframe objects because in pandas concat method only series dataframe valid 
# combined_csv = pd.concat([pd.read_csv(r'{}'.format(f)) for f in all_csv_files], ignore_index=True)

combined_csv = pd.concat([pd.read_csv(file) for file in all_csv_files], ignore_index =True)

combined_csv.to_csv("combined_csv.csv", index=False)


