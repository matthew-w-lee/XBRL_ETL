# Start from a core stack version
FROM jupyter/scipy-notebook:17aba6048f44
# Install in the default python3 environment
RUN pip install 'lxml'