<!-- TOC -->
* [Documentations](#documentations)
* [Install Python Poetry](#install-python-poetry)
* [Build and install common test library](#build-and-install-common-test-library)
  * [Clone the project to local](#clone-the-project-to-local)
  * [Navigate to the project](#navigate-to-the-project)
  * [Create project virtualenv and install dependencies](#create-project-virtualenv-and-install-dependencies)
  * [Build the test library to wheel package under `dist/*.whl`](#build-the-test-library-to-wheel-package-under-distwhl)
  * [Install the test library module in wheel package](#install-the-test-library-module-in-wheel-package)
    * [Install to global environment](#install-to-global-environment)
    * [Install to in-project virtual environment](#install-to-in-project-virtual-environment)
  * [Notes](#notes)
<!-- TOC -->

# Documentations

- Visit the [Wiki](../../wiki) page for more information.

# Install Python Poetry

Project is managed by Python Poetry, it is a tool for dependency management and packaging in a Python-based project.

```Bash
pip install poetry
```

# Build and install common test library

Common test library is separated out from the test cases repository, it is a reusable library for other test repos. It is built and installed as a Python package.

## Clone the project to local

```Bash
git clone https://github.com/NDViet/test-automation-fwk-python.git
```

## Navigate to the project

```Bash
cd test-automation-fwk-python
```

## Create project virtualenv and install dependencies

```Bash
poetry install
```

## Build the test library to wheel package under `dist/*.whl`

```Bash
poetry build
```

## Install the test library module in wheel package

_Notes: replace the module name if yours is different_

### Install to global environment

```Bash
pip install --force-reinstall --find-links=dist ndviet_test_automation
```

Test library module and dependencies belong to (include Robot Framework) is installed globally, it is available for any projects.

### Install to in-project virtual environment

Activate in-project virtualenv

```Bash
.venv/Scripts/activate
```

Install the wheel package

```Bash
pip install --force-reinstall --find-links=dist ndviet_test_automation
```

## Notes

Check list of installed packages (results will be different between global and virtualenv)

```Bash
pip list
```

To deactivate the virtualenv

```Bash
deactivate
```