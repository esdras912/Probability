
import pandas as pd
import itertools
import numpy as np
df = pd.read_csv('data0.csv')
df2 = pd.read_csv('data.csv')


df = df2[(df2['YEAR'] == 2021)]

R1 = [number for number in df.R1]
R2 = [number for number in df.R2]
R3 = [number for number in df.R3]
R4 = [number for number in df.R4]
R5 = [number for number in df.R5]
series = []

for num in range(len(R1)):
    series.append([])
    series[num].append(R1[num])
    series[num].append(R2[num])
    series[num].append(R3[num])
    series[num].append(R4[num])
    series[num].append(R5[num])


df['SERIE'] = series


numbers = [i for i in range(1,29)]

combinations = [combination for combination in itertools.combinations(numbers,2)]


years = [int(year.split('/')[2]) for year in np.array(df.FECHA)]
month = [int(year.split('/')[1]) for year in np.array(df.FECHA)]
day = [int(year.split('/')[0]) for year in np.array(df.FECHA)]

df['YEAR'] = years; df['MONTH'] = month; df['DAY'] = day
csv = df.to_csv()


iter_combinations = 0
iter_series = 0
inter_iter = 0
events_checked = False
combination_Numbers_compared = False
combinations_ammount = {}
process = False
progress_true = 0 # cantidad de numeros iguales entre una combinación y una serie si esta variable es igual
                              # a la longitud de la combinación significa que todos los numeros de esta están en la serie

current_succesfull_events = 0

while process == False:
    try:
        current_combination = combinations[iter_combinations]
        
    except IndexError:
   
        events_checked = True
        process = True

        

    try:
        current_serie = series[iter_series]  #si se acaban las series de números pasamos a la sig. combinacion
    except IndexError:
        combinations_ammount[str(current_combination)] = current_succesfull_events
        current_succesfull_events = 0
        iter_series = 0
        iter_combinations += 1

    if events_checked == False:
        combinations_ammount[str(current_combination)] = 0 # un diccionario que almacena el numero de veces que aparece una combinacion 
        
    if events_checked == False: # controlador si todos los eventos para una combinacion han sido analizados

        combination_Numbers_compared = False # variable de llave
        if combination_Numbers_compared == False:  # controlador si todos los numeros de una combinación han sido probados

            
            try:
                number = combinations[iter_combinations][inter_iter] # numero en la combinación

            except IndexError: # si falla significa que ya no hay mas numeros en la combinacion
                combination_Numbers_compared = True
                iter_series += 1 # pasamos a la siguiente serie
                inter_iter = 0
                progress_true = 0

                print("Combination numbers finished")

            if number in current_serie:
                progress_true += 1 # si hay un numero igual en la combinación aumenta el progreso

            if progress_true == len(current_combination): # vea comentario variable "progress_true"
                current_succesfull_events += 1 #agregamos un evento favorable al diccionario y a la llave de la combinacion

            else: 
                if combination_Numbers_compared == True:
                    inter_iter = 0
                else:
                    inter_iter += 1
            
                






        


    



