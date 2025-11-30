import pandas as pd

# Чтение CSV файла
df = pd.read_csv('C:\Afbks\pppp.csv', sep=';')

# Добавление нового столбца с первыми 13 символами
df['new_column'] = df['cad_num'].str[:13]

# Группировка и подсчет количества
grouped = df.groupby(['new_column', 'koord']).size().reset_index(name='count')

# Сохранение результата
grouped.to_csv('C:\Afbks\grouped_result.csv', sep=';', index=False)

# Просмотр результата
print(grouped)