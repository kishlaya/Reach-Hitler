# Reach Hitler

There was a post on [r/greentext](https://www.reddit.com/r/greentext/comments/cop674/anon_plays_a_game/) about reaching Hitler in 5 steps from a random wiki. 
I had just finished my exams a few days back and so had some free time right now.
Also, I have never done web scraping before so I thought let's do it now. Hee I go!

![greentext](greentext.jpg)

## What it does?
It starts the /Special:Random wiki and then does a "BFS" search to see if the Adolf Hitler Wiki is reachable from that page in 5 steps

## TODO
* Really slow as it loads the entire wiki page each time (in particular, find some way to only load the required text and skip images)
* Add graph structure to backtrack parent links

## Installation
```shell
$ pip3 install beautifulsoup4
$ pip3 install grequests
```

## Run
```shell
$ python3 reach.py
```
