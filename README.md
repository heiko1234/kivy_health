# kivy_health

This is a simple kivy app.

![heal_logo](./assets/Health_logo_Kreis3.png)


The purpose of this app is to give the user a 10 sek break.


# Install

The Repo is created with poetry.

```dash

# create virtual environment
python -m venv .venv

# poetry
python -m pip install --upgrade pip

python -m pip install poetry

# poetry update and install of packages

poetry update --lock -vvv

poetry install

```

## Screens

The App contains about 2 Screen. 

A start screen that will lead after a few seconds to the second screen, that will do the magic.

![startscreen](./assets/startscreen.png)

![secondscreen](./assets/progress_screen.png)

If you push the button, it will take your problems for 10 seconds away, while you are breathing.





