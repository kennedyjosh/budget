from Account import Account
from Transaction import Transaction
from pprint import pprint
from tools import *
from typing import TextIO
import datetime
import os
import sys

def process_csv(csvfile: TextIO, account: Account) -> [Transaction]:
    assert type(account) == Account, "account must be of type Account(Enum)"
    transactions = []
    with open(csvfile, "r") as f:
        for line in f.readlines():
            if account == Account.BoA_Checking:
                ## TODO
                pass
            elif account == Account.BoA_CreditCard:
                ## TODO
                pass
            elif account == Account.MFCU_Checking:
                # m/d/y date, desc, , amount, balance after transaction
                line = line.split(",")
                transactions.append(Transaction(Account.MFCU_Checking,
                                                datetime.datetime.strptime(line[0], "%m/%d/%y"),
                                                line[1],
                                                float(line[3])))
            elif account == Account.MFCU_Savings:
                ## TODO
                pass
            elif account == Account.Venmo:
                ## TODO
                pass
    return transactions


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    assert len(sys.argv) == 2, "to run file: python3 main.py [name of csv file]"
    for i, acc in enumerate(Account):
        print("{}. {}".format(i+1, acc.name))
    response = validate_user_input("Which account is the csv file associated with? Enter a number: ",
                                   range(1, i+2),
                                   fun=lambda x: int(x.strip()))
    for i, acc in enumerate(Account):
        if i+1 == response:
            transactions = process_csv(sys.argv[1], acc)

    pprint(transactions)
