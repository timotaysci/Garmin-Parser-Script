import fitparse
import pandas as pd
import matplotlib.pyplot as plt
# Load the FIT file
fitfile = fitparse.FitFile("activity.fit")

#Get the headings from the activity file
allHeadings =[]
for record in fitfile.get_messages("record"):
    for data in record:
        k = str(data.name) + ' (' + str(data.units) + ')'
        allHeadings.append(k)
#Removes duplicates from headings
allHeadings = list(dict.fromkeys(allHeadings))


#Here we iterate over the records and format them into columns which are easier to plot.

dictR = {}
df = pd.DataFrame(columns =allHeadings)
for record in fitfile.get_messages("record"):
    for data in record:
        k = str(data.name) + ' (' + str(data.units) + ')'
        v = {k : data.value}
        dictR.update(v)
    df = df.append(dictR, ignore_index=True)


#Creates a column to give activity in seconds
base_dt = df['timestamp (None)'].iloc[0]
df['Elapsed Time (s)'] = (df['timestamp (None)'] - base_dt).dt.total_seconds()


#Export to .CSV
print(df)
df.to_csv('output.csv') 



plt.plot(df['Elapsed Time (s)'],df['distance (m)'], label = 'Distance ')
plt.plot(df['Elapsed Time (s)'],df['heart_rate (bpm)'], label = 'Distance ')

plt.show()
