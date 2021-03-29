# Libraries
import logging
import urllib.parse
import time

# Packages
import dateutil.parser
import lxml.html
import requests

# Project
from typing import Union

# Setup logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)

HTTP_FAIL_SLEEP = [15, 30, 60, 300]
HTTP_SLEEP_DEFAULT = 0.0
ARELLE_BASE_URL = "http://arelle:8080/rest/xbrl/"
ARELLE_DATA_SETS = ["concepts", "pre", "dim", "facts", "factTable", "roleTypes"]


def get_buffer(filing_xml_url: str, data_set: str, media: str, base_path: str = ARELLE_BASE_URL):
    """
    Retrieve parsed xbrl from Arelle server to memory.
    :param filing_xml_url: url to XBRL instance on EDGAR
    :param base_path: base url for Arelle server
    :return: file_buffer
    """
    # Log entrance
    logger.info("Retrieving parsed XBRL for {0} to memory".format(filing_xml_url))
    
    # setting up final parameters string for request
    final_params = media
    
    # adding full listing of columns requested for facts data as required by Arelle server
    if data_set == "facts":
        final_params = final_params + "&factListCols=Label,unitRef,Dec,Value,EntityScheme,EntityIdentifier,Period,Dimensions"
    
    #Build URL    
    remote_uri = ARELLE_BASE_URL + filing_xml_url + "/{0}?media={1}".format(data_set, final_params)

    # Try to retrieve the file
    complete = False
    failures = 0
    file_buffer = None

    while not complete:
        try:
            with requests.Session() as s:
                r = s.get(remote_uri)
                file_buffer = r.content
                complete = True

                # Sleep if set gt0
                if HTTP_SLEEP_DEFAULT > 0:
                    time.sleep(HTTP_SLEEP_DEFAULT)
        except Exception as e:  # pylint: disable=broad-except
            # Handle and sleep
            if failures < len(HTTP_FAIL_SLEEP):
                logger.warning("File {0}, failure {1}: {2}".format(remote_uri, failures, e))
                time.sleep(HTTP_FAIL_SLEEP[failures])
                failures += 1
            else:
                logger.error("File {0}, failure {1}: {2}".format(remote_uri, failures, e))
                return file_buffer, last_modified_date
    # Log successful exit
    if complete:
        logger.info("Successfully retrieved file {0}; {1} bytes".format(remote_uri, len(file_buffer)))

    return file_buffer


def get_all_datasets(url, media: str = "xml"):
    data_sets = {}
    for s in ARELLE_DATA_SETS:
        data_sets[s] = get_buffer(url, data_set=s, media=media)
    return data_sets