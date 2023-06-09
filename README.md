[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/keeran97/connectivity-graph/b0a3d79)

# Connectivity Graph Notebook

The connectivity graphs notebook provides access to information on individual neuron populations as per SCKAN. The *connectivity_graph.ipynb* allows visualisation of the individual neuron connections and the related anatomical features, as per ApiNATOMY models. For more information on the different ApiNATOMY models and SCKAN, refer to the [SciCrunch](https://scicrunch.org/sawg/about/SCKAN) site.

The notebook can be accessed in two different ways. A live version of the notebook can be used via the Binder badge above. For more information refer to the *Jupyter Binder usage* section below. The notebook can also be installed and used locally on various machines. This allows changes to be made and saved locally (the files will be kept in their original state in this GitHub repository). Refer to the *Windows installation of Connectivity Graphs* guide for more information.

# Jupyter Binder usage

A live version of the Jupyter notebook can be launched via the Binder badge above. This allows usage of the notebook without the need to install any of the requirements. 

Clicking on the Binder badge will open the Jupyter notebook in a new tab. As shown below, the notebook can be opened and run in the web browser. Note that it may take some time for the notebook to load, as the environment must first be built. 
A SciCrunch Key must be input in order to access SCKAN, as highlighted in the red box below. For more information on obtaining a SciCrunch API Key follow these [instructions](https://docs.sparc.science/docs/accessing-scicrunch-vocabulary-services#getting-an-api-key-to-access-scicrunch).

![image](https://github.com/keeran97/connectivity-graph/assets/85910337/3a5b525a-aaf9-4d10-89ba-d0e40ad0f352)


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

Run an update to the Poetry environment to ensure all requirements in the Poetry environment are met.
```
poetry update
```

3.	A SciCrunch key will need to be set in order to access SCKAN. This can be done prior to launching the jupyter notebook, or can be set directly in the notebook itself. 

For more information on obtaining a SciCrunch API Key follow these [instructions](https://docs.sparc.science/docs/accessing-scicrunch-vocabulary-services#getting-an-api-key-to-access-scicrunch).

The SciCrunch key can be set as an environment variable before running the notebook. This removes the need to set it within the notebook. Alternatively, the API Key can be permanently added to the Windows environment by following these [instructions](https://www.howtogeek.com/787217/how-to-edit-environment-variables-on-windows-10-or-11/).

**NOTE**: *The process of setting a variable will differ depending on what interpreter is being used. In a Windows Command Prompt, the SciCrunch Key can be set as below.*
```
set SCICRUNCH_API_KEY= 'A valid SciCrunch API Key'
```

The key can also be set as an environment variable within the notebook, after activation as shown below. When doing this, be sure to remove the # from the line of code. This turns the line from a comment to an activate line of code, making sure it is run.

**NOTE**: *This step is done after activating the Jupyter notebook - Step 4*. 

![image](https://github.com/keeran97/connectivity-graph/assets/85910337/67dd1d25-01d7-4bd2-9acf-76a119dc82dc)

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

![GIFMaker_me (3)](https://github.com/keeran97/connectivity-graph/assets/85910337/204f68f2-2eb3-4968-8864-ab7c1d035277)

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
