# python-data-download-demo

This demo Python application uses the [Advice Slip JSON API](https://api.adviceslip.com/). When run, it contacts this API, pulls one advice from it and saves it to a file.

## usage
To use this app, go to terminal, create virtual environment
```
python3 -m venv venv
```
install dependencies
```
pip install -r requirements.txt
```
and run the program
```
python3 main.py
```
You can also run the script inside a Docker container using `docker compose up -d`

Result is stored in the output directory.