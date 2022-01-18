
### csv파일은 txt파일로 변환 ###
import pandas as pd
df = pd.read_excel('wellness_dialog_dataset.xlsx')
print(df)
df.to_csv('wellness_dialog_dataset.txt', index=False)