# XBRL ETL App
[view demo](https://www.google.com)
## About
This project provides for downloading XBRL data from a REST API provided by Arelle, an open-source project for interpreting XBRL, and further processing
to pull all data for a requested type of financial statement. A Jupyter Notebook is used as the interface.

## Built With
* [Arelle](https://github.com/Arelle/Arelle)
* [Jupyter Notebook](https://github.com/jupyter/notebook)
## Getting Started
#### Prerequisites
* Docker
* Docker Compose
#### Installation
* Clone the repository

```bash
    git clone https://github.com/matthew-w-lee/XBRL_ETL.git
```
* Enter repository directory

```bash
    cd XBRL_ETL
```
* Enter docker-compose up command. It may take a few minutes to download the images.
When the containers boot up, take note of the token provided in logging info from the Jupyter Notebook container.
You'll need it to access the interface.

```bash
    docker-compose up
```
* Open the Jupyter Notebook web app in your browser which should be available at localhost on port 8888.
* Enter the token mentioned above seen during container startup. 
* Click on the "src" folder.
* Click on the interface.ipynb file to open the interface.

## Usage
#### Arelle REST API and Client
The Arelle REST API is provided by a docker container. The API accepts a call with the web address on the SEC website of the XBRL instance file to be processed and a requested type of XBRL data file. The Arelle server provides several different types of XBRL data files coinciding with the specifications of the XBRL standard. The ones of particular concern for this project are:
* pre.xml (presentation information on the line items and their order in each report/statement found in the filing)
* facts.xml (numeric and date information related to each line item)

#### Jupyter Notebook interface
The Jupyter Notebook interface communicates with the Arelle REST API via methods provided by the arelle_client.py file. The notebook provides a method for downloading files obtained from the API to local disk but it is not necessary to use it in exploring this project. Sample xml files are included in the repository in the directory arelle_xbrl. The files are organized in folder, the first level being by CIK (a company's unique ID with the SEC) and then the second level being by accession number (a filing's unique ID with the SEC).

The second cell of the notebook provides classes that model the downloaded XBRL files and the company/accession_number directory structure.

The third cell provides the methods that can be used to pull information. Please see comments in that cell for further implementation details.

<!-- CONTACT -->
## Contact

Matthew W. Lee - matthew.w.lee44@gmail.com

Project Link: [https://github.com/matthew-w-lee/XBRL_ETL](https://github.com/matthew-w-lee/XBRL_ETL)
