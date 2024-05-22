# ETL. Procesamiento de datos de demanda de energía 

import pandas as pd
import os
from datetime import datetime

processed_path = 'data/processed/processed_data_energy.csv'
processed_path_supervised = 'data/processed/supervised_data_energy.csv'
raw_path = 'data/raw/Dataset_GCRNO.csv'
folder_path_log='logs/processed'

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


def log_error_write(description, line):
    # Verificando si la carpeta existe, si no, crearla
    if not os.path.exists(folder_path_log):
        os.makedirs(folder_path_log)

    date_now = datetime.now()

    # Variable que contiene el texto que tendrá el archivo txt que se generará y descargará.
    line_error = f"""{date_now.strftime('%Y-%m-%d %H:%M:%S')} {line} - {description}"""
    # Se crea el archivo a partir del texto de arriba, el cual se guardará con el nombre descriptivo más la fecha día*mes*año, para identificar la descarga por día.
    with open(f'{folder_path_log}/log_err_{date_now.strftime("%d%m%y")}.txt', 'a', encoding="utf-8") as error_file:
        error_file.write(f"\n{line_error}")

def log_write(description, line):
    # Verificando si la carpeta existe, si no, crearla
    if not os.path.exists(folder_path_log):
        os.makedirs(folder_path_log)

    date_now = datetime.now()

    # Variable que contiene el texto que tendrá el archivo txt que se generará y descargará.
    line_write = f"""{date_now.strftime('%Y-%m-%d %H:%M:%S')} {line} - {description}"""
    # Se crea el archivo a partir del texto de arriba, el cual se guardará con el nombre descriptivo más la fecha día*mes*año, para identificar la descarga por día.
    with open(f'{folder_path_log}/log_{date_now.strftime("%d%m%y")}.txt', 'a', encoding="utf-8") as write_file:
        write_file.write(f"\n{line_write}")

def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
   """
   Frame a time series as a supervised learning dataset.
   Arguments:
   data: Sequence of observations as a list or NumPy array.
   n_in: Number of lag observations as input (X).
   n_out: Number of observations as output (y).
   """
   df = pd.DataFrame(data)
   col_names = df.columns
   cols, names = list(), list()
   # input sequence (t-n, ... t-1)
   for i in range(n_in, 0, -1):
      cols.append(df.shift(i))
      names += [(f'{col}(t-{i})') for col in col_names]
   # forecast sequence (t, t+1, ... t+n)
   for i in range(0, n_out):
      cols.append(df.shift(-i))
   if i == 0:
      names += [(f'{col}(t)') for col in col_names]
   else:
      names += [(f'{col}(t+{i})') for col in col_names]
   # put it all together
   agg = pd.concat(cols, axis=1)
   agg.columns = names
   # drop rows with NaN values
   if dropnan:
      agg.dropna(inplace=True)
   return agg

try:
    log_write('Inicio de proceso','ETL')
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

    supervised_data = series_to_supervised(df_final[df_final.columns[4:]], n_in = 12, n_out = 1)

    supervised_data.to_csv(processed_path_supervised, index = False)

    log_write('Fin de proceso exitoso - creado processed_data_energy.csv y supervised_data_energy','ETL')
except Exception as e:
    log_error_write(f"Error ejecucion: {e}", 'Proceso ETL Energy Demand')

