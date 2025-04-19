import pandas as pd
import statsmodels.api as sm

# Replace 'data' with your actual DataFrame
# Assuming 'data' has two columns: 'IndependentVar' and 'DependentVar'

# Sample data creation for demonstration (please use your actual data instead)
data = pd.DataFrame({
    'IndependentVar': [1, 2, 3, 4, 5],  # Independent variable (e.g., time, temperature)
    'DependentVar': [2, 3, 4, 5, 6]     # Dependent variable (e.g., sales, pressure)
})

# Ordinary Least Squares (OLS) regression
# Add a constant to the independent variable to represent the intercept
X = sm.add_constant(data['IndependentVar'])
y = data['DependentVar']

# Fit the regression model
model = sm.OLS(y, X).fit()

# Print out the statistics
model_summary = model.summary()
print(model_summary)
