from selenium import webdriver

import json
import traceback
import urllib.request


def parse_page(driver):
    script_clue = "q(\"talkPage.init\","
    try:
        for script in driver.find_elements_by_tag_name("script"):
            content = script.get_attribute("innerHTML")
            if content.startswith(script_clue):
                content = content.lstrip(script_clue).rstrip(")")
                json_content = json.loads(content)
                title = json_content["__INITIAL_DATA__"]["name"]
                download_url = json_content["__INITIAL_DATA__"]["media"][
                    "internal"]["podcast-high-en"]["uri"]
                return title, download_url
    except Exception:
        print(traceback.format_exc())
        print("Unable to parse page. Stopping.")
        exit(-1)


def main(url):
    print("Processing URL %s..." % url)
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    title, download_url = parse_page(driver)
    print("TED talk: {}\nDownload URL: {}".format(title, download_url))
    file_title = title + ".mp4"
    print("Downloading file {}...".format(file_title))
    try:
        urllib.request.urlretrieve(download_url, file_title)
        print("Download completed.")
    except Exception:
        print(traceback.format_exc())
        print("Unable to download video. Stopping.")
        exit(-1)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="A simple tool to download TED talks via CLI.")
    parser.add_argument("-t", "--talk", type=str, required=True,
                        help="Link to TED talk")
    args = parser.parse_args()
    main(args.talk)

