import requests

from bs4 import BeautifulSoup


def extract_webpage_text(url):

    headers = {
        "User-Agent":
        "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers
    )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    # ----------------------------------------
    # REMOVE NOISE
    # ----------------------------------------

    for tag in soup([
        "script",
        "style",
        "noscript",
        "header",
        "footer",
        "nav",
        "aside",
        "form"
    ]):
        tag.decompose()

    # ----------------------------------------
    # PRIORITIZE MAIN CONTENT
    # ----------------------------------------

    main_content = soup.find("main")

    if main_content:

        text = main_content.get_text(
            separator=" "
        )

    else:

        article = soup.find("article")

        if article:

            text = article.get_text(
                separator=" "
            )

        else:

            text = soup.get_text(
                separator=" "
            )

    # ----------------------------------------
    # CLEAN TEXT
    # ----------------------------------------

    text = " ".join(
        text.split()
    )

    return text