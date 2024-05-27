## INTRODUCCION

Se ha considerado la prevención del consuma de energía como el tema clave para la planeación de red eléctricas inteligentes, en el mercado de electricidad y sustentabilidad de potencia eléctrica [1].  

Este problema se ha planteado a lo largo de diferentes trabajos, en todo el mundo, ya que la predicción del consumo es vital para el manejo de energía. Los motodos empleado se dividen en tres categorías: Análisis Estadístico, Aprendizaje Automático, y aprendizaje profundo (Deep Learning) [1].

La predicción es un requisito esencial para el sistema de generación de energía, no solo para la planeación de inversión de expansión de capacidad, sino también como factor crucial en el manejo de tarifas eléctricas, cual es relevante para el plan de administración de energía [2].

Debido al crecimiento poblacional de las ciudades y al cambio de clima por el calentamiento global, se puede apreciar un aumento en el consumo de energía eléctrica que va creciendo a lo largo de los años.

En este trabajo se empleó el uso de medidas de reducción de dimensionalidad de los datos; así como diversos métodos de entrenamiento no supervisado, y entrenamiento supervisado para explorar diversas formas de producir un modelo que prediga, de la mejor forma posible, el comportamiento variante del consumo de energía a lo largo de los años venideros, específicamente la zona norponiente de México. 

Se ha considerado que un Error Porcentaje Medio Absoluto de 5%, ya que este está plasmado en el reglamento de CENACE, por lo que, un error menor a este se considera un resultado satisfactorio. (revisión fáctica)
# <- comparación con diversas paperas que quieren hacer lo mismo.

## DATOS
Los datos empleados para crear dicho modelo son proporcionados por el Sistema Eléctrico Nacional (SEN), contienen el consumo eléctrico y las temperaturas máximas y mínimas del día en la zona norponiente del país de las siguientes localidades: Caborca, Ciudad Obregón, Hermosillo, en el estado de Sonora, y los Mochis y Culiacán del estado de Sinaloa. También estas cuentan con datos de actividades antropomórficas que se realizan en la zona estudiada, como lo es días feriados, los cuales, afectan directamente al consumo eléctrico debido a que en estos días se reduce significativamente la actividad laboral.

## Análisis de Componentes Principales

## K-MEANS
K-means es un algoritmo de aprendizaje no supervisado utilizado para agrupar datos en conjuntos o clústeres basados en similitudes. Para usar K-means, primero se elige el número de clústeres (K) que se desea identificar en los datos. Luego, el algoritmo asigna aleatoriamente puntos iniciales como centroides para cada clúster.
En este diagrama, podemos apreciar que nuestros datos podrían ser separados en al menos 5 clústeres, aunque también podemos apreciar una posible confusión entre estos (en este caso, entre el clúster `cyan` y `azul`).

## RANDOM FOREST
El algoritmo Random Forest se utilizó para construir un modelo de predicción de consumo energético al aprovechar su capacidad para manejar conjuntos de datos complejos y no lineales. Primero, se recopilaron datos históricos de consumo energético, incluidos factores como la hora del día, la temperatura, la temporada y eventos especiales. Luego, se dividió el conjunto de datos en un conjunto de entrenamiento y otro de prueba.
En este caso se realizo la selección de hiperparametros con Optuna. Optuna es una biblioteca de optimización de hiperparámetros de código abierto para Python. Su objetivo principal es automatizar el proceso de ajuste de hiperparámetros de algoritmos de machine learning de manera eficiente y fácil de usar. Dando un MAPE de 0.99% de error.

## GRADIENT-BOOSTING
El algoritmo de Gradient Boosting se empleó para construir un modelo de predicción de consumo energético aprovechando su capacidad para generar un conjunto de modelos débiles, como árboles de decisión, que se combinan secuencialmente para mejorar la precisión predictiva. Primero, se recopilaron datos históricos de consumo energético junto con variables relacionadas, como la temperatura, la hora del día y eventos especiales.
En este caso se utilizó Grid Search para seleccionar los hiperparametros. Dando un MAPE de 0.96% de error.

## REGRESION LINEAR
La regresión lineal se utilizó para desarrollar un modelo de predicción de consumo energético al establecer una relación lineal entre las variables predictoras, como la temperatura, la hora del día y el día de la semana, y la variable objetivo, que es el consumo energético.
Después de entrenar el modelo, se evaluó su rendimiento utilizando el conjunto de prueba para verificar su capacidad para generalizar y predecir con precisión el consumo energético en datos no vistos.
Como conclusión, en esta libreta pudimos apreciar que en nuestro caso, incluso un modelo tan "sencillo" como la regresión lineal permite ajustar y predecir muy bien nuestra variable objetivo. En este caso, podemos ver en los registros de mlflow que el coeficiente $R^2$ de nuestro modelo alcanza un valor de $0.99$. Además de esto, nuestra métrica objetivo (MAPE) alcanza un valor de apenas 2%, lo cual indica un buen desempeño del modelo.

## MAQUINA DE VECTORES DE SOPORTE
El algoritmo de Máquinas de Vectores de Soporte (SVM, por sus siglas en inglés) se aplicó para desarrollar un modelo de predicción de consumo energético aprovechando su capacidad para encontrar el hiperplano óptimo que mejor separa los datos en clases distintas.
Para este problema, se utilizó selecciona miento de hiperparametros usando Random Search y Grid Search para encontrar la configuración de hiperparametros.
En este caso nos dio un MAPE de alrededor de 2%.

## LSTM
Para construir un modelo de predicción de consumo energético utilizando redes neuronales LSTM (Long Short-Term Memory), se recopilaron datos históricos de consumo energético, incluyendo factores temporales como la hora del día, el día de la semana y factores ambientales como la temperatura. Estos datos se organizaron en secuencias temporales y se dividieron en conjuntos de entrenamiento y prueba. Las redes LSTM fueron utilizadas debido a su capacidad para capturar dependencias temporales a largo plazo en los datos.
El LSTM han aplicado en todos lados desde la predicción de futuro como lo es la predicción del clima, la contaminación del aire, y predicción de la bolsa de valores.

## CONCLUSIONES

## Bibliografía
[1] Sameh Mahjoub, LabriChririfi-Alaoui, Predicting Energy Consumption Using LSTM, MultiLayer GRU and Drop-GRU Neural Network, 
[2] Arturo Morales Acevedo, Forcasting Future energy demand: Electrical Energy in Mexico as example case; ISES Solar World Congress 2013.
[3] Informe de Labores 2022 - 2023, 1 de septiembre 2023. Secretaria de Energía.
[4] Demanda y consumo 2021 -2035. PRODECEN.
[5] Bibiana Lanzilotta, Silvia Rodriguez Collazo, Modelos de predccion de demanda de energía eléctrica con datos horarios para Uruguay, 2016,Cuadernos de CIMBAGE No 18 1-28.
