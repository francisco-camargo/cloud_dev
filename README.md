# gh_vscode
Test Github's use of VS code.
$$
y = mx+b
$$

## github issues
connect issues to branches via [pull requests](https://github.blog/2013-05-14-closing-issues-via-pull-requests/)

## environment
Create the environment for this repo by running:

`conda env create -f environment.yaml`

## unittest
able to run test_a.py from spyder or from terminal:

`python -m unittest tests.test_a`

However, trying in VSCode failed; doesn't handle importing packages in a similar fashion for some reason.

#### Run all tests

Add `__init__.py` file within `tests` folder and from parent directory run

`python -m unittest`

## pytest

try `pytest`, sounds simpler than unittest

Machine Learning for Trading class used pytest in [this](https://bitbucket.org/GT-OMSCS/cs7646-ml4t/src/master/project_7_q_learning_robot/grade_robot_qlearning.py) assignment

## dataclass decorator

## docker

## cloud dev

develop code deployed in the cloud (ie CGP, AWS, Azure)
