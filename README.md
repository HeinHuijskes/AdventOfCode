# Advent of code
My solutions to different years of advent of code, as well as a small python framework that attempts to smooth out data retrieval and the code writing process.

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
Love them. No coloured formatting though, GH seems to strip it.


### Completion
|Day|2015|2016|2019|2022|2023|2024|2025|Total|
|-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|%|50/50|14/50|4/50|22/50|22/50|50/50|16/50|178/550|
|1|🌟🌟|🌟🌟|🌟🌟|🌟🌟|🌟🌟|🌟🌟|🌟🌟|14🌟|
|2|🌟🌟|🌟🌟|🌟🌟|🌟🌟|🌟🌟|🌟🌟|🌟🌟|14🌟|
|3|🌟🌟|🌟🌟|-|🌟🌟|🌟🌟|🌟🌟|🌟🌟|12🌟|
|4|🌟🌟|🌟🌟|-|🌟🌟|🌟🌟|🌟🌟|🌟🌟|12🌟|
|5|🌟🌟|🌟🌟|-|🌟🌟|🌟🌟|🌟🌟|🌟🌟|12🌟|
|6|🌟🌟|🌟🌟|-|🌟🌟|🌟🌟|🌟🌟|🌟🌟|12🌟|
|7|🌟🌟|🌟🌟|-|🌟🌟|🌟🌟|🌟🌟|🌟🌟|12🌟|
|8|🌟🌟|-|-|🌟🌟|🌟🌟|🌟🌟|🌟🌟|10🌟|
|9|🌟🌟|-|-|🌟🌟|🌟🌟|🌟🌟|-|8🌟|
|10|🌟🌟|-|-|🌟🌟|🌟🌟|🌟🌟|-|8🌟|
|11|🌟🌟|-|-|-|🌟🌟|🌟🌟|-|6🌟|
|12|🌟🌟|-|-|🌟🌟|-|🌟🌟|-|6🌟|
|13|🌟🌟|-|-|-|-|🌟🌟|-|4🌟|
|14|🌟🌟|-|-|-|-|🌟🌟|-|4🌟|
|15|🌟🌟|-|-|-|-|🌟🌟|-|4🌟|
|16|🌟🌟|-|-|-|-|🌟🌟|-|4🌟|
|17|🌟🌟|-|-|-|-|🌟🌟|-|4🌟|
|18|🌟🌟|-|-|-|-|🌟🌟|-|4🌟|
|19|🌟🌟|-|-|-|-|🌟🌟|-|4🌟|
|20|🌟🌟|-|-|-|-|🌟🌟|-|4🌟|
|21|🌟🌟|-|-|-|-|🌟🌟|-|4🌟|
|22|🌟🌟|-|-|-|-|🌟🌟|-|4🌟|
|23|🌟🌟|-|-|-|-|🌟🌟|-|4🌟|
|24|🌟🌟|-|-|-|-|🌟🌟|-|4🌟|
|25|🌟🌟|-|-|-|-|🌟🌟|-|4🌟|


### Time
In python, ran on my laptop. I _want_ to say I took the average of 10 runs, but I probably did not.

