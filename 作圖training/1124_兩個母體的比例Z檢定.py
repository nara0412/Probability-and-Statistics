from scipy.stats import norm
import numpy as np

office_1_data = (35 , 250) #例如office 1 有35次成功 嘗試250次
office_2_data = (27 , 300) #例如office 2 有27次成功 嘗試300次

p1 = office_1_data[0] / office_1_data[1]
p2 = office_2_data[0] / office_2_data[1]

pooled_p = (office_1_data[0] + office_2_data[0]) / (office_1_data[1] + office_2_data[1])

z_score = (p1 - p2) / np.sqrt(pooled_p * (1 - pooled_p) * (1 / office_1_data[1] + 1 / office_2_data[1]))

p_value = norm.sf(abs(z_score)) * 2

print(z_score)
print(p_value)
