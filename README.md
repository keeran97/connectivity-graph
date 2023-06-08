[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/keeran97/connectivity-graph/HEAD)

# Windows installation of Connectivity Graphs

The connectivity graphs notebook provides access to information on individual neuron populations as per SCKAN and ApiNATOMY models. The *connectivity_graph.ipynb* allows visualisation of the individual neuron connections and the related anatomical features.

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
Poetry can be installed via the command below. In the desired directory:
```
python -m pip install poetry
```

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

Note that the process of setting a variable will differ depending on what interpreter is being used. In a Windows Command Prompt, the SciCrunch Key can be set as below.
```
set SCICRUNCH_API_KEY= *A valid SciCrunch API KEY*
```

Alternatively, the API Key can be permanently added to the Windows environment by following these [instructions](https://www.howtogeek.com/787217/how-to-edit-environment-variables-on-windows-10-or-11/).

4.	Activate the Jupyter notebook†.
```
poetry run jupyter notebook
```

A web browser should open to the Jupyter Notebook.

#### †NOTE: If steps 2 & 4 fail, Python may need to be invoked.
```
python -m poetry install
python -m poetry run jupyter notebook
```

## Usage
1.	Once successfully installed, start the Jupyter Notebook.

#### NOTE: If the browser doesn’t automatically open, the Notebook can be accessed via the URL provided.

2.	Navigate to and open the *connectivity_graph.ipynb* notebook.

![image](https://github.com/keeran97/connectivity-graph/assets/85910337/8574979c-987f-410c-8549-cb38c958444f)
 
3.	Neuron populations can be visualised by running the notebook. The first part of the notebook imports and loads the appropriate packages. The latter part (shown below), visualises the neuron population. The window that visualises the neuron population (highlighted by the red box below) can be navigated by left-clicking and dragging, and scrolling to zoom in/out. Note that the window can be resized from the lower right corner.

![image](https://github.com/keeran97/connectivity-graph/assets/85910337/a3ea594f-bf5f-468a-92c2-56321d6837d7)

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

For more information on the different ApiNATOMY models and their neuron populations, refer to the documentation below.
https://scicrunch.org/sawg/about/SCKAN

