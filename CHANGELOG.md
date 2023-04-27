# Table of contents

* [Overview](#overview)
* [Statistics](#statistics)
* [Version history](#version-history)
* [Changelog](#changelog)
# Overview

Remote address:
* **https://github.com/ErnestSzczepaniak/version**

Branches:
* **main [current]** (**19** commits)
* test (**15** commits)

Current version:
* **0.8.1**

Contributors:
* **Ernest Szczepaniak**

# Statistics

Project timeframe:
* **20.04.2023 - 27.04.2023** (8 days)

Code frequency:
* **19** commits (**2.38** / day)

Commit structure:
* **feat** - 8 (42.11%)
* **fix** - 7 (36.84%)
* **style** - 4 (21.05%)

# Version history

* [**0.8.1**](#081)
* [**0.8.0**](#080)
* [**0.7.0**](#070)
* [**0.6.0**](#060)
* [**0.5.1**](#051)
* [**0.5.0-rev.2**](#050-rev2)
* [**0.5.0-rev.1**](#050-rev1)
* [**0.4.0-rev.3**](#040-rev3)
* [**0.4.0-rev.2**](#040-rev2)
* [**0.4.0-rev.1**](#040-rev1)
* [**0.3.2**](#032)
* [**0.3.1**](#031)
* [**0.3.0-rev.2**](#030-rev2)
* [**0.3.0-rev.1**](#030-rev1)
* [**0.2.2**](#022)
* [**0.2.1**](#021)
* [**0.2.0**](#020)
* [**0.1.1**](#011)
* [**0.1.0**](#010)

# Changelog

## **[0.8.1](https://github.com/ErnestSzczepaniak/version/tree/03d32df)**
* **[27.04.2023]** [[03d32df](https://github.com/ErnestSzczepaniak/version/commit/03d32df)] (fix) - remove blank lines (**Ernest Szczepaniak** @ 10:48:38)
   2 files changed (15 insertions, 9 deletions):

   * `CHANGELOG.md [+14, -6]`
   * `main.py [+1, -3]`
## **[0.8.0](https://github.com/ErnestSzczepaniak/version/tree/45c6153)**
* **[27.04.2023]** [[45c6153](https://github.com/ErnestSzczepaniak/version/commit/45c6153)] (feat) - add edit number to each file in files changed section (**Ernest Szczepaniak** @ 10:47:57)
   2 files changed (88 insertions, 69 deletions):

   * `CHANGELOG.md [+33, -26]`
   * `github.py [+2, -1]`
## **[0.7.0](https://github.com/ErnestSzczepaniak/version/tree/2a05e5e)**
* **[27.04.2023]** [[2a05e5e](https://github.com/ErnestSzczepaniak/version/commit/2a05e5e)] (feat) - add files changed tracker with reworked insertions. (**Ernest Szczepaniak** @ 10:25:22)

   ```
   There could be an additional per file changes reportings.
   ```

   6 files changed (185 insertions, 38 deletions):

   * `CHANGELOG.md [+52, -6]`
   * `README.md [+4, -0]`
   * `changlelog.py [+9, -5]`
   * `commit.py [+5, -1]`
   * `difference.py [+0, -3]`
   * `github.py [+7, -4]`
## **[0.6.0](https://github.com/ErnestSzczepaniak/version/tree/ff646ce)**
* **[26.04.2023]** [[ff646ce](https://github.com/ErnestSzczepaniak/version/commit/ff646ce)] (feat) - split changelog to sections (**Ernest Szczepaniak** @ 15:09:03)
   2 files changed (36 insertions, 16 deletions):

   * `CHANGELOG.md [+23, -13]`
   * `changlelog.py [+13, -3]`
## **[0.5.1](https://github.com/ErnestSzczepaniak/version/tree/89e51aa)**
* **[26.04.2023]** [[89e51aa](https://github.com/ErnestSzczepaniak/version/commit/89e51aa)] (fix) - prepare to merge (**Ernest Szczepaniak** @ 14:36:47)
   2 files changed (25 insertions, 20 deletions):

   * `CHANGELOG.md [+22, -19]`
   * `github.py [+3, -1]`
## **[0.5.0-rev.2](https://github.com/ErnestSzczepaniak/version/tree/5864c0f)**
* **[26.04.2023]** [[5864c0f](https://github.com/ErnestSzczepaniak/version/commit/5864c0f)] (style) - change *-rc.X to *-rev.X (**Ernest Szczepaniak** @ 14:17:21)
   2 files changed (18 insertions, 8 deletions):

   * `CHANGELOG.md [+17, -7]`
   * `github.py [+1, -1]`
## **[0.5.0-rev.1](https://github.com/ErnestSzczepaniak/version/tree/6e61149)**
* **[26.04.2023]** [[6e61149](https://github.com/ErnestSzczepaniak/version/commit/6e61149)] (feat) - add release candidates numbering (**Ernest Szczepaniak** @ 14:12:43)

   ```
   when there is a keyword that is not affecting MAJOR, MINOR or PATCH number,
   all succesive releases will be marked as *-rc.X, where X is a number of
   release with same features (but with different styling, performance etc ...).
   ```

   3 files changed (37 insertions, 15 deletions):

   * `CHANGELOG.md [+18, -13]`
   * `commit.py [+1, -1]`
   * `github.py [+18, -1]`
## **[0.4.0-rev.3](https://github.com/ErnestSzczepaniak/version/tree/fd6bd44)**
* **[26.04.2023]** [[fd6bd44](https://github.com/ErnestSzczepaniak/version/commit/fd6bd44)] (style) - add tabs in COMMANDS dictionary (**Ernest Szczepaniak** @ 14:00:17)
   3 files changed (26 insertions, 15 deletions):

   * `CHANGELOG.md [+15, -10]`
   * `changlelog.py [+6, -0]`
   * `github.py [+5, -5]`
## **[0.4.0-rev.2](https://github.com/ErnestSzczepaniak/version/tree/dd41587)**
* **[26.04.2023]** [[dd41587](https://github.com/ErnestSzczepaniak/version/commit/dd41587)] (style) - rework to FORMAT_TABLE and COMMANDS (**Ernest Szczepaniak** @ 13:50:05)
   8 files changed (97 insertions, 93 deletions):

   * `CHANGELOG.md [+20, -9]`
   * `branch.py [+2, -1]`
   * `changlelog.py [+16, -13]`
   * `commit.py [+19, -40]`
   * `difference.py [+6, -0]`
   * `find.py [+1, -1]`
   * `github.py [+28, -22]`
   * `show.py [+2, -4]`
## **[0.4.0-rev.1](https://github.com/ErnestSzczepaniak/version/tree/0c23698)**
* **[21.04.2023]** [[0c23698](https://github.com/ErnestSzczepaniak/version/commit/0c23698)] (feat) - add branches in changelog (**Ernest Szczepaniak** @ 13:11:09)

   ```
   this will help to clarify the repository structure
   ```

   4 files changed (161 insertions, 120 deletions):

   * `CHANGELOG.md [+30, -28]`
   * `branch.py [+2, -0]`
   * `changlelog.py [+18, -12]`
   * `github.py [+3, -0]`
## **[0.3.2](https://github.com/ErnestSzczepaniak/version/tree/36f14bf)**
* **[21.04.2023]** [[36f14bf](https://github.com/ErnestSzczepaniak/version/commit/36f14bf)] (fix) - switch to another branch (**Ernest Szczepaniak** @ 12:51:02)
   5 files changed (194 insertions, 97 deletions):

   * `CHANGELOG.md [+34, -24]`
   * `changlelog.py [+25, -5]`
   * `commit.py [+1, -1]`
   * `find.py [+3, -3]`
   * `github.py [+10, -5]`
## **[0.3.1](https://github.com/ErnestSzczepaniak/version/tree/310b5b9)**
* **[20.04.2023]** [[310b5b9](https://github.com/ErnestSzczepaniak/version/commit/310b5b9)] (fix) - try commit without body (**Ernest Szczepaniak** @ 12:53:39)
   4 files changed (41 insertions, 31 deletions):

   * `CHANGELOG.md [+26, -10]`
   * `changlelog.py [+5, -2]`
   * `commit.py [+2, -2]`
   * `github.py [+8, -17]`
## **[0.3.0-rev.2](https://github.com/ErnestSzczepaniak/version/tree/6abd722)**
* **[20.04.2023]** [[6abd722](https://github.com/ErnestSzczepaniak/version/commit/6abd722)] (style) - add styling (**Ernest Szczepaniak** @ 11:55:29)

   ```
   asda
   asd
   asd
   
   dd2dadasd
   ```

   1 files changed (16 insertions, 0 deletions):

   * `CHANGELOG.md [+16, -0]`
## **[0.3.0-rev.1](https://github.com/ErnestSzczepaniak/version/tree/9dab4b1)**
* **[20.04.2023]** [[9dab4b1](https://github.com/ErnestSzczepaniak/version/commit/9dab4b1)] (feat) - check commit spacing (**Ernest Szczepaniak** @ 11:54:45)

   ```
   1
   2
   3
   
   3
   4
   
   4
   5
   6
   ```

   4 files changed (41 insertions, 50 deletions):

   * `CHANGELOG.md [+24, -35]`
   * `changlelog.py [+4, -6]`
   * `github.py [+5, -3]`
   * `markdown.py [+5, -1]`
## **[0.2.2](https://github.com/ErnestSzczepaniak/version/tree/b48fadf)**
* **[20.04.2023]** [[b48fadf](https://github.com/ErnestSzczepaniak/version/commit/b48fadf)] (fix) - verify changelog creation (**Ernest Szczepaniak** @ 08:56:10)

   ```
   This commit is to verify *.md creation.
   This will try to build up simple changelog based on commit messages and body.
   
   Try with blank space.
   Than text afterwards.
   ```

   6 files changed (89 insertions, 347 deletions):

   * `CHANGELOG.md [+8, -50]`
   * `changlelog.py [+1, -1]`
   * `commit.py [+1, -1]`
   * `find.py [+1, -1]`
   * `github.py [+3, -1]`
   * `markdown.py [+1, -1]`
## **[0.2.1](https://github.com/ErnestSzczepaniak/version/tree/6205f3d)**
* **[20.04.2023]** [[6205f3d](https://github.com/ErnestSzczepaniak/version/commit/6205f3d)] (fix) - newline at end of body (**Ernest Szczepaniak** @ 08:20:47)

   ```
   asd
   asd
   asd
   ```

   1 files changed (1 insertions, 0 deletions):

   * `main.py [+1, -0]`
## **[0.2.0](https://github.com/ErnestSzczepaniak/version/tree/9b1e0a5)**
* **[20.04.2023]** [[9b1e0a5](https://github.com/ErnestSzczepaniak/version/commit/9b1e0a5)] (feat) - test 2 line body (**Ernest Szczepaniak** @ 08:13:21)

   ```
   asdasd
   qweqwe
   qweqwe
   ```

   2 files changed (3 insertions, 0 deletions):

   * `github.py [+2, -1]`
   * `main.py [+1, -0]`
## **[0.1.1](https://github.com/ErnestSzczepaniak/version/tree/86a3303)**
* **[20.04.2023]** [[86a3303](https://github.com/ErnestSzczepaniak/version/commit/86a3303)] (fix) - remove empty spaces (**Ernest Szczepaniak** @ 08:03:50)

   ```
   this will prevent from bad coding practices.
   ```

   2 files changed (1 insertions, 2 deletions):

   * `github.py [+0, -1]`
   * `main.py [+1, -1]`
## **[0.1.0](https://github.com/ErnestSzczepaniak/version/tree/97beafd)**
* **[20.04.2023]** [[97beafd](https://github.com/ErnestSzczepaniak/version/commit/97beafd)] (feat) - add hyperlinks to changelog (**Ernest Szczepaniak** @ 07:53:28)

   ```
   This function works only when internet connection is present and github repository is a public one.
   ```

   11 files changed (690 insertions, 0 deletions):

   * `.gitignore [+2, -0]`
   * `CHANGELOG.md [+58, -0]`
   * `Makefile [+4, -0]`
   * `README.md [+0, -0]`
   * `changlelog.py [+10, -0]`
   * `commit.py [+11, -0]`
   * `find.py [+8, -0]`
   * `github.py [+8, -0]`
   * `main.py [+11, -0]`
   * `markdown.py [+8, -0]`
   * `show.py [+4, -0]`
