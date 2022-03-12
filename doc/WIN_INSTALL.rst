=======================
Map-tools under Windows
=======================

Installation:
=============

Python
------

- Download and run the installer `here <https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe>`_, ticking the ``Add Python to the PATH`` box when the installation starts.

Git
---

- Download and run the installer `here <https://github.com/git-for-windows/git/releases/download/v2.35.1.windows.2/Git-2.35.1.2-64-bit.exe>`_, accepting all default options.

Poetry
------

- From the Windows' Start menu, run ``Git/Git CMD``.

- Within the command window, verify Python and git have been installed by giving the commands::

   git --version

   python --version

- You should see something like::

   C:\Users\Dave>git --version
   git version 2.35.1.windows.2

   C:\Users\Dave>python --version
   Python 3.10.2

- Now run::

   python -m pip install poetry

Map-tools
---------

- Give the command::

   git clone https://github.com/AnatomicMaps/map-tools.git

- followed by::

   cd map-tools

   poetry install

Running
=======

From the ``Git CMD`` prompt and in the ``map-tools`` directory (which is where you are after the above installation process) start the Jupyter notebook server with::

   poetry run jupyter notebook

A browser window should open which should eventually show:

.. list-table::
   :widths: 100
   :header-rows: 0

   * - .. image:: images/jupyter_1.png

Click on ``connectivity-graph`` to get:

.. list-table::
   :widths: 100
   :header-rows: 0

   * - .. image:: images/jupyter_2.png

Click on ``connectivity_graph.ipynb`` to get:

.. list-table::
   :widths: 100
   :header-rows: 0

   * - .. image:: images/jupyter_3.png

Click ``Run`` in the toolbar to execute the code in the first cell to get:

.. list-table::
   :widths: 100
   :header-rows: 0

   * - .. image:: images/jupyter_4.png

Replace ``A_VALID_SCICRUNCH_API_KEY`` with an actual API key for SciCrunch and click ``Run`` to execute code in this cell.

The cell number will briefly change to ``[*]`` to indicate that code is running and change back to a number when execution is complete. Click ``Run`` after a cell's code has finished to execute code in the following cell.

The result after the final two cells have been run should be like:

.. list-table::
   :widths: 100
   :header-rows: 0

   * - .. image:: images/jupyter_5.png

and:

.. list-table::
   :widths: 100
   :header-rows: 0

   * - .. image:: images/jupyter_6.png

