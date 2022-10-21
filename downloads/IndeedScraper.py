from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from time import sleep
from random import randint
import pandas as pd
import sys
import re as regex
from datetime import datetime

def initialize_driver():
    driver = webdriver.Edge()
    driver.implicitly_wait(5)
    return driver

def open_indeed_and_deny_cookies(driver):
    driver.get('https://de.indeed.com/')
    driver.find_element(By.XPATH, '//*[@id="onetrust-reject-all-handler"]').click()
    sleep(1)

def get_url(job_title, page):
    job_title = job_title.replace(' ', '+').strip()
    return f'https://de.indeed.com/jobs?q={job_title}&l=M%C3%BCnchen&start={page}0'


def parse_page(driver, job_title, page):
    try:
        driver.find_element(By.XPATH, '//*[@id="google-Only-Modal"]/div/div[1]/button').click()
        driver.find_element(By.XPATH, '//*[@id="mosaic-modal-mosaic-provider-desktopserp-jobalert-popup"]/div/div/div[1]/div/button').click()
    except: pass

    driver.get(get_url(job_title, page))

    beacons = driver.find_elements(By.CLASS_NAME, 'job_seen_beacon')
    postings = parse_beacons(driver, beacons)

    return parse_all_postings(postings)


def parse_beacons(driver, beacons):
    postings = []

    for beacon in beacons:
        try: beacon.click()
        except: continue
        try: driver.find_element(By.XPATH, '//*[@id="jobsearch-ViewjobPaneWrapper"]/div/button')
        except: pass
        sleep(randint(1,7))

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        header = soup.find('div', {'class':'jobsearch-JobComponent-embeddedHeader'})
        body = soup.find('div', {'class':'jobsearch-JobComponent-embeddedBody'})
        if (header is not None) & (body is not None):
            postings.append((header, body))
        else: print('Posting did not load (fast enough).')

    return postings


def parse_all_postings(postings):
    records = []
    for (header, body) in postings:
        posting = parse_posting(header, body)
        if posting:
            records.append(posting)
    return records


def parse_posting(header, body):
    record = {}
    try:
        record['Job_Title'] = regex.sub('\(\w(/\w)+\)','', header.find('h1').text.replace('- job post', '').title()).strip()
        record['Company'] = header.find_all('div', {'class': 'jobsearch-InlineCompanyRating-companyHeader'})[1].text
    except AttributeError:
        print('Header not found')
        return

    try: record['Rating'] = float(header.find('a', {'class': 'icl-Ratings-starsCountWrapper icl-Ratings-link'})['aria-label'].split(' von')[0])
    except TypeError: pass

    try: record['Compensation'] = regex.sub('[^0-9–]', '', header.find('span', {'class': 'icl-u-xs-mr--xs attribute_snippet'}).text).replace('–', ' to ')
    except AttributeError: pass

    try:
        e_types = body.find('div', {'class': 'jobsearch-JobDescriptionSection-sectionItemKey icl-u-textBold'}).find_next_siblings('div')
        record['Employment_Type'] = [e_type.text for e_type in e_types]
    except AttributeError: pass

    record['Description'] = body.find('div', {'id': 'jobDescriptionText'}).text

    try: record['Insights'] = regex.search('vor \d+\+? Tag(en)? geschaltet', body.find('div', {'id': 'hiringInsightsSectionRoot'}).text).group(0)
    except AttributeError: pass

    try: record['Link'] = header.find('div', {'id':'applyButtonLinkContainer'}).find('a')['href']
    except AttributeError: record['Link'] = 'Fast application'

    return record


def main(queries):
    driver = initialize_driver()
    open_indeed_and_deny_cookies(driver)

    tot_pages = 0
    tot_page_counter = 0
    for query in queries:
        tot_pages += query[1]

    results = []

    for (job_title, pages) in queries:
        page_counter = 0
        for page in range(pages):
            try: results.extend(parse_page(driver, job_title, page))
            except Exception as e: print(type(e))
            page_counter += 1
            tot_page_counter += 1
            print(f'({tot_page_counter}/{tot_pages}):\n\
                \tFinished scraping page {page_counter} out of {pages} page(s) for keyword {job_title}.\n\
                \t{len(results)} results so far.')

    return results


if __name__ == '__main__':
    scrape_result = main([('Data Analyst', int(sys.argv[1])), ('Data Scientist', int(sys.argv[1])),
                          ('Business Analyst', int(sys.argv[1])), ('Business Intelligence', int(sys.argv[1]))])

    df = pd.DataFrame(scrape_result)
    today = datetime.today().date()
    df['Scraped_Date'] = today
    df.to_csv(f'data{today}.csv', index=False)

