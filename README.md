# Table of Contents

* [Getting Started](#getting-started)
* [Installation](#installation)
* [Usage](#usage)
* [License](#license)
* [Contributing](#contributing)

# Getting Started

This software tool is designed to help with version control of software projects. It is designed to work with git repositories and it is written in Python.

It uses a combination of git tags and git commits to calculate the current version of the software. It also allows you to generate a changelog file based on git commits.

Version calculation is based on SymVer 2.0.0 specification. For more information about SymVer, see [https://semver.org/](https://semver.org/) and conventional commits specification [https://www.conventionalcommits.org/en/v1.0.0/](https://www.conventionalcommits.org/en/v1.0.0/).

The default keywords used to calculate the version are:

* `break` - for breaking changes
* `feat` - for new features
* `fix` - for bug fixes

All other keywords are treated as non changing the version, but they are forming a release candidate (`.rcX`).

# Installation

This software requires the following packages to be installed:

* `python3`
* `python3-pip`
* `pyinstaller`

You can install these packages on Ubuntu with the following command:

```bash
sudo make configure
```

After satysfying the above requirements, you can build the executable of this software with the following command:

```bash
make build
```

To finish installation, all necessary files mute be copied to coresponding directories. This can be done with the following command:

```bash
sudo make install
```

This script does the following:

1. Copies the `version-control` executable to `/usr/local/bin`
2. Copies bash autocompletion script to `/etc/bash_completion.d`
3. Creates a shortcut symbolic link named `vc` in `/usr/local/bin` to the main executable

# Usage

Typical usage of this software is as follows:

1. Calculate and show curretn software version in current repository:

    ```bash
    version-control show
    ```

2. Find all versions of the software in specyfic repository:

    ```bash
    version-control find --path /home/user/Projects/MyProject
    ```

3. Find all version of the software in current repository, filter by author and show result is json format:

    ```bash
    version-control find --author "John Doe" --format json
    ```

4. Generate a changelog file and save it to specified location:

    ```bash
    version-control generate --output docs/CHANGELOG.md
    ```

5. Sign a file with current repository version (i.e rename a file to `file-version`):

    ```bash
    version-control sign --file file
    ```

# License

This software is licensed under the MIT license. See the [LICENSE](LICENSE) file for more information.

# Contributing
