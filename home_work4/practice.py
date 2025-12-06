"""
1) Открыть файл
2) Проанализировать
    а) на наличие пропусков (<..> NULL NONE EMPTY)
    б) признаки и их характер (признаки могут быть категориальные или численные)
3) Вывести первые н строк (полный вывод)
4) Вывести базовую статистику по любому столбцу (max min средние медианы моды и тд)
5) прочитать количество заголовков и количество строк в общем
вывод) вывести количество пропусков, заполнить пропуски в AGE средним
Numpy
1) сравнить 2 группы между собой (М и Ж)
    а) процент выживших
    б)средний возраст
    в) средний возраст выживших и погибших
2) Фильтрация
    ВЫБЕРИТЕ ВСЕХ ПАССАЖИРОВ
    а) возраст больше 30, мужчины, 1 класс
    б) моложе 18 или женщины, при этом выжили
    *в) сгрупировать по классу(Pclass) и полу(Sex) вычислить: средний возраст, доля выживших,средняя стоимость билета
3)сохранить файл
"""

import pandas as pd
import numpy as np

df=pd.read_csv('home_work4/tested.csv')
total_missing = df.isnull().sum().sum()
print(df.isnull().sum())
print("Всего пропусков:",total_missing)
print('')
print(df.dtypes)
print('')
print(df.head(10))
print('')
print(df['Age'].describe())
print('')
print("строки\столбцы")
print(df.shape)

print('')
print("Всего пропусков:",total_missing)
c=df['Age'].mean()
print(df['Age'].fillna(c))


survived = df['Survived'].values
sex = df['Sex'].values
age = df['Age'].values
pclass = df['Pclass'].values
fare = df['Fare'].values

# Сравнение М и Ж

male_mask = sex == 'male'
female_mask = sex == 'female'

# Процент выживших
male_survival_rate = np.mean(survived[male_mask]) * 100
female_survival_rate = np.mean(survived[female_mask]) * 100
m=np.sum(survived[male_mask])/np.sum(male_mask)
f=np.sum(survived[female_mask])/np.sum(female_mask)
print("   Мужчины: ",m)
print("   Женщины: ", f)

# Средний возраст
male_avg_age = np.mean(age[male_mask])
female_avg_age = np.mean(age[female_mask])

print("\n Средний возраст:")
print("   Мужчины: ", male_avg_age)
print("   Женщины: ", female_avg_age)

# возраст выживших и погибших
survived_mask = survived == 1
not_survived_mask = survived == 0

male_survived_age = np.mean(age[male_mask & survived_mask])
male_not_survived_age = np.mean(age[male_mask & not_survived_mask])
female_survived_age = np.mean(age[female_mask & survived_mask])
female_not_survived_age = np.mean(age[female_mask & not_survived_mask])

print("\n Средний возраст выживших и погибших:")
print(f"   Мужчины выжившие: {male_survived_age:.2f} лет")
print(f"   Мужчины погибшие: {male_not_survived_age:.2f} лет")
print(f"   Женщины выжившие: {female_survived_age:.2f} лет")
print(f"   Женщины погибшие: {female_not_survived_age:.2f} лет")

# 2) Фильтрация

#  Возраст больше 30, мужчины, 1 класс
mask_2a = (age > 30) & (sex == 'male') & (pclass == 1)
passengers_2a = df[mask_2a]
print(f"а) Пассажиры >30 лет, мужчины, 1 класс:")
print(f"   Найдено: {len(passengers_2a)} пассажиров")

#  Моложе 18 или женщины, при этом выжили
mask_2b = ((age < 18) | (sex == 'female')) & (survived == 1)
passengers_2b = df[mask_2b]
print(f"\nб) Пассажиры младше 18 ИЛИ женщины, которые выжили:")
print(f"   Найдено: {len(passengers_2b)} пассажиров")

# Группировка по классу и полу


#массив уникальных комбинаций класса и пола
unique_combinations = []
for p in [1, 2, 3]:
    for s in ['male', 'female']:
        unique_combinations.append((p, s))

print(f"{'Класс':<6} {'Пол':<8} {'Кол-во':<8} {'Ср. возраст':<12} {'Доля выживших':<15} {'Ср. стоимость':<12}")
print("-" * 70)

for pclass_val, sex_val in unique_combinations:
    mask_group = (pclass == pclass_val) & (sex == sex_val)
    
    if np.sum(mask_group) > 0:
        count = np.sum(mask_group)
        avg_age = np.mean(age[mask_group])
        survival_rate = np.mean(survived[mask_group]) * 100
        avg_fare = np.mean(fare[mask_group])
        
        print(f"{pclass_val:<6} {sex_val:<8} {count:<8} {avg_age:<12.2f} {survival_rate:<15.2f}% {avg_fare:<12.2f}")
    else:
        print(f"{pclass_val:<6} {sex_val:<8} {'0':<8} {'N/A':<12} {'N/A':<15} {'N/A':<12}")

# Дополнительный анализ - топ 10 самых дорогих билетов


top_10_expensive = df.nlargest(10, 'Fare')[['Name', 'Pclass', 'Sex', 'Age', 'Fare', 'Survived']]
print(top_10_expensive.to_string(index=False))



total_passengers = len(df)
survived_total = np.sum(survived)
survival_rate_total = (survived_total / total_passengers) * 100

print(f"Всего пассажиров: {total_passengers}")
print(f"Выжило: {survived_total} ({survival_rate_total:.2f}%)")
print(f"Погибло: {total_passengers - survived_total} ({(100 - survival_rate_total):.2f}%)")
