#Follow the instructions for what to code in this file.
from statistics import mean
table1=[18.1,15.4,19.0,13.4,10.2,13.1,18.1,14.4,15.0,10.8,5.4,12.2]
table2=[0.7,0.0,0.7,1.0,1.1,0.4,0.0,1.0,2.3,2.9,1.3]
mean1=mean(table1)
mean2=mean(table2)
print(f"Average mortality rate before hand washing policy:{mean1:.1f}")
print(f"Average mortality rate after hand washing policy:{mean2:.1f}")