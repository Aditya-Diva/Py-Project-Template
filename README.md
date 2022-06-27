# Py Project Template

## Table of Contents

- [About the Project](#about-the-project)
- [Packages Used](#packages-used)
- [Overall Flow](#overall-flow)
  - [Testing](#testing)
  - [Pre-commit](#pre-commit)
  - [Documentation](#documentation)
  - [Deployment](#deployment)
- [Usage](#usage)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About The Project

This is a sample template for python projects that i'd like to update from time to time as i learn more in python development.

It's also meant to act as a refresher for some good practices and/or to look up basic how-to.

It involves some concepts like abstract classes, documentation, and testing and implements a rather limited calculator logic for the base.

## Packages used

- **pipenv** for creating a virtual environment.
  Using pytest for testing packages. (https://docs.pytest.org/)
- **pre-commit** for linting(**pylint**) and running tests(**pytest**) before committing.
- **Sphinx** for maintaining auto generated code documentation.

## Overall Flow

Let's look into different components in brief.

### Testing

For testing:

```sh
$ cd tests
$ pytest
```

For quiet mode:

```sh
$ pytest -q
```

For marked testing:

```
$ pytest -m <mark_name>
E.g
$ pytest -m getter
```

Note different custom marks have been defined in [tests/pytest.ini](tests/pytest.ini)

### Pre-commit

Refer to [.pre-commit-config.yaml](.pre-commit-config.yaml)

Runs some basic checks on files, along with black formatter, pylint and finally pytest. These are run before user tries to commit and enforces standards.

To run this explicitly without having to commit:

```sh
$ pipenv shell
(env) $ chmod +x pre-commit.sh
(env) $ ./pre-commit.sh
```

### Documentation

Sphinx was used for documentation. Refer to live documentation for the project at <https://aditya-diva.github.io/py-project-template>

Please refer to [docs/auto_update.sh](docs/auto_update.sh) for updating docs if changes are made.

### Deployment:

- On my target system create a requirements.txt:

  ```sh
  $ pipenv requirements > requirements.txt
  $ pipenv requirements --dev-only > dev-requirements.txt
  ```

  While deploying, inside a virtualenv I run:

  ```sh
  $ pip3 install -r requirements.txt
  ```

- A similar setup can be created with Docker instead for containerization.

## Usage

### Installation

```sh
$ sudo apt-get install -y python3-pip
$ pip3 install pipenv
```

### Running the Application

To use Py-project-template, first:

```sh
$ git clone https://github.com/Aditya-Diva/py-project-template
$ cd py-project-template
```

To drop into the interactive terminal for the environment:

```
$ pipenv shell
$ python3 main.py
```

Else to run directly:

```sh
$ pipenv run python3 main.py
```

## Contributing

Any contributions made are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

## Contact

Aditya Divakaran - [@LinkedIn](https://www.linkedin.com/in/aditya-divakaran/) - [@Github](https://github.com/Aditya-Diva) - [@GMail](adi.develops@gmail.com)

Notes:

- This was tested on Ubuntu 20.04.
- Refer to [notes](notes.txt) for helpful links on particular framework/tool.
