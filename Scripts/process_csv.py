from Objects.Account import Account
from Objects.Transaction import Transaction
from pprint import pprint
from Tools.tools import *
import csv
import datetime
import os
import sys

def process_csv(csvfile: str, account: Account) -> [Transaction]:
    assert type(account) == Account, "account must be of type Account(Enum)"
    transactions = []
    with open(csvfile, newline='') as f:
        passed_header_boa = False
        first_line_boa = True
        reader = csv.reader(f)
        for line in reader:
            if account in [Account.BoA_Checking, Account.BoA_CreditCard]:
                # date, desc, amt, balance after transaction
                # some header info at top to ignore, also one line to ignore after date
                if len(line) > 0 and line[0] == "Date":
                    passed_header_boa = True
                    continue
                if passed_header_boa:
                    if first_line_boa:
                        first_line_boa = False
                        continue
                    transactions.append(Transaction(account,
                                                    datetime.datetime.strptime(line[0], "%m/%d/%Y"),
                                                    line[1],
                                                    float(line[2].replace("\"", " "))))
            elif account in [Account.MFCU_Checking, Account.MFCU_Savings]:
                # m/d/y date, desc, , amount, balance after transaction
                transactions.append(Transaction(account,
                                                datetime.datetime.strptime(line[0], "%m/%d/%y"),
                                                line[1],
                                                float(line[3])))
            elif account == Account.Venmo:
                # username, transaction ID, datetime, type, status, note, from, to, amt, fee, ...
                if line[0] == '' and line[0] != '':
                    desc = "FROM:{}, TO:{}; {}".format(line[6], line[7], line[5])
                    transactions.append(Transaction(account,
                                                    datetime.datetime.strptime(line[2], "%Y-%m-%dT%H:%M:%S"),
                                                    desc,
                                                    float(line[8].replace("$", " ").replace(" ", ""))))
    return transactions


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    assert len(sys.argv) == 2, "to run file: python3 process_csv.py [name of csv file]"
    for i, acc in enumerate(Account):
        print("{}. {}".format(i+1, acc.name))
    response = validate_user_input("Which account is the csv file associated with? Enter a number: ",
                                   range(1, i+2),
                                   fun=lambda x: int(x.strip()))
    for i, acc in enumerate(Account):
        if i+1 == response:
            transactions = process_csv(sys.argv[1], acc)

    pprint(transactions)
