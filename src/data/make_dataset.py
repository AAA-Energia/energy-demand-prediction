# ETL. Procesamiento de datos de demanda de energía 

import pandas as pd

processed_path = 'data/processed/processed_data_energy.csv'
raw_path = 'data/raw/Dataset_GCRNO.csv'

# Diccionario para meses
dict_mes = {'ene':'01',
            'feb':'02',
            'mar':'03',
            'abr':'04',
            'may':'05',
            'jun':'06',
            'jul':'07',
            'ago':'08',
            'sep':'09',
            'oct':'10',
            'nov':'11',
            'dic':'12'
        }

# Leemos el csv
df = pd.read_csv(raw_path)

# Escribimos con minúscula los nombres de las columnas o características
df.columns = map(str.lower, df.columns)

# 
df['fecha'] = df['fecha'].replace(dict_mes, regex=True)
df['fecha'] = df['fecha'].apply(lambda x: x[0:6] + '20' + x[6:])
df['fecha']= pd.to_datetime(df['fecha'], format='%d-%m-%Y')


df['dia'] = pd.DatetimeIndex(df['fecha']).day
df['mes'] = pd.DatetimeIndex(df['fecha']).month
df['anio'] = pd.DatetimeIndex(df['fecha']).year

columnas_horas = [f'dem_gcrno_h{i}' for i in range(24)]

df_long = df.melt(id_vars='fecha', value_vars=columnas_horas,
                  var_name='hora', value_name='demanda_energia')

df_long['hora'] = df_long['hora'].str.extract('(\d+)').astype(int)
df_long = df_long.sort_values(by=['fecha', 'hora']).reset_index(drop=True)

df_combined = df_long.merge(df, on=['fecha'])

df_combined = df_combined.drop(columns=columnas_horas)

df_combined.drop(columns=['fecha'], inplace = True)

columns = df_combined.columns
ordered_columns = list([columns[0]]) + list(columns[-3:]) + list(columns[2:26]) + list([columns[1]])
df_final = df_combined[ordered_columns]

df_final.to_csv(processed_path, index = False)