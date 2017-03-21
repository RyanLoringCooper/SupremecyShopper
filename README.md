# SupremecyShopper
A web bot that will try to purchase an item from www.SupremecyNewYork.com. Items are very commonly sold out on this website. To ensure that a user gets their desired item, the web bot will repeatedly refresh the page and check to see if the item is in stock.

The config file is used to store all the basic information needed to purchase from the website. Be warned, running this program will actually make the purchase automatically if the item is available. The url field is the url of the desired item. 

## Dependancy
The two dependancies are selenium and the geckodriver. geckodriver.exe is provided and will only work for Windows machines. Install selenium with

`pip install -U selenium`

