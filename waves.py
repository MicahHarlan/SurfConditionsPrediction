import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.preprocessing import LabelEncoder,PolynomialFeatures
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
np.set_printoptions(suppress=True)

df = pd.read_csv("waves.txt",sep=" ")
df = df.sort_values(by=['MM'])

bad_data = df[(df['WVHT'] == 99.0)].index
df.drop(bad_data, inplace=True)



#FEATURES
wave_height = df['WVHT']
wave_height_ft = []
count = 0


#for wave in wave_height:
#	if wave == 99.0:
#		count = count + 1
#	wave = wave * 3.28084
#	wave_height_ft.append(wave)
#df['WVHT'] = wave_height_ft



months = df['MM']
day = df['DD']


m = [0,1,2,3,4,5,6,7,8,9,10,12]
avg_height = []
order = df['MM'].value_counts()
order = order.sort_index()  
order = order.unique()
for a in range(len(order)):
	t = np.empty(order[a])
	num = order[a]
	i = 0
	while(i < num):
		t[i] = wave_height[a]
		i= i + 1
		a = a + 1
	mean = t.mean()
	avg_height.append(mean)
"""
avg_height = np.array(avg_height)
avg_height[np.isnan(avg_height)] = avg_height.mean()
avg_height = avg_height
plt.plot(m,avg_height)
plt.xlabel('Months')
plt.ylabel('Avg Height(m)')
plt.show()
"""
#tide = df['TIDE']



#Features For making a Decision Tree to predict wave height:
#NORM of all number Features
norm = MinMaxScaler(feature_range=(0,1))
norm_DPD = norm.fit_transform(df['DPD'].to_numpy().reshape(len(df['DPD']),1))
norm_APD = norm.fit_transform(df['APD'].to_numpy().reshape(len(df['APD']),1))
norm_MWD = norm.fit_transform(df['MWD'].to_numpy().reshape(len(df['MWD']),1))
norm_WTMP = norm.fit_transform(df['WTMP'].to_numpy().reshape(len(df['WTMP']),1))



#le = LabelEncoder()
#months = le.fit_transform(df['MM'])

y = []
for a in df['WVHT']:
	if a < 0.84:
		y.append(0)#('small')
	elif a > 0.84 and a <= 1.2:
		y.append(0) #('medium')
	else:
		y.append(1)#('large')  

#DECISION TREE
x = np.c_[norm_DPD,norm_APD,norm_MWD,norm_WTMP]
Xtrain, Xtest, ytrain, ytest = train_test_split(x,y,shuffle=True, test_size=.2)

rf = RandomForestClassifier(max_depth=5,random_state=1)#,#criterion='entropy')
rf.fit(Xtrain,ytrain)
scores = cross_val_score(rf, x, y, cv=5)
print(f"Cross validation mean score for Tree: {scores.mean():.4f}")

#NEAREST NEIGHBORS
kn = KNeighborsClassifier(n_neighbors=8)
Xtrain, Xtest, ytrain, ytest = train_test_split(x,y,shuffle=True, test_size=.2)
kn.fit(Xtrain,ytrain)
scores = cross_val_score(kn, x, y, cv=5)
print(f"Cross validation mean score for KNN: {scores.mean():.4f}")

#Naive Bayes
nb = GaussianNB()
Xtrain, Xtest, ytrain, ytest = train_test_split(x,y,shuffle=True, test_size=.2)
nb.fit(Xtrain,ytrain)
scores = cross_val_score(nb, x, y, cv=5)
print(f"Cross validation mean score for Naive Bayes: {scores.mean():.4f}")


#Voting Classifier:
vote = VotingClassifier(estimators=[('rf', rf), ('kn', kn), ('gnb', nb)], voting='hard')
Xtrain, Xtest, ytrain, ytest = train_test_split(x,y,shuffle=True, test_size=.2)
vote.fit(Xtrain,ytrain)
scores = cross_val_score(vote, x, y, cv=5)
print(f"Cross validation mean score for Voter: {scores.mean():.4f}")




