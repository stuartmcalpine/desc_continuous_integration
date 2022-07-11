.. DESC CI test documentation master file, created by
   sphinx-quickstart on Mon Jun 20 11:41:18 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to DESC CI test's documentation!
========================================

This repository contains a set of example Continuous Integration (CI) workflows
to get you started when considering CI for DESC software.  

The code in this repository is pure Python, yet the CI principles remain the
same regardless of the language. We also use ``pytest`` to build our test
framework, however again this is up to you what works best for your software. 

Those already familiar with GitHub Actions and CI can skip to the *DESC CI
Checklist* to see what we would recommend you use in your CI workflows.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   ./desc/ci
   ./desc/gh_actions
   ./desc/desc_working_examples
   ./desc/desc_checklist
   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
