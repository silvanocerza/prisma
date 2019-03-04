import os

import click
from selenium import webdriver


@click.command()
@click.option("-w", "--width", "width", prompt=True, type=int)
@click.option("-h", "--height", "height", prompt=True, type=int)
@click.option("-u", "--url", "url", prompt=True, type=str)
@click.option("-f", "--file", "file", prompt=True, type=str)
def prisma(width, height, url, file):
    driver = webdriver.Firefox()
    driver.set_window_size(width, height)
    driver.get(url)

    scroll_w = driver.execute_script("return window.document.body.scrollWidth;")
    scroll_h = driver.execute_script("return window.innerHeight;")

    width_diff = width - scroll_w
    height_diff = height - scroll_h
    driver.set_window_size(width + width_diff, height + height_diff)

    driver.save_screenshot(file)
    driver.quit()


if __name__ == "__main__":
    os.environ["MOZ_HEADLESS"] = "1"
    prisma()
