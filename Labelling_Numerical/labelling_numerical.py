import pandas as pd
from ydata_quality.labelling import LabelInspector

df = pd.read_csv('../../datasets/guerry_num_label.csv')
print(df.head())

li = LabelInspector(df=df, label='Donations', random_state=24)

results = li.evaluate()
print(results)

print(li.missing_labels())

print(li.outlier_detection(th=3))

print(li.outlier_detection(th=3, use_clusters=True))

print(li.test_normality())