# Line Chatbot Webhook for Azure OpenAI
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is a webhook for Line chatbot that use Azure OpenAI to generate text.

## Pre-requisites
- [Python](https://www.python.org/downloads/) 3.11 or higher
- [Poetry](https://python-poetry.org/docs/#installation)
- [Line Developer Account](https://developers.line.biz/en/)
- [Azure OpenAI Service](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI)


## Installation
```bash
poetry install
```

## Configuration .env
```bash
cp .env.example .env
```

<!-- Table for configure in .env -->
| Key | Description |
| --- | --- |
| `PORT` | Port for run server |
| `HOST` | Host for run server |
| `DEBUG` | Debug mode |
| `LINE_CHANNEL_ACCESS_TOKEN` | Line channel access token |
| `LINE_CHANNEL_SECRET` | Line channel secret |
| `OPENAI_TYPE` | OpenAI type e.g. "azure" |
| `OPENAI_BASE_URL` | OpenAI base url |
| `OPENAI_VERSION` | OpenAI version e.g. "2023-05-15" |
| `OPENAI_KEY` | OpenAI API key |
| `OPENAI_COMPLETION_ENGINE` | OpenAI deployment name |


## Usage
```bash
poetry run python main.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author
<a href="https://github.com/antronic">
  <img src="https://avatars.githubusercontent.com/u/2222477?v=4" width="36px" style="border-radius: 100%"/>
</a>