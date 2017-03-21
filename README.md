# SupremecyShopper
A web bot that will try to purchase an item from www.supremenewyork.com. Items are very commonly sold out on this website. To ensure that a user gets their desired item, the web bot will repeatedly refresh the page and check to see if the item is in stock.

The config file is used to store all the basic information needed to purchase from the website. Be warned, running this program will actually make the purchase automatically if the item is available. The url field is the url of the desired item. 

## Dependancies
The three dependancies are selenium, firefox, and the geckodriver. geckodriver.exe is provided and will only work for Windows machines. Firefox can be downloaded and installed on https://www.mozilla.org/en-US/firefox/new/. Install selenium with

`pip install -U selenium`

