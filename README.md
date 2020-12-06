## Budget

The purpose of this project is to keep track of my personal spending
by processing and categorizing my transactions over all my accounts.

### How to use

First, place CSV files in the ProcessQueue folder. All files in this
folder will be processed and the data serialized. After processing, these
files will be deleted.

Next, run the program. Do `python3 main.py` when in the top level of the
project's directory.

That's it! The program is very user-friendly, and does not need
any further explanation

### Can I use this for my personal spending?

Sure! Though, you will have to configure your own accounts (Objects/Account.py).
You should also configure your own rules for automatic categorization 
(Objects/Transaction.py); the current rules may only apply to me.