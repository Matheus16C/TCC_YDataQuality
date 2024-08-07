import pandas as pd
from ydata_quality.duplicates import DuplicateChecker

df = pd.read_csv(
    'C:/Users/ist.mevangelista/Documents/tcc/Datasets/Census/Census_50k.csv')

dc = DuplicateChecker(df=df)

results = dc.evaluate()
print(results.keys())

warnings = dc.get_warnings()
print(warnings)

# exact_duplicates_out = dc.exact_duplicates()
# print(exact_duplicates_out.head())

# given_entity_duplicates_out = dc.entity_duplicates('MainCity')

# dc.entities = ['Region']
# entity_duplicates_out = dc.entity_duplicates()

# dc.entities = []
# print(dc.entity_duplicates())

# dc.entities = [['Region', 'MainCity']]
# composed_entity_duplicates_out = dc.entity_duplicates()

# print(dc.duplicate_columns())
