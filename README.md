# Mobility Optimizers

Plotly Dash based dashboard for showing how public policy can affect greenhouse gas emissions

## Run with Python
Consider creating a virtual environment before installing dependencies.

```sh
pip install -r requirements.txt
python app.py
```

## Build and run with Docker

```sh
docker build -t dash-image .

docker run -p 8050:8050 -v --rm -it -v %cd%:/app --name dash-container dash-image
```

## Access the page

Go to `http://localhost:8050` in browser.



## Development

The page will auto reload each time a change is made and the file is saved if debug mode is set to True 
```sh
app.run_server(host="0.0.0.0", port=8050, debug=True)
```