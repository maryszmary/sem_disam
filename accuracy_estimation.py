from sklearn.metrics import classification_report
import pandas as pd

FNAME = 'polnyj.measuring.result.csv'

df = pd.read_csv(FNAME, sep='\t')
result = list(df['result'])
golden_standard = list(df['golden_standard'])
print(classification_report(golden_standard, result))
