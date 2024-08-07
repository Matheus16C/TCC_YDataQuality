from ydata_quality.data_relations import DataRelationsDetector
import pandas as pd
import numpy as np

df = pd.read_csv(
    'C:/Users/ist.mevangelista/Documents/tcc/Datasets/Census/Census_50k.csv')

drd = DataRelationsDetector()


results = drd.evaluate(df, None, None)

warnings = drd.get_warnings()

print(warnings)

print(results)

# print(results['Confounders'])

# print(results['Colliders'])

# print(results['Feature Importance'])

# print(results['High Collinearity']['Categorical'])
