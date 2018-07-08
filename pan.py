#1
import pandas as pd
data=[['abc',20,'abc@gmail.com',34354657],
    ['apa',21,'apa@gmail.com',2223665]]
dataframe=pd.DataFrame(data=data,columns=['Name','Age','Mail_id','Phone_no'])
print(dataframe)

#2
import pandas as pd
df=pd.read_csv(("https://raw.githubusercontent.com/Shreyas3108/Weather/master/weather.csv"))
a=df.head(5)
print(a)

b=df.head(10)
print(b)

c=df.describe()
print(c)