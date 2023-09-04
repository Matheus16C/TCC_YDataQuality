import pandas as pd
import numpy as np
from ydata_quality.erroneous_data import ErroneousDataIdentifier

df = pd.read_csv('../../datasets//macrodata.csv', index_col='YearQuarter', parse_dates=True)
print(df.head(5))

edv_extensions = ['a_custom_edv', 999999999, '!', '', 'UNKNOWN']
edi = ErroneousDataIdentifier(df=df, ed_extensions=edv_extensions)

results = edi.evaluate()
print(results)

warnings = edi.get_warnings()
print(warnings)

flatlines_out = edi.flatlines(th=4)
print(flatlines_out['realdpi'])

print(edi.predefined_erroneous_data())