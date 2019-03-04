Prisma
======

Simple websites screenshooter using Selenium.

Installation
============

Clone the project and run `pipenv install` and you're all set.

Requirements
============

* selenium
* click
* [geckodriver](https://github.com/mozilla/geckodriver/releases)

Usage
=====

To run the script:

    pipenv shell
    python prisma.py -w 1080 -h 900 -u https://duckduckgo.com -f /file/to/save.png

This are the necessary arguments:

* `--width` or `-w`: width of the screenshot
* `--height` or `-h`: height of the screenshot
* `--url` or `-u`: url to load before taking the screenshot
* `--file` or `-f`: full file path of the image to save

If you omit any argument you will be prompted for it.

License
=======

This software is licensed under the [BSD 3-Clause License](https://github.com/silvanocerza/prisma/blob/master/LICENSE).
