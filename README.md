# TED Downloader

A simple tool to download [TED](https://www.ted.com/) talks via CLI.

---
## Information

**Status**: `Occasionally maintained`

**Type**: `Personal project`

**Development year(s)**: `2018+`

**Authors**: [ShadowTemplate](https://github.com/ShadowTemplate)

**Notes**: *This tool parses the source code of TED pages and may thus suddenly 
break if changes are performed on its front end.*

---
## Getting Started

The script is ready to be used and no configuration is required.
A TED talk can be downloaded by its URL (typically 
_https://www.ted.com/talks/TALK_AUTHOR_AND_TITLE_), e.g.:

```
$ python ted.py -t https://www.ted.com/talks/barry_schwartz_on_the_paradox_of_choice
```

The output should be a nicely formatted video with title "*Barry Schwartz: The 
paradox of choice.mp4*".

Talks are downloaded in the original language, with English subtitles 
hard-coded and in the best available definition. Different languages and 
formats can be used. Feel free to find the appropriate tags from TED pages and 
use them in the script.

### Prerequisites

Clone the repository and install the required Python dependencies:

```
$ git clone https://github.com/ShadowTemplate/ted-downloader.git
$ cd ted-downloader/
$ pip install --user -r requirements.txt
```

---
## Building tools

* [Python 3.6](https://www.python.org/downloads/release/python-360/) - Programming language
* [Selenium](https://www.seleniumhq.org/projects/webdriver/) - 
Web page scraping and JavaScript extraction

---
## Contributing

Any contribution is welcome. Feel free to open issues or submit pull requests.

---
## License

This project is licensed under the GNU GPLv3 license.
Please refer to the [LICENSE.md](LICENSE.md) file for details.

---
*This README.md complies with [this project template](https://github.com/ShadowTemplate/project-template). Feel free to adopt it
and reuse it.*