|Day|2015|2016|2019|2022|2023|2024|2025|Total|
|-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|All|<span class="bad">`396.8s`</span>|<span class="decent">`30.7s`</span>|<span class="perfect">`174.7ms`</span>|<span class="good">`1.8s`</span>|<span class="good">`4.0s`</span>|<span class="bad">`254.8s`</span>|<span class="good">`3.7s`</span>|<span class="bad">`692.0s`</span>|
|1|<span class="perfect">`64.0ms`</span>|<span class="perfect">`63.7ms`</span>|<span class="perfect">`72.4ms`</span>|<span class="perfect">`73.1ms`</span>|<span class="perfect">`160.7ms`</span>|<span class="perfect">`107.9ms`</span>|<span class="perfect">`2.2ms`</span>|<span class="perfect">`544.0ms`</span>|
|2|<span class="perfect">`65.7ms`</span>|<span class="perfect">`74.2ms`</span>|<span class="perfect">`102.3ms`</span>|<span class="perfect">`72.5ms`</span>|<span class="perfect">`74.8ms`</span>|<span class="perfect">`89.6ms`</span>|<span class="good">`2.6s`</span>|<span class="good">`3.1s`</span>|
|3|<span class="perfect">`67.3ms`</span>|<span class="perfect">`107.4ms`</span>|-|<span class="perfect">`75.4ms`</span>|<span class="perfect">`83.5ms`</span>|<span class="perfect">`103.0ms`</span>|<span class="perfect">`2.8ms`</span>|<span class="perfect">`439.4ms`</span>|
|4|<span class="good">`4.4s`</span>|<span class="perfect">`71.3ms`</span>|-|<span class="perfect">`92.6ms`</span>|<span class="good">`2.2s`</span>|<span class="perfect">`116.0ms`</span>|<span class="perfect">`228.2ms`</span>|<span class="good">`7.1s`</span>|
|5|<span class="perfect">`109.1ms`</span>|<span class="decent">`30.2s`</span>|-|<span class="perfect">`87.5ms`</span>|<span class="perfect">`92.6ms`</span>|<span class="perfect">`120.7ms`</span>|<span class="perfect">`8.0ms`</span>|<span class="decent">`30.6s`</span>|
|6|<span class="good">`4.2s`</span>|<span class="perfect">`60.5ms`</span>|-|<span class="perfect">`79.2ms`</span>|<span class="perfect">`104.6ms`</span>|<span class="good">`4.7s`</span>|<span class="perfect">`18.5ms`</span>|<span class="good">`9.1s`</span>|
|7|<span class="perfect">`78.1ms`</span>|<span class="perfect">`184.5ms`</span>|-|<span class="perfect">`93.3ms`</span>|<span class="perfect">`685.6ms`</span>|<span class="good">`1.6s`</span>|<span class="perfect">`6.0ms`</span>|<span class="good">`2.6s`</span>|
|8|<span class="perfect">`73.0ms`</span>|-|-|<span class="perfect">`99.7ms`</span>|<span class="perfect">`99.1ms`</span>|<span class="perfect">`86.5ms`</span>|<span class="perfect">`833.0ms`</span>|<span class="good">`1.2s`</span>|
|9|<span class="perfect">`180.7ms`</span>|-|-|<span class="perfect">`113.1ms`</span>|<span class="perfect">`91.0ms`</span>|<span class="decent">`14.0s`</span>|-|<span class="decent">`14.3s`</span>|
|10|<span class="good">`3.5s`</span>|-|-|<span class="perfect">`70.1ms`</span>|<span class="perfect">`117.2ms`</span>|<span class="perfect">`112.0ms`</span>|-|<span class="good">`3.8s`</span>|
|11|<span class="good">`2.9s`</span>|-|-|-|<span class="perfect">`295.7ms`</span>|<span class="perfect">`146.7ms`</span>|-|<span class="good">`3.3s`</span>|
|12|<span class="perfect">`102.2ms`</span>|-|-|<span class="perfect">`928.2ms`</span>|-|<span class="good">`3.0s`</span>|-|<span class="good">`4.0s`</span>|
|13|<span class="perfect">`976.3ms`</span>|-|-|-|-|<span class="perfect">`110.9ms`</span>|-|<span class="good">`1.1s`</span>|
|14|<span class="perfect">`73.9ms`</span>|-|-|-|-|<span class="good">`2.1s`</span>|-|<span class="good">`2.2s`</span>|
|15|<span class="good">`1.1s`</span>|-|-|-|-|<span class="perfect">`152.0ms`</span>|-|<span class="good">`1.2s`</span>|
|16|<span class="perfect">`116.4ms`</span>|-|-|-|-|<span class="bad">`144.4s`</span>|-|<span class="bad">`144.5s`</span>|
|17|<span class="bad">`361.9s`</span>|-|-|-|-|<span class="perfect">`90.8ms`</span>|-|<span class="bad">`362.0s`</span>|
|18|<span class="good">`4.9s`</span>|-|-|-|-|<span class="good">`7.7s`</span>|-|<span class="decent">`12.6s`</span>|
|19|<span class="perfect">`90.0ms`</span>|-|-|-|-|<span class="good">`2.8s`</span>|-|<span class="good">`2.9s`</span>|
|20|<span class="good">`5.8s`</span>|-|-|-|-|<span class="good">`3.3s`</span>|-|<span class="good">`9.2s`</span>|
|21|<span class="perfect">`76.1ms`</span>|-|-|-|-|<span class="perfect">`88.6ms`</span>|-|<span class="perfect">`164.7ms`</span>|
|22|<span class="good">`2.4s`</span>|-|-|-|-|<span class="decent">`18.4s`</span>|-|<span class="decent">`20.8s`</span>|
|23|<span class="perfect">`61.6ms`</span>|-|-|-|-|<span class="decent">`51.3s`</span>|-|<span class="decent">`51.4s`</span>|
|24|<span class="good">`1.9s`</span>|-|-|-|-|<span class="perfect">`107.3ms`</span>|-|<span class="good">`2.0s`</span>|
|25|<span class="good">`1.5s`</span>|-|-|-|-|<span class="perfect">`113.2ms`</span>|-|<span class="good">`1.6s`</span>|


<style>
    .perfect {
        /* 100%; 1-1000 ms */
        color: green;
    }
    .quitegood {
        color: lightgreen;
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
        /* 1-1000 Î¼s */
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
