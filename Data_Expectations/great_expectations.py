import pandas as pd

from ydata_quality.data_expectations import DataExpectationsReporter

df = pd.read_csv('../../datasets/taxi_yellow_tripdata_sample_2019-01.csv')
results_json_path = '../../datasets/taxi_long.json'

der = DataExpectationsReporter()

results = der.evaluate(results_json_path, df)

print(results)

warnings = der.get_warnings()
print(warnings[0])

print(list(results.keys()))

failed_expectations_ids = results['Overall Assessment']
print(failed_expectations_ids)

coverage_fraction = results['Coverage Fraction']
print(coverage_fraction)

expectations_report, expectations_dense = results['Expectation Level Assessment']
print(expectations_report)

print(expectations_dense[0])

