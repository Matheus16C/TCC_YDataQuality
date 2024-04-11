from ydata_quality.data_relations import DataRelationsDetector
import pandas as pd
import numpy as np
from sklearn.datasets import load_boston

boston = load_boston()

print(boston.feature_names);
df = pd.DataFrame(boston.data, columns=boston.feature_names)

drd = DataRelationsDetector()


results = drd.evaluate(df)

warnings = drd.get_warnings()

print(warnings)

print(results)

# print(results['Confounders'])

# print(results['Colliders'])

# print(results['Feature Importance'])

# print(results['High Collinearity']['Categorical'])
