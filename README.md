# Energy Demand Prediction Model

- **¿Que problema se plantea resolver?**  
  En este proyecto, se pretende generar un modelo de aprendizaje automático que permita predecir la demanda de energía en la región noroeste de México.

- **¿Porqué es un problema importante para la institución/organización/empresa?**  
  Una de las tareas principales del Centro Nacional de Control de Energía (CENACE) es la predicción de la demanda de energía eléctrica en el Sistema Eléctrino Nacional, por lo que un modelo de este tipo podría ser una herramienta clave para realizar esta tarea.
- **¿Cuales son las métricas para medir el impacto de la solución una vez obtenida?**

- **¿Que problema de aprendizaje implica resolver?**  
  En este caso, nuestro problema se trata de un problema de regresión, ya que nuestra variable de respuesta corresponde a la demanda de energía de la zona del noroeste, la cual es un valor continuo positivo.  
  Nuestros datos de entrada son además series de tiempo, ya que se trata de diversas variables meteorológicas y de demanda de energía entre los años 2017 y 2022.
- **¿Qué metricas permiten medir la calidad del modelo de aprendizaje? ¿Cuales son sus valores deseables?**  
  En el caso de la predicción de la demanda de energía, el [Manual de Pronósticos](https://www.diputados.gob.mx/LeyesBiblio/regla/n533.pdf) que rige las métricas a utilizar por el CENACE, establece que se utilizará la métrica MAPE para medir el grado de certeza con que realiza sus
  pronósticos de demanda.  
  La fórmula del MAPE, o Mean Absolute Percentage Error, es la siguiente:  
  $$\textup{MAPE} = \frac{1}{h}\sum_{t=1}^{h}\left |  \frac{DR_t - DP_t}{DR_t} \right | * 100$$  
  Donde:

  - $h$ = Número de horas a evaluar
  - $DR_t$ = Demanda integrada real de la hora $t$
  - $DP_t$ = Demanda integrada pronosticada de la hora $t$

  Siguiendo lo establecido en el Manual, nuestro modelo deberá igualmente utilizar esta métrica para evaluar su desempeño. Idealmente, se busca un valor del MAPE menor al 5%.

- **¿Como están alineadas las métricas de la calidad del modelo con las métricas de impacto de la solución?**

---

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

---

To create a project like this, just go to https://dagshub.com/repo/create and select the **Cookiecutter DVC** project template.

Made with 🐶 by [DAGsHub](https://dagshub.com/).
