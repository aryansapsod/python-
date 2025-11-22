import pandas as pd

# df =pd.read_csv('C:\\Users\\DELL\\\\sales_data_sample.csv',encoding="latin1")
# print(df)

df =pd.read_excel("D:\\Book1.xlsx")
df =pd.DataFrame(df)
print('-'*120)
print(df)
df= pd.read_json("c:\\Users\\DELL\\Downloads\\sample_Data.json")
df =pd.DataFrame(df)
print('-'*120)

print(df)

df = pd.read_excel("D:\\Book1.xlsx")
df =pd.DataFrame(df)

print(df)
print('-'*120)

print(df.tail())
Data = {
    "Name":['Aryan','Rohit','Nitin','Raj','Amar'],
    "Age":[21,23,21,25,24],
    "City":["Latur","Pune",'Mumbai','Delhi','Murud']
}
df =pd.DataFrame(Data)
print(df)
print('-'*60)
Data = {
    "Name":['Aryan','Rohit','Nitin','Raj','Amar'],
    "Age":[21,23,21,25,24],
    "City":["Latur","Pune",'Mumbai','Delhi','Murud']
}
df =pd.DataFrame(Data)
print(df)
print('-'*120)