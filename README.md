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




# To make an android app

Install `javac` see [here](https://stackoverflow.com/questions/66853462/how-to-install-javac-on-linux-mint).

```dash

# for Ubuntu
sudo apt-get install openjdk-8-jdk

# check version
javac -version   
# javac 1.8.0_352

```

Install buildozer in the virtual environment with poetry

```dash

poetry add buildozer

poetry add cython

```

Install [sdkmanager](https://developer.android.com/studio/command-line/sdkmanager)


Download the latest "command line tools only" package from the Android Studio downloads page and unzip the package.
Move the unzipped cmdline-tools directory into a new directory of your choice, such as android_sdk. This new directory is your Android SDK directory.





