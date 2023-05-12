# Table of Contents

* [Getting Started](#getting-started)
* [Installation](#installation)
* [Basic usage](#basic-usage)
* [Advance usage](#advance-usage)
* [License](#license)
* [Contributing](#contributing)
* [FAQ](#faq)

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

1. Find specyfic version in repository that coresponds to `1.0.0`:

    ```bash
    version-control find --version 1.0.0
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
    version-control sign --file myapp # Sign your application with version number ie. myapp-0.4.20
```

# License

This software is licensed under the MIT license. See the [LICENSE](LICENSE) file for more information.

# Contributing

This software is open source and contributions are welcome. See the [CONTRIBUTING](CONTRIBUTING.md) file for more information.

# FAQ

1. **Question:** Why my changelog contains strange strings in places related to Github?

    > Make sure that you repository has a remote named `origin` and that you have access to it. This software uses `git log` command to generate changelog and it uses `origin` remote to generate links to commits.

2. **Question:** Why some of my changelog links are not working properly ?

    > Make sure you have all of your commits pushed to remote repository (for example with `git push` command) in order to make hyperlinks work properly.

3. **Question:** Why there are some strange unrendered characters in my changelog ?

    > `version-control` software uses basic inline `HTML` tags to format changelog. Make sure that your markdown renderer supports inline `HTML` tags. It is recommended to use one of VSCode extensions to render markdown files.

4. **Question:** Does `find` module support asterisk wildcards ?

    > Yes, you can use asterisk wildcards in `find` module. For example, you can use `version-control find --author "John*"` to find all versions created by authors with name starting with `John`.