from scipy.stats import chi2

df = 19 #自由度
alpha = 0.025

#卡方值
chi_square_value = chi2.isf(alpha, df)
print(chi_square_value)

#卡方值的右邊面積
p_value = chi2.sf(chi_square_value, df)
print(p_value)


#若alpha = 0.975時
alpha = 0.975

#卡方值
chi_square_value = chi2.isf(alpha, df)
print(chi_square_value)

#卡方值的右邊面積
p_value = chi2.sf(chi_square_value, df)
print(p_value)