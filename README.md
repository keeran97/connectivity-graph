[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/keeran97/connectivity-graph/9e4ba28)

# Connectivity Graph Notebook

The connectivity graphs notebook provides access to information on individual neuron populations as per SCKAN. The *connectivity_graph.ipynb* allows visualisation of the individual neuron connections and the related anatomical features, as per ApiNATOMY models. For more information on the different ApiNATOMY models and SCKAN, refer to the [SciCrunch](https://scicrunch.org/sawg/about/SCKAN) site.

The notebook can be accessed in two different ways. A live version of the notebook can be used via the Binder badge above. For more information refer to the *Jupyter Binder usage* section below. The notebook can also be installed and used locally on various machines. This allows changes to be made and saved locally (the files will be kept in their original state in this GitHub repository). Refer to the *Windows installation of Connectivity Graphs* guide for more information.

# Jupyter Binder usage

A live version of the Jupyter notebook can be launched via the Binder badge above. This allows usage of the notebook without the need to install any of the requirements. In order to use the notebook, the extra step of adding a SciCrunch key must be done in order to access SCKAN. For more information on obtaining a SciCrunch API Key follow these [instructions](https://docs.sparc.science/docs/accessing-scicrunch-vocabulary-services#getting-an-api-key-to-access-scicrunch).

Clicking on the Binder badge will open the Jupyter notebook in a new tab. As shown below, the notebook can be opened and run in the web browser.

**NOTE**: To use the live version of the notebook the *live_connectivity_graph.ipynb* in the *Binder* folder must be opened, as highlighted with the red boxes below.

![image](https://github.com/keeran97/connectivity-graph/assets/85910337/aa6f3b0d-afa5-4064-8ab4-187d105b65aa)

# Windows installation of Connectivity Graphs

The jupyter notebook can be installed using various command interpreters. In this case, the notebook was installed using the [Windows Command Prompt](https://www.lifewire.com/how-to-open-command-prompt-2618089).

## Requirements

### Python
If not already present, download and install Python as per the [official instructions](https://www.python.org/downloads/). Be sure to select the ‘*Add Python to PATH*’ option.
                      
The installation can be tested with
```
    python --version
```

### GitHub
Download and install Git as per the [official instructions](https://github.com/git-guides/install-git).

For more information on using Git refer to this [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf).

The installation can be tested with 
```
git version
```

### Poetry
Poetry can be easily installed via the command below. In the desired directory:
```
python -m pip install poetry
```

The Poetry tool can also be installed as per the [official instructions](https://python-poetry.org/docs/#installation).

## Installation

1.	 Having installed the requirements, clone the connectivity-graph repository.
```
git clone https://github.com/keeran97/connectivity-graph.git
```

2.	Navigate into the cloned directory and install poetry†.
```
cd connectivity-graph
poetry install
```

3.	A SciCrunch key will need to be set in order to access SCKAN. For more information on obtaining a SciCrunch API Key follow these [instructions](https://docs.sparc.science/docs/accessing-scicrunch-vocabulary-services#getting-an-api-key-to-access-scicrunch).

**NOTE**: *The process of setting a variable will differ depending on what interpreter is being used. In a Windows Command Prompt, the SciCrunch Key can be set as below.*
```
set SCICRUNCH_API_KEY= *A valid SciCrunch API KEY*
```

Alternatively, the API Key can be permanently added to the Windows environment by following these [instructions](https://www.howtogeek.com/787217/how-to-edit-environment-variables-on-windows-10-or-11/).

4.	Activate the Jupyter notebook†.
```
poetry run jupyter notebook
```

A web browser should open to the Jupyter Notebook.

**†NOTE**: *If steps 2 & 4 fail, Python may need to be invoked.*
```
python -m poetry install
python -m poetry run jupyter notebook
```

## Usage
1.	Once successfully installed, start the Jupyter Notebook.

**NOTE**: *If the browser doesn’t automatically open, the Notebook can be accessed via the URL provided.*

2.	Navigate to and open the *connectivity_graph.ipynb* notebook.

![image](https://github.com/keeran97/connectivity-graph/assets/85910337/8574979c-987f-410c-8549-cb38c958444f)
 
3.	Neuron populations can be visualised by running the notebook. The first part of the notebook imports and loads the appropriate packages. The latter part (shown below), visualises the neuron population. The window that visualises the neuron population can be navigated by left-clicking and dragging, and scrolling to zoom in/out. Note that the window can be resized from the lower right corner.

![Media2_AdobeExpress](https://github.com/keeran97/connectivity-graph/assets/85910337/ace31ffb-7d95-4bf6-9d1c-a73cab7b4c9e)

## ApiNATOMY Models

The different populations can be visualised by changing the entity attribute of the Jupyter Notebook, highlighted in the image above. 
The table below displays the different ilxtr and path IDs for the various ApiNATOMY models and their respective paths.

| **Model**                                 | **ilxtr** ('X' represents Path ID) | **Path IDs**                                                          |
| ----------------------------------------- | ---------------------------------- | --------------------------------------------------------------------- |
| ApiNATOMY model of bronchomotor control   | neuron-type-bromo-X                | 1, 2, 3, 4, 5, 6                                                      |
| ApiNATOMY model of the spleen             | neuron-type-splen-X                | 1, 2, 3, 4, 5                                                         |
| ApiNATOMY model of the stomach            | neuron-type-sstom-X                | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13                             |
| Ardell-Armour model of the heart          | neuron-type-aacar-X                | 1, 2i, 2m, 4, 5, 6, 7a, 7v, 8a, 8v, 9a, 9v, 10a, 10v, 11, 12, 13      |
| Bolser-Lewis model of defensive breathing | neuron-type-bolew-unbranched-X     | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29 |
| Keast model of the bladder                | neuron-type-keast-X                | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 |
| SAWG model of the distal colon            | neuron-type-sdcol-X                | b, c, d, f, g, h, i, j, j’, k, l, l’, m, n, o, p, q                   |
