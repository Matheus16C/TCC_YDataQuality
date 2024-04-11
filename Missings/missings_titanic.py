from ydata_quality.missings import MissingsProfiler
from ydata_quality.core import QualityWarning
import pandas as pd

df = pd.read_csv('Titanic.csv', engine='python')

mp = MissingsProfiler(df=df)

results = mp.evaluate()
print(results)
warnings = mp.get_warnings()
print(warnings)

# print(mp.null_count())

# print(mp.nulls_higher_than(th=0.1))

# print(mp.missing_correlations())

# print(mp.high_missing_correlations(th=0.8))

# print(mp.predict_missings(['so', 'lg']))

# print(mp.predict_missings())

# mp.label = 'ab'
# print(mp.performance_drop(normalize=True))

# new_warning = QualityWarning(
#     category='Missings',
#     test='Performance Drop',
#     description='Found severe  differences in performance between missing and non-missing feature values.',
#     priority=2, # 0 critical, 1 heavy, 2 medium, 3 minor
#     data=mp.performance_drop(normalize=True),
# )

# print(mp.store_warning(new_warning))

# perf_drop_warnings = mp.get_warnings(test='Performance Drop')
# print(perf_drop_warnings)
