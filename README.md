# API email generating and sending agent

## The email agent takes in an input of a mode, returns data from that modes api (for example news -> returns the top 5 news headlines) and then sends it to chatgpt to write the email and send it out using the smpt library and gmail.com

TLDR: pick mode -> mode API -> openai API -> SMTP

The project has two integrated modes: news, stock. It uses sys.argv, so your input's format should be:
* python email_agent.py <receiver_email> news
* or
* python email_agent.py <receiver_email> stock

To set up this project you will need three api's:
* Gnews api (free): https://gnews.io/
* Alphavantage api (free): https://www.alphavantage.co/
* openai api (paid): https://platform.openai.com/settings/profile/user

> [!IMPORTANT]
> Make sure to pip install -r requirements.txt

You will also have to set up your gmail account by enabling 2-step verification and creating a 3rd party app password:
1) Enable 2-Step Verification (if not already enabled) 
    - Go to: https://myaccount.google.com/security
    - Under "Signing in to Google", enable 2-Step Verification
2) Generate an App Password:
    - After 2-Step Verification is enabled:
    - Go to: https://myaccount.google.com/apppasswords

After this fill in the .env file with the your own codes