# Advent of code
My solutions to different years of advent of code, as well as a small python framework that attempts to smooth out data retrieval and the code writing process.  

It also contains a java framework, which was closely adapted from `Day.java` of the [version](https://github.com/Mathijs-Vogelezang/AdventOfCode/blob/master/src/main/java/common/Day.java) of [Mathijs Vogelezang](https://github.com/Mathijs-Vogelezang).

## Requirements
### Python
Requires python 3.0 or above. Probably. I have not tested it below.

### Requests package
Install the python requests package.
> ```$ python -m pip install requests```

### Cookie
Add a `cookie.txt` file to the framework folder, containing the value of the cookie from a logged-in http request to https://adventofcode.com. It is valid for about a month, enough for all of AoC each year.

## Usage
Run `Run.py` to generate files for the current day. Add a solution to those files, and run them to try and find the right answer.
