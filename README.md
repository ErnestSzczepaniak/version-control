# Table of Contents

* [Getting Started](#getting-started)
* [Installation](#installation)
* [Basic usage](#basic-usage)
* [Advance usage](#advance-usage)
* [License](#license)
* [Contributing](#contributing)

# Getting Started

This software tool is designed to help with version control of software projects. It is designed to work with git repositories and it is written in Python.

It uses a combination of git tags and git commits to calculate the current version of the software. It also allows you to generate a changelog file based on git commits.

Version calculation is based on:

* [SymVer 2.0.0](https://semver.org/)
* [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)

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

# Basic usage

Typical usage of this software is as follows:

1. Calculate and show current software version in current repository:

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

4. Find all versions of the software in current repository and change output schema to `version` + `date` pair:

    ```bash
    version-control find --schema version date
    ```

5. Generate a changelog file and save it to specified location:

    ```bash
    version-control generate --output docs/CHANGELOG.md
    ```

6. Sign a file with current repository version (i.e rename a file to `file-version`):

    ```bash
    version-control sign --file file
    ```

# Advance usage

This software was build to support CI/CD procedure for standalone project. You can use it to automate versioning and changelog generation.

For example, you can use it in your `Makefile` to automate versioning and changelog generation by adding this target:

```makefile
release:
    git add . && git commit # Commit all changes to update version
    g++ -o myapp main.cpp # Build your application
    version-control generate --output CHANGELOG.md # Generate changelog
    version-control find --schema version date > VERSIONS.txt # Save version history
    version-control sign --file myapp # Sign your application with version number ie. myapp-1.0.0
```

# License

This software is licensed under the MIT license. See the [LICENSE](LICENSE) file for more information.

# Contributing

This software is open source and contributions are welcome. See the [CONTRIBUTING](CONTRIBUTING.md) file for more information.