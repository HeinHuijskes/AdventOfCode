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

### Years completed & times
In python, averaged over 10 runs on my laptop
|Year|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|%
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
|2024|76.3 ms|57.2 ms|65.3 ms|83.7 ms|93.9 ms|4.3 s|1.6 s|54.2 ms|14.0 s|61.2 ms|0.1 s|2.9 s|53.5 ms|-|-|-|-|-|-|-|-|-|-|-|-|52.0

Total completed: 5.2%