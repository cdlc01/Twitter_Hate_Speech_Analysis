# Hate Speech Predictor Flask App Template

### Requirements

This repo uses Python 3.8.5, Flask 1.1.2, and scikit-learn 0.23.2. All python packages can be found in the `requirements.txt` file.  The requirements are in `pip` style, because this is supported by Heroku.

To create a new `conda` environment to use this repo, run:
```bash
conda create --name speech-flask pip
conda activate speech-flask
pip install -r requirements.txt
```

### Running the Flask Application

To run in a development environment (on your local computer), run:
```bash
export FLASK_ENV=development
env FLASK_APP=app.py flask run
```

This will produce an output that looks something like:
```
 * Serving Flask app "app.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: <PIN>
```

Like Jupyter Notebook, this server needs to stay running in the terminal for the application to work.  If you want to do something else in the terminal, you need to open a new window/tab, or shut down the server with CTRL+C. **DO NOT** just close the terminal window when you are done running the Flask app — it will keep running in the background and cause problems until you locate the process ID and terminate it — always make sure you use CTRL-C.

Unlike Jupyter Notebook, this doesn't open in the browser automatically.  You need to copy the URL http://127.0.0.1:5000/ and paste it into a web browser.  Once you do that, you should see the homepage of the example app!

## How to Use This Application

The application asks for you to copy and paste an example. Simply copy and paste a tweet and hit "Predict!" 

It will take the application about two minutes to run the tweet through the pipeline but it will return it's prediction at the end
