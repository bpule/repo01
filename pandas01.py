# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 19:23:56 2024

@author: BPule
"""
#Manipulating Excel files using the panda library
import pandas
file = pandas.read_csv("country_data.csv")
print(file.info())
print(file.describe())
#Panda practice
#Storing Data
B1 = 30
B2 = 40
B3 = 30
B4 = 49
B5 = 22
B6 = 35
B7 = 22
B8 = 46
B9 = 29
B10 =25
B11 = 39
print(B1)
print(B2)
print(B3)
print(B4)
print(B5)
print(B6)
print(B7)
print(B8)
print(B9)
print(B10)
print(B11)
#Using Lists to store data
age = [30,40,30,49,22,35,22,46,29,25,39]
print(age)
#Lists indexes (aka positions/locations) start at 0 which has the value of 30
print(age[0])
print(age[1])
print(age[10])
print(min(age))
print(max(age))
"""
49
"""
print(len(age))
"""
11
"""
print(sum(age))
"""
367
"""
average = sum(age)/len(age)
print(average)
"""
33.36363636363637
"""
file = pandas.read_csv("diab_data.csv")
print(file.info())
"""
RangeIndex: 768 entries, 0 to 767
Data columns (total 9 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   preg_count  768 non-null    int64  
 1   glucose     768 non-null    int64  
 2   bp          768 non-null    int64  
 3   skinfold    768 non-null    int64  
 4   insulin     768 non-null    int64  
 5   BMI         768 non-null    float64
 6   predigree   768 non-null    float64
 7   age         768 non-null    int64  
 8   class       768 non-null    int64  
dtypes: float64(2), int64(7)
memory usage: 54.1 KB
"""
print(file.describe())
"""
preg_count     glucose          bp  ...   predigree         age       class
count  768.000000  768.000000  768.000000  ...  768.000000  768.000000  768.000000
mean     3.845052  120.894531   69.105469  ...    0.471876   33.240885    0.348958
std      3.369578   31.972618   19.355807  ...    0.331329   11.760232    0.476951
min      0.000000    0.000000    0.000000  ...    0.078000   21.000000    0.000000
25%      1.000000   99.000000   62.000000  ...    0.243750   24.000000    0.000000
50%      3.000000  117.000000   72.000000  ...    0.372500   29.000000    0.000000
75%      6.000000  140.250000   80.000000  ...    0.626250   41.000000    1.000000
max     17.000000  199.000000  122.000000  ...    2.420000   81.000000    1.000000

[8 rows x 9 columns]
"""
column_names = ["A","B","C"]
file = pandas.read_csv("housing_data.csv", names=column_names)
print(file.info())
"""
RangeIndex: 505 entries, 0 to 504
Data columns (total 14 columns):
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   0.00632  505 non-null    float64
 1   18       505 non-null    float64
 2   2.31     505 non-null    float64
 3   0        505 non-null    float64
 4   0.538    505 non-null    float64
 5   6.575    505 non-null    float64
 6   65.2     505 non-null    float64
 7   4.09     505 non-null    float64
 8   1        505 non-null    int64  
 9   296      505 non-null    float64
 10  15.3     505 non-null    float64
 11  396.9    505 non-null    float64
 12  4.98     505 non-null    float64
 13  24       451 non-null    float64
dtypes: float64(13), int64(1)
memory usage: 55.4 KB
None
"""
print(file.describe())
"""
          0.00632          18        2.31  ...       396.9        4.98          24
count  505.000000  505.000000  505.000000  ...  505.000000  505.000000  451.000000
mean     1.271696   13.285941    9.218812  ...  332.664158   11.550792   23.749889
std      2.400926   23.070598    7.170151  ...  125.414151    6.063900    8.818376
min      0.000000    0.000000    0.000000  ...    0.320000    1.730000    6.300000
25%      0.049810    0.000000    3.440000  ...  364.610000    6.900000   18.500000
50%      0.144760    0.000000    6.960000  ...  390.640000   10.400000   21.900000
75%      0.825260   18.100000   18.100000  ...  395.600000   15.020000   26.600000
max      9.966540  100.000000   27.740000  ...  396.900000   34.410000   50.000000

[8 rows x 14 columns]
"""
file = pandas.read_csv("iris.csv")
print(file.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   sepal_length  150 non-null    float64
 1   sepal_width   150 non-null    float64
 2   petal_length  150 non-null    float64
 3   petal_width   150 non-null    float64
 4   species       150 non-null    object 
dtypes: float64(4), object(1)
memory usage: 6.0+ KB
None
"""
print(file.describe())
"""
       sepal_length  sepal_width  petal_length  petal_width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000
"""
file = pandas.read_csv("insurance_data.csv",skiprows=5)
#Skiprows is used to exclude rows that are not compatible with Python e.g metadata, giving additional information
print(file)
"""
      X      Y
0   108  392.5
1    19   46.2
2    13   15.7
3   124  422.2
4    40  119.4
..  ...    ...
58    9   87.4
59   31  209.8
60   14   95.5
61   53  244.6
62   26  187.5

[63 rows x 2 columns]
"""
print(file.describe())
"""
                X           Y
count   63.000000   63.000000
mean    22.904762   98.187302
std     23.351946   87.327553
min      0.000000    0.000000
25%      7.500000   38.850000
50%     14.000000   73.400000
75%     29.000000  140.000000
max    124.000000  422.200000
"""
"""
Storing data
1. Lists,use []
2. Dictionaries
3. Data frames - specific to pandas
"""
file = pandas.read_csv("country_data.csv")
print(file)
"""
                X           Y
count   63.000000   63.000000
mean    22.904762   98.187302
std     23.351946   87.327553
min      0.000000    0.000000
25%      7.500000   38.850000
50%     14.000000   73.400000
75%     29.000000  140.000000
max    124.000000  422.200000
    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
"""
file = pandas.read_csv("country_data.csv")
#Storing text
C2="M"
C3="M"
C4="F"
print(C2)
"""
M
"""
#gender list
gender =["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
"""
M
"""
print(gender[1])
print(gender[2])
#A nice feature of Python is that you can access the last value in the list by setting the index = -1.
print(gender[-1])
#country list
country = ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
print(country)
"""
['South Africa', 'Botswana', 'South Africa', 'South Africa', 'Kenya', 'Mozambique', 'Lesotho', 'Kenya', 'Kenya', 'Egypt', 'Sudan']
"""
print (country[0])
"""
South Africa
"""
print (country[5])
"""
Mozambique
"""
"""
We can do many things with lists:

print all the items in the list using [:]
we can add items to the end of the list using append()
add items at specific positions using insert()
remove an item from the list using the remove() function
check how many variables are in the list using the len()
print a range of values using [start:end] – just like in excel!
"""
my_list = [42, -2021, 6.283, "tau", "node"]
print(my_list)
print(my_list[:])
my_list.append("pi")
print(my_list)
my_list.insert(1,"pi2")
print(my_list)
my_list.remove("pi")
print(my_list)
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)
print(len(my_list))
#View a certain range of items:
print(my_list[0:3])
"""
The command print(my_list[0:3]) outputs three variables (42, -2021, 6.283) instead of four because of the way Python handles slicing.
In Python, when you use the notation, it includes elements starting from the start index up to, BUT NOT INCLUDING, the element at the stop index.

The fourth value is not included because the last index is 3 - 1. So values from 0 to 3 - 1 = 2 are included.
"""
#Dictionaries
"""
A dictionary in Python is a collection of key-value pairs, where each key is unique. Dictionaries are also known as associative arrays or hash maps. They are similar to lists, but instead of using integer indices to access elements, you use keys. It is an unordered data type that is structured using keys and values and is defined with curly brackets {}. Where keys are like the column names and values are the lists of data.
"""
person = {'name': 'Boitumelo Maboko', 'age': 41, 'address': '337 Kersboom'}
print(person['name'])
print(person.get('age'))
print(person['address'])
print(person['age'])
#DataFrame
import pandas as pd
data = {'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39], 'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"], 'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]}
df = pd.DataFrame(data)
print(df)
print(df['age'])
print(df['gender'])
print(df['age'].min())
"""
22
"""
print(df['age'].max())
"""
49
"""
print(df['age'].mean())
"""
33.36363636363637
"""
#Filtering data in DataFrame
print(df[df['age']>30])
"""
    age gender       country
1    40      M      Botswana
3    49      M  South Africa
5    35      F    Mozambique
7    46      M         Kenya
10   39      M         Sudan
"""
#Slicing rows and columns
print(df[1:4])
"""
   age gender       country
1   40      M      Botswana
2   30      F  South Africa
3   49      M  South Africa
"""
#Adding a new column
df['new_column'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(df)
"""
    age gender       country  new_column
0    30      M  South Africa           1
1    40      M      Botswana           2
2    30      F  South Africa           3
3    49      M  South Africa           4
4    22      F         Kenya           5
5    35      F    Mozambique           6
6    22      F       Lesotho           7
7    46      M         Kenya           8
8    29      M         Kenya           9
9    25      F         Egypt          10
10   39      M         Sudan          11
"""
df.drop(columns=["new_column]), inplace=True)