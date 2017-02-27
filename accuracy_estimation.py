from sklearn.metrics import classification_report
import pandas as pd

FNAME = 'myagk.measuring.result.csv'

df = pd.read_csv('myagk.measuring.result.csv', sep='\t')
result = [v if v else '' for v in df['result']]
golden_standard = [v if v else '' for v in df['golden_standard']]
print(classification_report(golden_standard, result))
# print(list(df['result']))