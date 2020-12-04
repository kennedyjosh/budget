from Account import Account
from Category import Category
from datetime import datetime
from tools import *

class Transaction:
    ask_if_unsure = None  # ask about category if unsure

    def __init__(self, account: Account, date: datetime, description: str, amount: int, category: Category = None):
        self.account = account          # account (MFCU/BoA/etc.)
        self.date = date                # date of transation
        self.desc = description         # description of transaction
        self.amt = amount               # transaction amount
        if category == None:
            self.category = self.try_determine_category()
        else:
            self.category = category    # category of transaction (optional)

    def __str__(self):
        if self.category:
            return "Transaction ({}) via {} on {}: {}; ${}".format(self.category.name, self.account.name,
                                                               self.get_readable_date(), self.desc, self.amt)
        else:
            return "Transaction (uncategorized) via {} on {}: {}; ${}".format(self.account.name,
                                                               self.get_readable_date(), self.desc, self.amt)

    def __repr__(self):
        return self.__str__()

    def get_readable_date(self):
        return self.date.strftime("%m/%d/%y")

    def try_determine_category(self):
        # tries to determine category from transaction description
        # returns None if category cannot be determined
        desc = self.desc.strip().lower()
        ## RENT
        if "ralph malin" in desc:
            return Category.Rent
        ## GROCERY
        elif "star market" in desc:
            return Category.Grocery
        ## RESTAURANT
        elif "starbucks" in desc:
            return Category.Restaurant
        elif "grubhub" in desc:
            return Category.Restaurant
        elif "uber" in desc and "eats" in desc:
            return Category.Restaurant
        elif "teado" in desc:
            return Category.Restaurant
        elif "domino's" in desc:
            return Category.Restaurant
        ## TRANSPORTATION
        elif "subway" in desc and self.amt == -9.6:
            return Category.Transportation
        ## INTERNAL TRANSFER
        elif "home banking" in desc:
            return Category.InternalTransfer
        elif "bank of america" in desc:
            return Category.InternalTransfer
        ## ENTERTAINMENT
        elif "playstation" in desc:
            return Category.Entertainment
        ## ELSE, ASK OR RETURN NONE
        else:
            if Transaction.ask_if_unsure == None:
                response = validate_user_input("Should I ask you if I am unsure of a transaction's category? y/n:",
                                               ["y", "n"],
                                               fun=lambda x: x.strip().lower())
                if response == "y":
                    Transaction.ask_if_unsure = True
                else:
                    Transaction.ask_if_unsure = False

            if Transaction.ask_if_unsure:
                print("Categories:")
                for i, cat in enumerate(Category):
                    print("\t{}. {}".format(i+1, cat.name))
                response = validate_user_input("Enter the number of the category for this transaction:\n" +
                                                   "\t{}, {}, ${}\nEnter a number here: ".format(
                                                       self.get_readable_date(), self.desc, self.amt),
                                               range(1, i+2),
                                               lambda x: int(x.strip()))
                for i, cat in enumerate(Category):
                    if i+1 == response:
                        return cat
                return None
            else:
                return None
