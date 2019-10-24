# olmod_serverlist

Show the content of https://olproxy.otl.gg/ in a terminal-friendly format
---
This is a (perhaps excessively) simple Python 3 script that scrapes the [OLMod Server List](https://olproxy.otl.gg/) webpage,
then displays each server listing in a block format (to accomodate narrower terminal windows). 

I made this for two reasons:

- I'm a terminal geek. Why load a webpage if I can run a single command????
- I needed some Python practice anyway. 

---
### What's OLMod?

OLMod is a mod for the game Overload. Overload is a spiritual successor to the Descent series of the 90s. OLMod itself adds some
conspicuously missing multiplayer features to the base game, and is an open source project maintained at https://github.com/arbruijn/olmod

---
## Usage

Being too simple and designed against exactly one webpage, most everything is hardcoded in the script. The following should be sufficient:

```
$ cd $INSTALLDIR/
$ python3 ./olserv.py
``` 
(where $INSTALLDIR is whereever you put the script)

The output will be something like
```
<VEX>Server_Use 'vex-server.de' as PW
        IP: 167.86.101.80
        Players: 5/10
        Map: QUICK1(https://overloadmaps.com/quick1), Mode: Anarchy
        Last Update: Sun Oct 20 2019 19:46:03 GMT+0000 (Coordinated Universal Time)
        Last Game Started: Sun Oct 20 2019 19:25:35 GMT+0000 (Coordinated Universal Time)
        
Notes: Europe, Germany, Use 'vex-server.de' as Password, Intel Xeon E5-2630, 8GB, 1GB NIC

************
...
```
---

## Setup

The script was made with `pipenv` in order to install the BeautifulSoup library. Making this into a proper package is on the to-do
list, but in the meantime, do either:

* Install BeautifulSoup with your distro's package manager
* Install beautifulsoup4 with `pip`
* or install Pipenv, clone this repo, and run `pipenv install` inside the repo's directory. Highly recommend this option--pipenv is awesome.
