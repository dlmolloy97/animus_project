---
title: "README"
author: "Desmond L Molloy"
date: "11/13/2020"
output: html_document
---

The aim of this project was to create an interactive version of the graph produced by Chae et al in their 2015 paper "Association between an Internet-Based Measure of Area Racism and Black Mortality", enabling the user to highlight the percent difference between the measure of racism used for selected designated market areas (the basic geographic unit of the study) and the national median. A shapefile with the boundaries of current DMAs was joined with a modified version of Chae et al's original data. This merged dataframe was then used to create an HTML visualisation, via the Altair package in Python. The visualisation displays percent different, and name, for each DMA. Results differed slightly from the original paper's visualisations, due to the use of percent difference rather than standard deviations. Altair tended to 
