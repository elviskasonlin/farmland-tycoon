# Farmland Tycoon

For 10.014 Computational Thinking for Design, 1D Project

Created by\
*in order of increasing student ID number*

1004210 Pyae Phyo Aung @ Elvis Kason Lin\
1005262 Kevin Teng Jin Peng\
1005275 Lin Lin\
1005477 Theresa Lam Zouh Ling\
1003595 Yang Chen Ye

Freshmore, Class of 2024, Singapore University Technology and Design

# About
Farmland Tycoon is a farming simulator created in python.
...

# Setting up development environment

1. (Optional) Install `pyenv` and `virtualenv`
  - `pyenv` to manage your python versions
  - `virtualenv` to enable python virtual environments
2. Install `pipenv` to manage per-project dependencies
3. Run `pipenv install --dev` to install development dependencies
4. Run `pipenv shell` to enter into the `pipenv` environment

# Generating Documentation with Sphinx

Follow the steps below to use [Sphinx](https://packaging.python.org/tutorials/creating-documentation/) for automatic documentation creation in different formats:

1. Install it by running `pipenv install --dev`
2. Go to the project directory using `cd /path/to/project/docs/`
3. Next, to generate the documentation, 
   * run `make html` to generate a html site
   * run `make pdf` to generate a pdf file
4. View the generated files by going to `./docs/build/` and entering the corresponding folder (`html/` or `pdf/`)
5. To edit the generated contents, edit the `index.rst` and other `.rst` files located inside `./docs/source/`

Go to the official sphinx [site](https://www.sphinx-doc.org/en/master/usage/quickstart.html) to understand it in more detail.

Currently, this Sphinx installation uses `rst2pdf` module (installed during `pipenv install --dev`) to generate the documentation in pdf format.