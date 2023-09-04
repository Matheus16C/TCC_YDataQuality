from ydata_quality.data_relations import DataRelationsDetector
import pandas as pd

df = pd.read_csv('../../datasets/census_10k.csv')
df.drop(columns=['education-num'], inplace=True)

drd = DataRelationsDetector()


results = drd.evaluate(df, None, 'income')

warnings = drd.get_warnings()

print(warnings)

print(results['Confounders'])

print(results['Colliders'])

print(results['Feature Importance'])

print(results['High Collinearity']['Categorical'])
