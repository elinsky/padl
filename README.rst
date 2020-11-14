====
PADL
====


.. image:: https://img.shields.io/pypi/v/padl.svg
        :target: https://pypi.python.org/pypi/padl

.. image:: https://img.shields.io/travis/elinsky/padl.svg
        :target: https://travis-ci.com/elinsky/padl

.. image:: https://readthedocs.org/projects/padl/badge/?version=latest
        :target: https://padl.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/elinsky/padl/shield.svg
     :target: https://pyup.io/repos/github/elinsky/padl/
     :alt: Updates



Python algorithms and data structures library


* Free software: MIT license
* Documentation: https://padl.readthedocs.io. (work in progress)


Features
--------

* Graph - Data structure for unweighted undirected graphs.
* Depth First Search - Given an undirected unweighted graph and a source vertex, DepthFirstSearch calculates how many
  and which vertices in the graph are reachable from the source target.
* Depth First Search Paths - Given an undirected unweighted graph and a source vertex, DepthFirstSearchPaths calculates
  whether or not there exists a path from the source to the target, and if it exists, the path.
* Breadth First Search Paths - Given an undirected unweighted graph and a source vertex, BreadthFirstPaths calculates
  the shortest path between the source vertex and all other vertices.

Development
-----------

* Travis CI is used for continuous integration testing.
* PyUp is used to keep dependencies secure and up to date.
* Flake8 is used to enforce style guidelines.
* Tox is used to ensure:

  * Tests pass on multiple versions of Python.
  * Flake8 tests pass.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
