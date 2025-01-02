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
|Day|2015|2019|2022|2023|2024|Total|
|-:|:-:|:-:|:-:|:-:|:-:|:-:|
|%|32/50|4/50|20/50|22/50|50/50|128/550|
|1|🌟🌟|🌟🌟|🌟🌟|🌟🌟|🌟🌟|10🌟|
|2|🌟🌟|🌟🌟|🌟🌟|🌟🌟|🌟🌟|10🌟|
|3|🌟🌟|-|🌟🌟|🌟🌟|🌟🌟|8🌟|
|4|🌟🌟|-|🌟🌟|🌟🌟|🌟🌟|8🌟|
|5|🌟🌟|-|🌟🌟|🌟🌟|🌟🌟|8🌟|
|6|🌟🌟|-|🌟🌟|🌟🌟|🌟🌟|8🌟|
|7|🌟🌟|-|🌟🌟|🌟🌟|🌟🌟|8🌟|
|8|🌟🌟|-|🌟🌟|🌟🌟|🌟🌟|8🌟|
|9|🌟🌟|-|🌟🌟|🌟🌟|🌟🌟|8🌟|
|10|🌟🌟|-|🌟🌟|🌟🌟|🌟🌟|8🌟|
|11|🌟🌟|-|-|🌟🌟|🌟🌟|6🌟|
|12|🌟🌟|-|-|-|🌟🌟|4🌟|
|13|🌟🌟|-|-|-|🌟🌟|4🌟|
|14|🌟🌟|-|-|-|🌟🌟|4🌟|
|15|🌟🌟|-|-|-|🌟🌟|4🌟|
|16|🌟🌟|-|-|-|🌟🌟|4🌟|
|17|-|-|-|-|🌟🌟|2🌟|
|18|-|-|-|-|🌟🌟|2🌟|
|19|-|-|-|-|🌟🌟|2🌟|
|20|-|-|-|-|🌟🌟|2🌟|
|21|-|-|-|-|🌟🌟|2🌟|
|22|-|-|-|-|🌟🌟|2🌟|
|23|-|-|-|-|🌟🌟|2🌟|
|24|-|-|-|-|🌟🌟|2🌟|
|25|-|-|-|-|🌟🌟|2🌟|


### Time
In python, ran on my laptop. I _want_ to say I took the average of 10 runs, but I probably did not.

|Day|2015|2019|2022|2023|2024|Total|
|-:|:-:|:-:|:-:|:-:|:-:|:-:|
|All|<span class="decent">`18.8s`</span>|<span class="perfect">`160.6ms`</span>|<span class="perfect">`696.0ms`</span>|<span class="good">`5.2s`</span>|<span class="bad">`262.2s`</span>|<span class="bad">`287.1s`</span>|
|1|<span class="perfect">`63.9ms`</span>|<span class="perfect">`67.9ms`</span>|<span class="perfect">`62.1ms`</span>|<span class="perfect">`107.9ms`</span>|<span class="perfect">`83.1ms`</span>|<span class="perfect">`384.9ms`</span>|
|2|<span class="perfect">`67.6ms`</span>|<span class="perfect">`92.7ms`</span>|<span class="perfect">`55.5ms`</span>|<span class="perfect">`62.3ms`</span>|<span class="perfect">`63.5ms`</span>|<span class="perfect">`341.7ms`</span>|
|3|<span class="perfect">`73.7ms`</span>|-|<span class="perfect">`56.0ms`</span>|<span class="perfect">`65.8ms`</span>|<span class="perfect">`76.0ms`</span>|<span class="perfect">`271.5ms`</span>|
|4|<span class="good">`4.0s`</span>|-|<span class="perfect">`75.9ms`</span>|<span class="good">`2.3s`</span>|<span class="perfect">`95.2ms`</span>|<span class="good">`6.5s`</span>|
|5|<span class="perfect">`104.9ms`</span>|-|<span class="perfect">`58.7ms`</span>|<span class="perfect">`85.0ms`</span>|<span class="perfect">`97.2ms`</span>|<span class="perfect">`345.9ms`</span>|
|6|<span class="good">`4.4s`</span>|-|<span class="perfect">`58.6ms`</span>|<span class="good">`1.1s`</span>|<span class="good">`4.4s`</span>|<span class="good">`10.0s`</span>|
|7|<span class="perfect">`65.2ms`</span>|-|<span class="perfect">`79.2ms`</span>|<span class="perfect">`765.7ms`</span>|<span class="good">`1.6s`</span>|<span class="good">`2.5s`</span>|
|8|<span class="perfect">`75.7ms`</span>|-|<span class="perfect">`85.3ms`</span>|<span class="perfect">`116.0ms`</span>|<span class="perfect">`68.8ms`</span>|<span class="perfect">`345.9ms`</span>|
|9|<span class="perfect">`178.0ms`</span>|-|<span class="perfect">`109.1ms`</span>|<span class="perfect">`78.6ms`</span>|<span class="decent">`13.4s`</span>|<span class="decent">`13.7s`</span>|
|10|<span class="good">`4.0s`</span>|-|<span class="perfect">`55.6ms`</span>|<span class="perfect">`105.4ms`</span>|<span class="perfect">`72.3ms`</span>|<span class="good">`4.3s`</span>|
|11|<span class="good">`3.6s`</span>|-|-|<span class="perfect">`302.1ms`</span>|<span class="perfect">`133.7ms`</span>|<span class="good">`4.1s`</span>|
|12|<span class="perfect">`88.3ms`</span>|-|-|-|<span class="good">`3.0s`</span>|<span class="good">`3.1s`</span>|
|13|<span class="perfect">`873.8ms`</span>|-|-|-|<span class="perfect">`66.3ms`</span>|<span class="perfect">`940.2ms`</span>|
|14|<span class="perfect">`78.4ms`</span>|-|-|-|<span class="good">`2.1s`</span>|<span class="good">`2.1s`</span>|
|15|<span class="good">`1.0s`</span>|-|-|-|<span class="perfect">`134.0ms`</span>|<span class="good">`1.1s`</span>|
|16|<span class="perfect">`104.1ms`</span>|-|-|-|<span class="bad">`151.2s`</span>|<span class="bad">`151.3s`</span>|
|17|-|-|-|-|<span class="perfect">`69.4ms`</span>|<span class="perfect">`69.4ms`</span>|
|18|-|-|-|-|<span class="good">`7.3s`</span>|<span class="good">`7.3s`</span>|
|19|-|-|-|-|<span class="good">`2.6s`</span>|<span class="good">`2.6s`</span>|
|20|-|-|-|-|<span class="good">`3.2s`</span>|<span class="good">`3.2s`</span>|
|21|-|-|-|-|<span class="perfect">`76.2ms`</span>|<span class="perfect">`76.2ms`</span>|
|22|-|-|-|-|<span class="decent">`19.4s`</span>|<span class="decent">`19.4s`</span>|
|23|-|-|-|-|<span class="decent">`53.1s`</span>|<span class="decent">`53.1s`</span>|
|24|-|-|-|-|<span class="perfect">`86.2ms`</span>|<span class="perfect">`86.2ms`</span>|
|25|-|-|-|-|<span class="perfect">`95.2ms`</span>|<span class="perfect">`95.2ms`</span>|


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
