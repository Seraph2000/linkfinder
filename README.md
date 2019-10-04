# linkfinder
Scrapy spider to crawl all links on a website


## Installation

### Requirements
- Python 3.7: https://www.python.org/downloads/
- Terminal: Using Ubuntu 18 terminal in this example. 
- Virtualenv: https://pypi.org/project/virtualenv/
- Scrapy: https://scrapy.org/

#### Create a virtual environment with virtualenv
`virtualenv --python=<path to python> <name of virtual environment>`

#### Enter virtual environment, and install Scrapy inside it, together with any necessary dependencies
`pip install scrapy`

## Running Instructions

### Enter 

`scrapy run links -o <file-name>.<format>`

#### Where the data output could be a .csv, .json, or .xml, for example, depending upon the post processing.


## Trouble Shooting and Optimisation

### Common scraping issues

- It's likely that the owner has made their website dynamic to deter scraping, but it may nevertheless be useful to determine whether a website is dynamic or not
- Dynamic web content
    - solution 1: utilise the Python requests library if the website backend isn't too complex
        - study the requests happening behind the scenes, and or whether cookies are being used. 
    - solution 2: utilise Selenium, if this is not going to impact too much  on speed of scraping
    - solution 3: determine if the website has alternative urls (i.e. containing 'data', or even json formatted pages)

- Robot blocking software
    - software which runs in the background on websites, to protect their data, designed to detect bots
    
- CAPTCHAS
    - if the captcha isn't the latest one, it may be possible to plug in a library such as python-anticaptcha: https://pypi.org/project/python-anticaptcha/
    
![Froggy Weirdness](https://i.imgur.com/kXt1K5G.gif)
