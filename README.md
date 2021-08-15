# cloud_dev
Francisco Camargo

I want to be able to end up with a coding environment that enables me to develop and deploy on the cloud. I want to be able to make changes to the code on the cloud on the fly, this is possible with VS Code (somehow...).

## Using this repo

### Typora

Using [Typora](https://typora.io/) to read and edit .md files. Using the Nord [theme](https://theme.typora.io/theme/Nord/).

### environment

Create the environment for this repo by running:

`conda env create -f environment.yaml`

### dataclass decorator

### Running Unit Tests

[Guide](https://realpython.com/python-testing/)

#### unittest

able to run test_a.py from spyder or from terminal:

`python -m unittest tests.test_a`

However, trying in VSCode failed; doesn't handle importing packages in a similar fashion for some reason.

#### run all tests with unittest

Add `__init__.py` file within `tests` folder and from parent directory run

`python -m unittest`

#### pytest

try `pytest`, sounds simpler than unittest.

Following [ref](https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest): Ran all tests including the ones written in other files using `unittest` by running 

`python -m pytest` 

By using `@pytest.fixture` decorators we avoided having write some repetitive boilerplate code to make instances of the `Wallet` class. Each test is provided with a newly-initialized `Wallet` instance, and not one that has been used in another test. By running parametrized test functions we can easily test several quantitative scenarios.

[ref](https://realpython.com/pytest-python-testing/)

## GitHub Issues

connect issues to branches via [pull requests](https://github.blog/2013-05-14-closing-issues-via-pull-requests/)

After I opened a pull request on GitHub, I then selected the relevant issue from the right-hand set of options. Then when the merge was complete, the issue was automatically closed.

## GitHub Codespaces

GitHub Codespaces would let me develop in-browser. On a waitlist for the time being.

### Continuous integration / continuous deployment

[Tutorial](https://www.youtube.com/watch?v=eB0nUzAI7M8&ab_channel=Fireship)

GitHub Actions

## docker
