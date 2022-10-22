---
title: 'Scraping & Analyzing Job Postings'
subtitle: 'with Python: Selenium and BeautifulSoup'
date: 2022-10-01 00:00:00
description: I queried Indeed.com for jobs with the keywords Data Analyst & Scientist, and Business Analyst & Intelligence to get a sense of the most demanded skills for these positions, and identifying employees with growing data teams.
featured_image: '/images/IndeedScraper/indeed-scraping.png'
---
# Data Analytics on Data Analytics

## Purpose

Data Engineering, Analytics, Science & corresponding Machine Learning Engineering can be an overwhelming field with an even more **overwhelming amount of tools** that *might* be **necessary for landing a job** in that business. Hence, in order to better understand if I am on the right path with Excel, SQL, Python and PowerBI as my *go-to* tools, I decided on checking in on **current job descriptions and the demanded skills**.  
Again, with Selenium (see Price Research project) I scraped Indeed.com for job postings in Munich showing for the keywords...
- *Data Analyst (DA)* 
- *Data Scientist (DS)*
  ... as these are the jobs I am most interested in, and for which I learned the most through courses. And I added...
- *Business Analyst (BA)*
- *Business Intelligence (BI)*
... to the list, since I am / was working in BI at IVECO. Additionally, I need to note that I did not actively look for jobs in...
- *Data Engineering (DE)*
- *Machine Learning Engineering (MLE)*
... since I do not see myself fully qualified for this positions, **yet!** However, as you will see, some job postings for DE & MLE showed up nonetheless.

## Methods
I followed the classic ETL procedure

### Extract
As mentioned before, I used the Selenium library, for the reason that it was necessary to click each *job-beacon* in order to open up the job description.
I will not go in-depth for the scraping part once more (see Price Research project). However, the code is still available  [here](https://github.com/JosefMoosholzer/JosefMoosholzer.github.io/blob/main/downloads/IndeedScraper.py). For it to work on your computer, you require the latest version of both, the [Microsoft Edge driver]("https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/") and the Microsoft Edge browser. The file needs to be started through the command line, whilst passing an argument in for the number of pages for each job, that should be scraped. For example, 5 pages...
```bash
python IndeedScraper.py 5
```
For this project, I spread the scraping over many days, for two reasons:
- Not being flagged by Indeed as a bot (in case they had an algorithm that was trying to catch some).
- Still achieving a great sample size.
The result were dozens of [csv-files](https://github.com/JosefMoosholzer/JosefMoosholzer.github.io/raw/main/downloads/data.zip) that needed to be merged first. Thankfully the glob.glob library provides a neat solution to this.
```python
import pandas as pd
from glob import glob

files = glob('Data/data*.csv')
dfs = []
for file in files:
    dfs.append(pd.read_csv(file, parse_dates=['Scraped_Date']))

df = pd.concat(dfs)
```

### Transform
Next, I transformed the *Job Title* and *Posting Description* into valuable information. For that, I defined regular expression patterns that extracted a job position and a job level (e.g. Junior, Senior, Manager...) out of the *Job Title*, and demanded skills out of the *Job Description*.