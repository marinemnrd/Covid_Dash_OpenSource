[![SWH](https://archive.softwareheritage.org/badge/swh:1:dir:2bc38c6287a8fcc88daa9de467006b0fa00a9233/)](https://archive.softwareheritage.org/swh:1:dir:2bc38c6287a8fcc88daa9de467006b0fa00a9233;origin=https://github.com/marinemnrd/Covid_Dash_OpenSource.git;visit=swh:1:snp:a80e358a9385105e7e665d652280d97e4b5c2072;anchor=swh:1:rev:f55e028537102fb0004e136b7f7767f7492c7d18)


# Covid Open Source DashBoard 📈  <p style='text-align: right;'> ![this](https://coronavirus.jhu.edu/static/media/jhu-logo-white-horizontal.68872b26.svg) </p>


Table of Content
-----------------
  * Project Description
  * Set up
  * Launching the App
  * The dashboard
  * Made with
  * Authors
  * License


# Project Description :clipboard:

Covid Open Source Dashboard is an interactive Visualisation tool provinding an overview of the evolution of different Covid Pandemic indicators as a function of time. The available Indicators are : 

- Cumulated Number of cases
- Cumulated Number of Deaths

All the Datas Are provided as open-data by the [Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19) and [Kaggle](https://www.kaggle.com/tanuprabhu/population-by-country-2020).


 # Set Up :wrench:
Clone this repository using command 

```
git clone https://github.com/marinemnrd/Covid_Dash_OpenSource.git
```
 
Create a python virtual environnemnt and install the requirement.txt package using pip :

```
pip install -r requirements.txt
```

The requirements.txt contains : 

```
numpy==1.20.3
pandas==1.2.4
plotly==4.14.3
plotly-express==0.4.1
streamlit==0.82.0
```

Open your favourite IDE, open the project and you are ready to launch the app !


# Launching the App :key:

Run the following line in the terminal then go to the suggested URL. It will launch the Dashboard locally.

```
streamlit run main.py
```
:sparkling_heart: Enjoy ! :sparkling_heart:


# Web :computer:

The project is Hosted by streamlit.
You can also click on this [link](https://share.streamlit.io/paulmontecot/covid_dash_opensource/main/main.py) to visualize the dashboard.


# Made with :construction:

Here are the programs / software / resources that we used to develop our project.

* [Python 3.9](https://www.python.org/) - Programming language version 3.9
* [Materialize.css](http://materializecss.com) - Framework CSS (front-end)
* [Streamlit](https://streamlit.io/) - Open-source Python library 
* [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/) - IDE
* [John Hopkins University Data](https://coronavirus.jhu.edu/map.html) - Coronavirus data used to build the Dash
* [Jupyter Notebook](https://jupyter.org/) - Open-source web application to create and share code
* [Deenote](https://deepnote.com/project/CovidDashOpenSource-vWDQOttkRneLrrNERsUCUg/%2Fnotebook.ipynb) - Data Science NoteBook


## Authors :crown:

* **Marine** [@MarineMnrd](https://github.com/marinemnrd)
* **Elysabeth** [@Lily87-hub](https://github.com/Lily87-hub)
* **Paul** [@paulmontecot](https://github.com/paulmontecot)


## License :white_check_mark:

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



