# NetworkStrengthMapping

This project deals with the aspect of capturing strength of various networks using an unmanned aerial vehicle, a hexacopter. A PixHawk controller is used to control the hexacopter in flight either automated using a flight plan or a RC transmitter being controlled by a user. A raspberry pi is attached to the hexacopter for recording network details via a Python script. A dongle or a WiFi module is used for connecting to network. 

## Getting Started

Follow the proceding instructions to use the repository in one's project.

### Prerequistes 
Install these software for a smooth run.
```
 Python v3.7.5 or greater
 Jupyter Notebooks
```
Libraries required for the project
```
pandas
gmaps
IPython
ipywidgets
```

### Installing
Clone the repository on the local machine. Change the minor details
```
Interface name in DataCollectionScript.py
File where values are stored
```
In case of one wants to update the files please feel free to fork the repository and make a pull request to update the changed file.
There are comments in the files explaining the various aspects of the programs.

## Deployment
Run the DataCollectionScript.py file either on startup of local machine or through the terminal/command prompt.
Press Crtl-Z/Ctrl-C to terminate the execution of file.
Run jupyter notebooks to make the heat map.
In case figure is not displayed run "jupyter nbextension enable --py gmaps" in the terminal/command prompt.

## Built With
* **Python v3.7.5**
* **Jupyter Notebooks**

## Authors
* **Gotam Dahiya** - *Creation of data collection and heat map generation script*
