import pytest
from email_agent import validate_input, get_api_data, generate_email
import os
import sys
from dotenv import load_dotenv
from unittest.mock import patch
import responses


load_dotenv()


def test_validate_input():
    allowed_modes = ("stock", "news")

    with patch.object(
        sys, "argv", ["email_agent.py", "pipinasdarius@gmail.com", "Invalid_mode"]
    ):
        with pytest.raises(
            SystemExit,
            match="This mode has not yet been implemented. Current modes: stock and news.",
        ):
            validate_input(allowed_modes)

    with patch.object(
        sys,
        "argv",
        ["email_agent.py", "pipinasdarius@gmail.com", "news", "Extra unneeded value"],
    ):
        with pytest.raises(SystemExit, match="Enter email and type: "):
            validate_input(allowed_modes)


@responses.activate
def test_get_api_data():
    stock_url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey={os.getenv("ALPHAVANTAGE_API")}'
    news_url = f"https://gnews.io/api/v4/top-headlines?category=business&lang=en&max=5&nullable=image&apikey={os.getenv("GNEWS_API")}"

    responses.add(responses.GET, stock_url, json={"data": "BUY IBM"}, status=200)
    responses.add(responses.GET, news_url, json={"data": "TOP NEWS"}, status=200)

    stock = get_api_data(stock_url)
    news = get_api_data(news_url)

    assert type(stock) == str
    assert type(news) == str
    assert stock == '{"data": "BUY IBM"}'
    assert news == '{"data": "TOP NEWS"}'

    with pytest.raises(SystemExit, match="Stock data API is not working"):
        get_api_data("Invalid API")

def test_generate_email():
    api = os.getenv("OPENAI_API")

    chatgpt_email = generate_email(
        api, data="USD=200EUR", instructions="Is this  conversion rate correct?"
    )
    assert type(chatgpt_email) == dict
    assert len(chatgpt_email) > 0

    with pytest.raises(SystemExit, match="OpenAI API key invalid"):
        generate_email(
            api="Invalid Api", data="IBM price: 200USD", instructions="Create email"
        )