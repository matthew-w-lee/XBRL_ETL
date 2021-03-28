# SEC Filing Database and Parser
[view demo](https://www.google.com)
## About
The primary aim of this project is to parse filings submitted with the U.S. Securities and Exchange Commission ("SEC") into a format more useful for analysis by computer. Companies over the years have filed their disclosures in one of several electronic formats -- plain text files (prior to early 2000s), HTML (early 2000s - present), and XBRL (eXtensible Business Reporting Language) (since the early 2010s).

Although the filings submitted in XBRL offer a clear path towards obtaining such data, the filings made in plain text or HTML are more idiosyncratic and resistant to simple parsing. The organization and format of the information embedded in these filings can vary widely between different companies and different time periods.

This project is built on top of OpenEDGAR by LexPredict, a Django framework for building databases from EDGAR that can automate the retrieval and parsing of EDGAR forms. OpenEDGAR is used to download the file representing a submission and to store metadata regarding that submission in a PostgresSQL database. From there, upon request, this project processes the content of a filing into a List of Dicts, with each Dict representing a "row" of text in the filing along with some other metadata regarding that row. This process helps to standardize a filing contents with others and to facilitate a search that mimics the "reading" of the filings content on a row-by-row (or paragraph-by-paragraph) basis.

The project uses a Jupyter Notebook as a user interface, communicating with the Django app via a minimal REST HTTP API. 

## Built With
* [OpenEDGAR by LexPredict](https://github.com/LexPredict/openedgar)
* [Jupyter Notebook](https://github.com/jupyter/notebook)
## Getting Started
#### Prerequisites
* Docker
* Docker Compose
#### Installation
* Clone the repository

```bash
    git clone https://github.com/matthew-w-lee/sec_database_parser.git
```
* Enter repository directory

```bash
    cd sec_filing_app
```
* Enter docker-compose up command. It may take a few minutes to download the images.
When the containers boot up, take note of the token provided in logging info from the Jupyter Notebook container.
You'll need it to access the interface.

```bash
    docker-compose up
```
* Run the migrate script (location below) using the docker exec command to do an inital migration of the database.
The container for Django app should be named sec_database_parser_openedgar_1 as set forth below.

```bash
    docker exec -it sec_database_parser_openedgar_1 /bin/bash /opt/openedgar/lexpredict_openedgar/openedgar/migrate.sh
```
* To seed the database with example companies and filings, enter Django's shell by running the shell.sh script with the docker exec command below.

```bash
    docker exec -it sec_database_parser_openedgar_1 /bin/bash /opt/openedgar/lexpredict_openedgar/openedgar/shell.sh
```

* In the shell, run the following command to seed the database. This will download all of the 10-K form filings
for 10 companies.

```python
    exec(open('/opt/openedgar/lexpredict_openedgar/openedgar/seed_db.py').read())
```

* Open the Jupyter Notebook web app in your browser which should be available at localhost on port 8888.
* Enter the token mentioned above seen during container startup. 
* Click on the interface_notebooks folder.
* Click on the notebook_interface.ipynb file to open the interface.

## Usage
* See notebook_interface.ipynb per the instructions above.

<!-- CONTACT -->
## Contact

Matthew W. Lee - - matthew.w.lee44@gmail.com

Project Link: [https://github.com/matthew-w-lee/sec_database_parser](https://github.com/matthew-w-lee/sec_database_parser)
