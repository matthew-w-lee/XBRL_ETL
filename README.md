# XBRL ETL App
[view demo (password: matt)](http://161.35.250.95:8888)
## About
This project provides for downloading XBRL (eXtensible Business Reporting Language) data from a REST API built on Arelle, an open-source project for interpreting XBRL.  It also provides models and methods that can be used to pull all data for a requested type of financial statement. A Jupyter Notebook serves as the user interface.

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
* Enter the repository's directory

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
#### Access
If locally installed, please follow instructions above. If using demo, enter the password: "matt". Then click on the src folder and click on the interface.ipynb file.

#### Arelle REST API and Client
The Arelle REST API is a feature of the Arelle project that has been incorporated into a docker container. The API accepts a call with the web address on the SEC website for a XBRL instance file to be processed and a requested type of XBRL data file. The Arelle server provides several different types of XBRL data files that coincide with the specifications of the XBRL standard. The ones of particular concern for this project are:
* pre.xml (presentation information on the line items and their order in each report/statement found in the filing)
* facts.xml (numeric and date information related to each line item)

#### Jupyter Notebook interface
The Jupyter Notebook interface communicates with the Arelle REST API via methods provided by the arelle_client.py file. The notebook provides a method for downloading files obtained from the API to local disk. Note however is it not available or necessary to explore this project). Sample xml files are included with the repository in the 'arelle_xbrl' directory. The files are organized by folder with the first level of folders being named after the CIK (a company's unique ID with the SEC) of a company and the second level named after the accession number (a filing's unique ID with the SEC) of a filing.

The second cell of the notebook provides classes that model the downloaded XBRL files and the company cik/accession_number directory structure.

The third cell provides the methods that can be used to pull information. Please see comments in that cell for further details on use.

<!-- CONTACT -->
## Contact

Matthew W. Lee - matthew.w.lee44@gmail.com

Project Link: [https://github.com/matthew-w-lee/XBRL_ETL](https://github.com/matthew-w-lee/XBRL_ETL)
