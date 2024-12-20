<style>
    .perfect {
        /* 100%; 1-1000 ms */
        color: green;
    }
    .good {
        /* 50-100%; 1-10 s */
        color: yellow;
    }
    .decent {
        /* 10-50%; 10-100 s */
        color: orange;
    }
    .bad {
        /* 0-10%; 100+ s */
        color: red;
    }
    .insane {
        /* 1-1000 μs */
        color: blue;
    }
    .impossible {
        /* <1000 ns */
        color: purple;
    }
    .horrendous {
        /* >100 s */
        color: black;
    }

</style>

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

## Stats
Love them.
### Completion
|Day|2015|2019|2020|2021|2022|2023|2024|All|
|-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|%|<span class="decent">28%</span>|<span class="bad">8%</span>|<span class="bad">0%</span>|<span class="bad">0%</span>|<span class="decent">48%</span>|<span class="decent">44%</span>|<span class="good">80%</span>|<span class="decent">8.0%</span>|
|1|🌟🌟|🌟🌟|-|-|🌟🌟|🌟🌟|🌟🌟|10🌟|
|2|🌟🌟|🌟🌟|-|-|🌟🌟|🌟🌟|🌟🌟|10🌟|
|3|🌟🌟|-|-|-|🌟🌟|🌟🌟|🌟🌟|8🌟|
|4|🌟🌟|-|-|-|🌟🌟|🌟🌟|🌟🌟|8🌟|
|5|🌟🌟|-|-|-|🌟🌟|🌟🌟|🌟🌟|8🌟|
|6|🌟🌟|-|-|-|🌟🌟|🌟🌟|🌟🌟|8🌟|
|7|🌟🌟|-|-|-|🌟🌟|🌟🌟|🌟🌟|8🌟|
|8|-|-|-|-|🌟🌟|🌟🌟|🌟🌟|6🌟|
|9|-|-|-|-|🌟🌟|🌟🌟|🌟🌟|6🌟|
|10|-|-|-|-|🌟🌟|🌟🌟|🌟🌟|6🌟|
|11|-|-|-|-|🌟🌟|🌟🌟|🌟🌟|6🌟|
|12|-|-|-|-|🌟🌟|-|🌟🌟|4🌟|
|13|-|-|-|-|-|-|🌟🌟|2🌟|
|14|-|-|-|-|-|-|🌟🌟|2🌟|
|15|-|-|-|-|-|-|🌟🌟|2🌟|
|16|-|-|-|-|-|-|🌟🌟|2🌟|
|17|-|-|-|-|-|-|🌟🌟|2🌟|
|18|-|-|-|-|-|-|🌟🌟|2🌟|
|19|-|-|-|-|-|-|🌟🌟|2🌟|
|20|-|-|-|-|-|-|🌟🌟|2🌟|
|21|-|-|-|-|-|-|-|-|
|22|-|-|-|-|-|-|-|-|
|23|-|-|-|-|-|-|-|-|
|24|-|-|-|-|-|-|-|-|
|25|-|-|-|-|-|-|-|-|

### Time
In python, ran on my laptop. I _want_ to say I took the average over 10 runs, but I did not.
|Day|2015|2019|2020|2021|2022|2023|2024|All|
|-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Total|-|-|-|-|-|-|<span class="bad">`>176 s`</span>|<span class="bad">`>176 s`</span>|
|1|-|-|-|-|-|-|<span class="perfect">`97.8 ms`</span>|<span class="perfect">`97.8 ms`</span>|
|2|-|-|-|-|-|-|<span class="perfect">`70.8 ms`</span>|<span class="perfect">`70.8 ms`</span>|
|3|-|-|-|-|-|-|<span class="perfect">`80.8 ms`</span>|-|
|4|-|-|-|-|-|-|<span class="perfect">`97.1 ms`</span>|-|
|5|-|-|-|-|-|-|<span class="perfect">`98.1 ms`</span>|-|
|6|-|-|-|-|-|-|<span class="good">`4.2 s`</span>|-|
|7|-|-|-|-|-|-|<span class="good">`1.6 s`</span>|-|
|8|-|-|-|-|-|-|<span class="perfect">`69.0 ms`</span>|-|
|9|-|-|-|-|-|-|<span class="decent">`13.8 s`</span>|-|
|10|-|-|-|-|-|-|<span class="perfect">`69.6 ms`</span>|-|
|11|-|-|-|-|-|-|<span class="perfect">`100 ms`</span>|-|
|12|-|-|-|-|-|-|<span class="good">`2.7 s`</span>|-|
|13|-|-|-|-|-|-|<span class="perfect">`67.8 ms`</span>|-|
|14|-|-|-|-|-|-|<span class="good">`1.8 s`</span>|-|
|15|-|-|-|-|-|-|<span class="perfect">`100 ms`</span>|-|
|16|-|-|-|-|-|-|<span class="bad">`138.7 s`</span>|-|
|17|-|-|-|-|-|-|<span class="perfect">`64.1 ms`</span>|-|
|18|-|-|-|-|-|-|<span class="good">`7.5 s`</span>|-|
|19|-|-|-|-|-|-|<span class="good">`2.8 s`</span>|-|
|20|-|-|-|-|-|-|<span class="good">`3.3 s`</span>|-|
|21|-|-|-|-|-|-|-|-|
|22|-|-|-|-|-|-|-|-|
|23|-|-|-|-|-|-|-|-|
|24|-|-|-|-|-|-|-|-|
|25|-|-|-|-|-|-|-|-|