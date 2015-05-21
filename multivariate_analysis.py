import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
loanData = pd.read_csv('LoanStats3.csv', header=1)
InterestRate = loanData['int_rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loanData['int_rate'] = InterestRate
def T_F(dt):
	if (dt) == "OWN":
		return 1
	else:
		return 0
loanData['home_ownership'] = loanData['home_ownership'].apply(T_F)
X = loanData[['annual_inc','home_ownership']]
y = loanData['int_rate']
X = sm.add_constant(X)
#est = sm.OLS(y, X).fit()
est = smf.ols(formula='int_rate ~ annual_inc * home_ownership', data=loanData).fit()
print est.summary()
