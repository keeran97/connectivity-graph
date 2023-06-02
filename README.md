# Windows installation of Connectivity Graphs

The connectivity graphs notebook provides access to information on individual neuron populations as per SCKAN and ApiNATOMY models. The connectivity_graph.ipynb allows visualisation of the individual neuron connections and the related anatomical features.

The jupyter notebook can be installed using various command interpreters. In this case, the notebook was installed using the Windows Command Prompt.

## Requirements

### Python
If not already present, download and install Python as per the official instructions. Be sure to select the ‘Add Python to PATH’ option.
                     
https://www.python.org/downloads/
                      
The installation can be tested with
```
    python --version
```

### GitHub
Download and install Git as per the official instructions. 

https://github.com/git-guides/install-git

For more information on using Git refer to this Git Cheat Sheet.

https://education.github.com/git-cheat-sheet-education.pdf

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

3.	A SciCrunch key will need to be set in order to access SCKAN. For more information on obtaining a SciCrunch API Key refer to the documentation below.

https://docs.sparc.science/docs/accessing-scicrunch-vocabulary-services#getting-an-api-key-to-access-scicrunch

Note that the process of setting a variable will differ depending on what interpreter is being used. In a Windows Command Prompt, the SciCrunch Key can be set as below.
```
set SCICRUNCH_API_KEY= *A valid SciCrunch API KEY*
```

Alternatively, the API Key can be permanently added to the environment, shown in the link below.

https://www.howtogeek.com/787217/how-to-edit-environment-variables-on-windows-10-or-11/

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

2.	Navigate to and open the connectivity_graph.ipynb notebook.

![image](https://github.com/keeran97/connectivity-graph/assets/85910337/8574979c-987f-410c-8549-cb38c958444f)
 
3.	Neuron populations can be visualised by running the notebook. The first part of the notebook imports and loads the appropriate packages. The latter part (shown below), visualises the neuron population. The window that visualises the neuron population (highlighted by the red box below) can be navigated by left-clicking and dragging, and scrolling to zoom in/out. Note that the window can be resized from the lower right corner.

![image](https://github.com/keeran97/connectivity-graph/assets/85910337/a3ea594f-bf5f-468a-92c2-56321d6837d7)

## ApiNATOMY Models

The different populations can be visualised by changing the entity attribute of the Jupyter Notebook, highlighted in the image above. 
The image below displays the different ilxtr and path IDs for the various ApiNATOMY models and their respective paths.

![image](https://github.com/keeran97/connectivity-graph/assets/85910337/9c6bcb41-8a6f-4430-b19f-9a28973f3d1c)

For more information on the different ApiNATOMY models and their neuron populations, refer to the documentation below.
https://scicrunch.org/sawg/about/SCKAN

