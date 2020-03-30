import pandas as pd
import numpy as np
import re
pd.set_option('display.max_columns', None)

recipes = pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DS0103EN/labs/data/recipes.csv')
print('Data read to dataframe!')

ingredients = list(recipes.columns.values)

print([match.group(0) for ingredient in ingredients for match in [(re.compile(".*(rice).*")).search(ingredient)] if match])
print([match.group(0) for ingredient in ingredients for match in [(re.compile(".*(wasabi).*")).search(ingredient)] if match])
print([match.group(0) for ingredient in ingredients for match in [(re.compile(".*(soy).*")).search(ingredient)] if match])

recipes['country'].value_counts()

column_name = recipes.columns.values
column_name[0] = 'cuisine'
recipes.columns = column_name

recipes['cuisine'] = recipes['cuisine'].str.lower()

recipes.loc[recipes["cuisine"] == "austria", "cuisine"] = "austrian"
recipes.loc[recipes["cuisine"] == "belgium", "cuisine"] = "belgian"
recipes.loc[recipes["cuisine"] == "china", "cuisine"] = "chinese"
recipes.loc[recipes["cuisine"] == "canada", "cuisine"] = "canadian"
recipes.loc[recipes["cuisine"] == "netherlands", "cuisine"] = "dutch"
recipes.loc[recipes["cuisine"] == "france", "cuisine"] = "french"
recipes.loc[recipes["cuisine"] == "germany", "cuisine"] = "german"
recipes.loc[recipes["cuisine"] == "india", "cuisine"] = "indian"
recipes.loc[recipes["cuisine"] == "indonesia", "cuisine"] = "indonesian"
recipes.loc[recipes["cuisine"] == "iran", "cuisine"] = "iranian"
recipes.loc[recipes["cuisine"] == "italy", "cuisine"] = "italian"
recipes.loc[recipes["cuisine"] == "japan", "cuisine"] = "japanese"
recipes.loc[recipes["cuisine"] == "israel", "cuisine"] = "jewish"
recipes.loc[recipes["cuisine"] == "korea", "cuisine"] = "korean"
recipes.loc[recipes["cuisine"] == "lebanon", "cuisine"] = "lebanese"
recipes.loc[recipes["cuisine"] == "malaysia", "cuisine"] = "malaysian"
recipes.loc[recipes["cuisine"] == "mexico", "cuisine"] = "mexican"
recipes.loc[recipes["cuisine"] == "pakistan", "cuisine"] = "pakistani"
recipes.loc[recipes["cuisine"] == "philippines", "cuisine"] = "philippine"
recipes.loc[recipes["cuisine"] == "scandinavia", "cuisine"] = "scandinavian"
recipes.loc[recipes["cuisine"] == "spain", "cuisine"] = "spanish_portuguese"
recipes.loc[recipes["cuisine"] == "portugal", "cuisine"] = "spanish_portuguese"
recipes.loc[recipes["cuisine"] == "switzerland", "cuisine"] = "swiss"
recipes.loc[recipes["cuisine"] == "thailand", "cuisine"] = "thai"
recipes.loc[recipes["cuisine"] == "turkey", "cuisine"] = "turkish"
recipes.loc[recipes["cuisine"] == "vietnam", "cuisine"] = "vietnamese"
recipes.loc[recipes["cuisine"] == "uk-and-ireland", "cuisine"] = "uk-and-irish"
recipes.loc[recipes["cuisine"] == "irish", "cuisine"] = "uk-and-irish"

recipes_counts = recipes['cuisine'].value_counts()
cuisines_indices = recipes_counts > 50

cuisines_to_keep = list(np.array(recipes_counts.index.values)[np.array(cuisines_indices)])

rows_before = recipes.shape[0]
print('Number of rows of original dataframe is{}'.format(rows_before))
recipes = recipes.loc[recipes['cuisine'].isin(cuisines_to_keep)]
rows_after = recipes.shape[0]
print('number of rows of proceed datasheet is {}'.format(rows_after))
print('rows remowed{}'.format(rows_before - rows_after))

recipes = recipes.replace(to_replace='Yes', value=1)
recipes = recipes.replace(to_replace='No', value=0)

check_recipes = recipes.loc[
    (recipes ['rice'] == 1 ) &
    (recipes ['soy_sauce'] == 1) &
    (recipes ['wasabi'] == 1) &
    (recipes ['seaweed'] == 1)
]

check_recipes

ing = recipes.iloc[:, 1:].sum(axis=0)

ingredients = pd.Series(ing.index.values, index=np.arange(len(ing)))
count = pd.Series(list(ing), index=np.arange(len(ing)))

ing_dif = pd.DataFrame(dict(ingredients = ingredients, count = count))
ing_dif = ing_dif[['ingredients', 'count']]

print(ing_dif.to_string())

ing_dif.sort_values(['count'], ascending = False, inplace = True)
ing_dif.reset_index(inplace = True, drop = True)

print(ing_dif)

cuisines = recipes.groupby('cuisine').mean()
cuisines.head()

num_ingridients = 4

def print_ingridients(row):
    print(row.name.upper())
    row_sorted = row.sort_values(ascending = False)*100
    top_ingridients = list(row_sorted.index.values)[0:num_ingridients]
    row_sorted = list(row_sorted)[0:num_ingridients]
    
    for ind, ingridient in enumerate(top_ingridients):
        print("%s (%d%%)" % (ingridient, row_sorted[ind]), end=' ')
    print('\n')
    
    
crerate_cuisines_profile = cuisines.apply(print_ingridients, axis=1)
