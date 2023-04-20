#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import github, pathlib, argparse, show, find, changlelog
from argparse import RawTextHelpFormatter
import argcomplete

# /* ---------------------------------------------| help |--------------------------------------------- */

DESCRIPTION = """Calculate version or find commit(s) in git repository.

Calculation of version is based on SymVer 2.0.0 (https://semver.org/) i.e:

  * [break] - increases major version (X.0.0)
  * [feat]  - increases minor version (0.X.0)
  * [fix]   - increases patch version (0.0.X)

Commit finding is based on detailed commit schema, where every commit is represented as:

  * version - software version (i.e 1.0.0)
  * hash    - short hash (7 characters)
  * date    - date (day, month, year)
  * time    - time (hour, minute, second)
  * keyword - commit type (i.e [break], [feat], [fix] ...)
  * subject - commit subject (first line of commit message)
  * body    - commit body (all lines of commit message except first line)
  * author  - git user.name of commit author

"""

EPILOG = """Usage examples:

  version calculate - calculate git repository version in current directory
  version calculate -p /path/to/git/repository - calculate git repository version in specified directory
  version find --type fix --author 'John Doe' - find commit(s) in git repository based on type and author

"""

def add_subparser(subparser, name, help, arguments, executor):
    
    parser = subparser.add_parser(name, help=help)

    for argument in arguments:
        parser.add_argument(argument[0], **argument[1])

    parser.set_defaults(func=executor)


# /* ---------------------------------------------| parsers |--------------------------------------------- */

parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, description=DESCRIPTION, epilog=EPILOG)

subparser_operation = parser.add_subparsers(title='operations', help='operations')

add_subparser(subparser_operation, 'find', 'Find commit(s) in git repository', find.ARGUMENTS, find.execute)
add_subparser(subparser_operation, 'show', 'Show git repository version', show.ARGUMENTS, show.execute)
add_subparser(subparser_operation, 'changelog', 'Show git repository changelog', changlelog.ARGUMENTS, changlelog.execute)

args = parser.parse_args()

# /* ---------------------------------------------| main |--------------------------------------------- */

args.func(**vars(args))