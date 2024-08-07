import pandas as pd
from ydata_quality.labelling import LabelInspector

df = pd.read_csv(
    'C:/Users/ist.mevangelista/Documents/tcc/Datasets/Census/Census_50k.csv')

li = LabelInspector(df=df, label='workclass')
li = LabelInspector(df=df, label='education-num')

results = li.evaluate()
print(results)

# warnings = li.get_warnings()
# print(warnings)

# print(li.missing_labels())

# print(li.few_labels())

# print(li.one_vs_rest_performance(slack=0.1))

# print(li.unbalanced_classes(slack=0.3))

# print(li.outlier_detection(th=3))
