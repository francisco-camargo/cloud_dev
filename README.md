# cloud_dev
I want to be able to end up with a coding environment that is deployed to the cloud and I can develop on from VS Code or equivalent on the fly.

## github issues
connect issues to branches via [pull requests](https://github.blog/2013-05-14-closing-issues-via-pull-requests/)

After I opened a pull request on GitHub, I then selected the relevant issue from the right-hand set of options. Then when the merge was complete, the issue was automatically closed.

## GitHub Codespaces

GitHub Codespaces would let me develop in-browser. On a waitlist for the time being.

## environment

Create the environment for this repo by running:

`conda env create -f environment.yaml`

## Running Unit Tests

### unittest

able to run test_a.py from spyder or from terminal:

`python -m unittest tests.test_a`

However, trying in VSCode failed; doesn't handle importing packages in a similar fashion for some reason.

### Run all tests with unittest

Add `__init__.py` file within `tests` folder and from parent directory run

`python -m unittest`

### pytest

try `pytest`, sounds simpler than unittest

Machine Learning for Trading class used pytest in [this](https://bitbucket.org/GT-OMSCS/cs7646-ml4t/src/master/project_7_q_learning_robot/grade_robot_qlearning.py) assignment

## dataclass decorator

## docker

## cloud dev

develop code deployed in the cloud (ie CGP, AWS, Azure)
