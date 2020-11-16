# CDT 1D Project Game
___

For 10.014 Computational Thinking for Design

Created by\
*in order of increasing student ID number*

1004210 Pyae Phyo Aung @ Elvis Kason Lin\
1005262 Kevin Teng Jin Peng\
1005275 Lin Lin\
1005477 Theresa Lam Zouh Ling\

Freshmore, Class of 2024

# About

# Setting up development environment

1. (Optional) Install `pyenv` and `virtualenv`
  - `pyenv` to manage your python versions
  - `virtualenv` to enable python virtual environments
2. Install `pipenv` to manage per-project dependencies
3. Run `pipenv install --dev` to install development dependencies
4. Run `pipenv shell` to enter into the `pipenv` environment

# Documentation

To use [Sphinx](https://packaging.python.org/tutorials/creating-documentation/) for documentation creation,

1. Install it by running `pipenv install --dev`
2. Go to the project directory using `cd /path/to/project/docs/`
3. Next, to generate the documentation, run `make html`
4. To edit, edit the `index.rst` file inside `./docs/source/`

Go to the official sphinx [site](https://www.sphinx-doc.org/en/master/usage/quickstart.html) to understand it in more detail.
