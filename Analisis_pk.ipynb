import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pokemon.csv")

df.shape
df.info()

#Se quitan las resistencias de tipos por ahora

resistence = ['against_bug', 'against_dark', 'against_dragon', 'against_electric', 
              'against_fairy', 'against_fight', 'against_fire', 'against_flying', 
              'against_ghost', 'against_grass', 'against_ground', 'against_ice', 
              'against_normal', 'against_poison', 'against_psychic', 'against_rock', 
              'against_steel', 'against_water']

df_pk = df.drop(columns = resistence)

#Eliminar nombre en japones y clasificación. Son irrelevantes

df_pk = df_pk.drop(columns = ['japanese_name', 'classfication'])

df_pk.info()

#Se organizan las columnas

df_pk = df_pk.reindex(columns=['pokedex_number', 'name', 'type1','type2', 'percentage_male','height_m',
                               'weight_kg', 'base_egg_steps', 'base_happiness',
                               'capture_rate', 'experience_growth', 'generation', 'is_legendary', 
                               'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed','base_total', 'abilities'])


#Análisis de nulos

def nulos(df):
  na_sum = df.isnull().sum()
  na_ratio = ((na_sum/len(df)) * 100)#.sort_values(ascending = False)
  col_type = df.dtypes
  nunique = df.nunique()
  nulls = pd.DataFrame(data = {'Num_nulos':na_sum, 'Ratio_nulos':na_ratio, 'Col_type':col_type, 'Nunique_values':nunique}) #.reset_index()
  return nulls

nulos(df_pk)

#El segundo tipo se cambia por none ya que significa que no tiene tipo secundario El porcentaje de macho se cambia a 0 porque significa que no puede ser macho

df_pk['type2'] = df_pk['type2'].fillna('None')
df_pk['percentage_male'] = df_pk['percentage_male'].fillna(0)

#La altura y el peso no son tan importantes y eliminar las filas quitaria analisis en otras columnas. Se pone en 0 y no sería un cambio tan significante

df_pk['height_m'] = df_pk['height_m'].fillna(0)
df_pk['weight_kg'] = df_pk['weight_kg'].fillna(0)

nulos(df_pk)

#Análisis varios
#Peso

df_pk.groupby('generation')['weight_kg'].sum()

df_pk.groupby('type1')['weight_kg'].sum().sort_values(ascending=False)

df_pk.groupby('type2')['weight_kg'].sum().sort_values(ascending=False)

#Altura

df_pk.groupby('generation')['height_m'].sum()

df_pk.groupby('type1')['height_m'].sum().sort_values(ascending=False)

df_pk.groupby('type2')['height_m'].sum().sort_values(ascending=False)

#Tipos
#Tipo primario

suma_tipos_por_generacion = df_pk.groupby('generation')['type1'].value_counts()

df_tipos_por_generacion = suma_tipos_por_generacion.to_frame(name='Count').reset_index()

plt.figure(figsize=(15, 6))
ax = plt.gca()
df_tipos_por_generacion.pivot('generation', 'type1', 'Count').plot(kind='bar', ax=ax)
plt.xlabel('Generación')
plt.ylabel('Cantidad')
plt.title('Cantidad de Tipos Primario por Generación')
plt.legend(title='Tipo')
plt.show()


#Tipo puro por gen

puro = df_pk['type2'] != 'None'
df_puro = df_pk.drop(df_pk[puro].index)

suma_tipos_por_generacion = df_puro.groupby('generation')['type1'].value_counts()

df_tipos_por_generacion = suma_tipos_por_generacion.to_frame(name='Count').reset_index()

plt.figure(figsize=(15, 6))
ax = plt.gca()
df_tipos_por_generacion.pivot('generation', 'type1', 'Count').plot(kind='bar', ax=ax)
plt.xlabel('Generación')
plt.ylabel('Cantidad')
plt.title('Cantidad de Tipos Puro por Generación')
plt.legend(title='Tipo')
plt.show()

#Tipo secundario

suma_tipos_por_generacion = df_pk.groupby('generation')['type2'].value_counts()

df_tipos_por_generacion = suma_tipos_por_generacion.to_frame(name='Count').reset_index()

plt.figure(figsize=(15, 6))
ax = plt.gca()
df_tipos_por_generacion.pivot('generation', 'type2', 'Count').plot(kind='bar', ax=ax)
plt.xlabel('Generación')
plt.ylabel('Cantidad')
plt.title('Cantidad de Tipos Secundarios por Generación')
plt.legend(title='Tipo')
plt.show()

#El tipo puro es bastante más contundente asi que se quitan para ver mejor los tipos secundarios

secun = df_pk['type2'] == 'None'
df_secun = df_pk.drop(df_pk[secun].index)

suma_tipos_por_generacion = df_secun.groupby('generation')['type2'].value_counts()

df_tipos_por_generacion = suma_tipos_por_generacion.to_frame(name='Count').reset_index()

plt.figure(figsize=(15, 6))
ax = plt.gca()
df_tipos_por_generacion.pivot('generation', 'type2', 'Count').plot(kind='bar', ax=ax)
plt.xlabel('Generación')
plt.ylabel('Cantidad')
plt.title('Cantidad de Tipos Secundarios por Generación')
plt.legend(title='Tipo')
plt.show()

