import pandas as pd
from ydata_quality import DataQuality
from ydata_quality.data_expectations import DataExpectationsReporter

df = pd.read_csv('Titanic.csv')
results_json_path = 'titanic_results.json'

dq = DataExpectationsReporter()

results = dq.evaluate(results_json_path, df)

warnings = dq.get_warnings()
print(warnings)

print(list(results.keys()))

failed_expectations_ids = results['Overall Assessment']
print(failed_expectations_ids)

coverage_fraction = results['Coverage Fraction']
print(coverage_fraction)

expectations_report, expectations_dense = results['Expectation Level Assessment']
print(expectations_report)

print(expectations_dense[0])
