# flask-market

a simple market app for sell and buy products using Flask Web Framework

## get started

## Prerequisites

Make sure you have the following installed on your system:

* Python 3.10 or above
* pip (Python package installer)
* NodeJS 20 or above (for tailwindcss)

### clone the repository

Clone the repository using the following command:

```bash
git clone https://github.com/sinasezza/flask-market.git
```

Change directory to flask-market:

```bash
cd flask-market
```

### install python packages and dependencies

Install the required packages and dependencies by running:

```bash
pip install uv
uv pip install -r requirements.txt --upgrade
```

### configure dotenv file

The dotenv file is used to hide secrets from the source code and inject them at runtime. You can rename **.env.example** to **.env** and configure it as needed.

```bash
mv .env.example .env
# Edit .env to set your configurations
```

### Configure and Run TailwindCss

change the directory to styler and follow its README.md file directives.

### run the application

To start the application, run:

```bash
python main.py
```
