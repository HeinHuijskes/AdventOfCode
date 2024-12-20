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
|2024|<span style="color:green">97.8 ms</span>|<span style="color:green">70.8 ms</span>|<span style="color:green">80.8 ms</span>|<span style="color:green">97.1 ms</span>|<span style="color:green">98.1 ms</span>|<span style="color:blue">4.2 s</span>|<span style="color:lightblue">1.6 s</span>|<span style="color:green">69.0 ms</span>|<span style="color:red">13.8 s</span>|<span style="color:green">69.6 ms</span>|<span style="color:blue">0.1 s</span>|<span style="color:blue">2.7 s</span>|<span style="color:green">67.8 ms</span>|<span style="color:blue">1.8 s</span>|<span style="color:blue">0.1 s</span>|<span style="color:red">138.7 s</span>|<span style="color:green">64.1 ms</span>|<span style="color:blue">7.5 s</span>|<span style="color:blue">2.8 s</span>|<span style="color:blue">3.3 s</span>|-|-|-|-|-|80.0

Total completed: 8.0%