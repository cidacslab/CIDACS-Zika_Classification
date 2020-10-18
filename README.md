# Classification algorithm of Congenital Zika Syndrome: characterizations, diagnosis and validation

## Table of contents
* [General info](#general-info)
* [Compilation](#compilation)
* [Input data](#Input-data)
* [Files](#files)
* [References](#references)

## General info
In this directory, we present the code to construct a Classification algorithm for Congenital Zika Syndrome (CZS)

The code originated from the project described in the paper [1]. The purpose of this algorithm is to be able to identify cases of CZS automatically based on electronic records, serogy and imaging reports.

## Compilation
We performed our statistical analysis using Python version 3.6.5.  We computer classification evaluation using Jupyter Notebook.
Necessary packages:
* [scikit-learn](https://scikit-learn.org)
* [matplotlib](https://matplotlib.org)
* [spacy](https://spacy.io)

## Input data

we use the Brazilian electronic records RESP (Public Health Event Record) [2] linked with SINASC (Live Birth Information System) [3].
For training, results obtained by the classification performed by a group of specialists described in the article were used [4].

## Files

To perform the study of time series analyses we collected the confirmed and discarded reported cases of each arbovirus per epidemiological week in Brazil, from 2015 to 2017.

## References 
[1] Interdependence between confirmed and discarded cases of dengue, chikungunya and Zika viruses in Brazil: A multivariate time-series analysis, DOI:10.1371/journal.pone.0228347.

[2] Seabold, Skipper and Perktold, Josef Statsmodels: Econometric and statistical modeling with python.
9th Python in Science Conference, 2010. https://www.statsmodels.org/stable/index.html.
