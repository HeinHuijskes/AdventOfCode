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
|Day|2015|2019|2022|2023|2024|Total|
|-:|:-:|:-:|:-:|:-:|:-:|:-:|
|%|32%|16%|40%|12%|80%|3.6%|
|1|🌟🌟|🌟🌟|🌟🌟|🌟🌟|🌟🌟|10🌟|
|2|🌟🌟|🌟🌟|🌟🌟|🌟🌟|🌟🌟|10🌟|
|3|🌟🌟|🌟🌟|🌟🌟|🌟🌟|🌟🌟|10🌟|
|4|🌟🌟|🌟🌟|🌟🌟|-|🌟🌟|8🌟|
|5|🌟🌟|-|🌟🌟|-|🌟🌟|6🌟|
|6|🌟🌟|-|🌟🌟|-|🌟🌟|6🌟|
|7|🌟🌟|-|🌟🌟|-|🌟🌟|6🌟|
|8|🌟🌟|-|🌟🌟|-|🌟🌟|6🌟|
|9|-|-|🌟🌟|-|🌟🌟|4🌟|
|10|-|-|🌟🌟|-|🌟🌟|4🌟|
|11|-|-|-|-|🌟🌟|2🌟|
|12|-|-|-|-|🌟🌟|2🌟|
|13|-|-|-|-|🌟🌟|2🌟|
|14|-|-|-|-|🌟🌟|2🌟|
|15|-|-|-|-|🌟🌟|2🌟|
|16|-|-|-|-|🌟🌟|2🌟|
|17|-|-|-|-|🌟🌟|2🌟|
|18|-|-|-|-|🌟🌟|2🌟|
|19|-|-|-|-|🌟🌟|2🌟|
|20|-|-|-|-|🌟🌟|2🌟|
|21|-|-|-|-|-|-|
|22|-|-|-|-|-|-|
|23|-|-|-|-|-|-|
|24|-|-|-|-|-|-|
|25|-|-|-|-|-|-|

### Time
|Day|2015|2019|2022|2023|2024|Total|
|-:|:-:|:-:|:-:|:-:|:-:|:-:|
|All|<span class="good">`8.9s`</span>|<span class="good">`1.6s`</span>|<span class="perfect">`696.0ms`</span>|<span class="perfect">`236.0ms`</span>|<span class="bad">`189.5s`</span>|<span class="bad">`200.9s`</span>|
|1|<span class="perfect">`63.9ms`</span>|<span class="perfect">`67.9ms`</span>|<span class="perfect">`62.1ms`</span>|<span class="perfect">`107.9ms`</span>|<span class="perfect">`83.1ms`</span>|<span class="perfect">`384.9ms`</span>|
|2|<span class="perfect">`67.6ms`</span>|<span class="perfect">`92.7ms`</span>|<span class="perfect">`55.5ms`</span>|<span class="perfect">`62.3ms`</span>|<span class="perfect">`63.5ms`</span>|<span class="perfect">`341.7ms`</span>|
|3|<span class="perfect">`73.7ms`</span>|<span class="perfect">`110.5ms`</span>|<span class="perfect">`56.0ms`</span>|<span class="perfect">`65.8ms`</span>|<span class="perfect">`76.0ms`</span>|<span class="perfect">`382.0ms`</span>|
|4|<span class="good">`4.0s`</span>|<span class="good">`1.3s`</span>|<span class="perfect">`75.9ms`</span>|-|<span class="perfect">`95.2ms`</span>|<span class="good">`5.4s`</span>|
|5|<span class="perfect">`104.9ms`</span>|-|<span class="perfect">`58.7ms`</span>|-|<span class="perfect">`97.2ms`</span>|<span class="perfect">`260.8ms`</span>|
|6|<span class="good">`4.4s`</span>|-|<span class="perfect">`58.6ms`</span>|-|<span class="good">`4.4s`</span>|<span class="good">`8.9s`</span>|
|7|<span class="perfect">`65.2ms`</span>|-|<span class="perfect">`79.2ms`</span>|-|<span class="good">`1.6s`</span>|<span class="good">`1.7s`</span>|
|8|<span class="perfect">`130.9ms`</span>|-|<span class="perfect">`85.3ms`</span>|-|<span class="perfect">`68.8ms`</span>|<span class="perfect">`285.1ms`</span>|
|9|-|-|<span class="perfect">`109.1ms`</span>|-|<span class="decent">`13.4s`</span>|<span class="decent">`13.5s`</span>|
|10|-|-|<span class="perfect">`55.6ms`</span>|-|<span class="perfect">`72.3ms`</span>|<span class="perfect">`127.9ms`</span>|
|11|-|-|-|-|<span class="perfect">`133.7ms`</span>|<span class="perfect">`133.7ms`</span>|
|12|-|-|-|-|<span class="good">`3.0s`</span>|<span class="good">`3.0s`</span>|
|13|-|-|-|-|<span class="perfect">`66.3ms`</span>|<span class="perfect">`66.3ms`</span>|
|14|-|-|-|-|<span class="good">`2.1s`</span>|<span class="good">`2.1s`</span>|
|15|-|-|-|-|<span class="perfect">`134.0ms`</span>|<span class="perfect">`134.0ms`</span>|
|16|-|-|-|-|<span class="bad">`151.2s`</span>|<span class="bad">`151.2s`</span>|
|17|-|-|-|-|<span class="perfect">`69.4ms`</span>|<span class="perfect">`69.4ms`</span>|
|18|-|-|-|-|<span class="good">`7.3s`</span>|<span class="good">`7.3s`</span>|
|19|-|-|-|-|<span class="good">`2.6s`</span>|<span class="good">`2.6s`</span>|
|20|-|-|-|-|<span class="good">`3.2s`</span>|<span class="good">`3.2s`</span>|
|21|-|-|-|-|-|-|
|22|-|-|-|-|-|-|
|23|-|-|-|-|-|-|
|24|-|-|-|-|-|-|
|25|-|-|-|-|-|-|