# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
print(data)
cencus=np.concatenate((data,new_record),axis=0)
print(cencus.shape)
age=cencus[:,0]
max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)
print(max_age,min_age,age_mean,age_std)
race=cencus[:,2]
race_0=race[race==0]
race_1=race[race==1]
race_2=race[race==2]
race_3=race[race==3]
race_4=race[race==4]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
len_list=[len_0,len_1,len_2,len_3,len_4]
np.min(len_list)
minority_race=np.argmin(len_list)
print(minority_race)
senior_citizens=age[age>60]
working_hours_sum=sum(cencus[:,6][age>60])
print(working_hours_sum)
avg_working_hours=working_hours_sum/len(senior_citizens)
print(avg_working_hours)

education=cencus[:,1]
high=education[education>10]
low=education[education<=10]
income=cencus[:,7]
avg_pay_high=sum(income[education>10])/len(high)
print(avg_pay_high)
avg_pay_low=sum(income[education<=10])/len(low)
print(avg_pay_low)                                                                                                                                                                                                                                                                         


