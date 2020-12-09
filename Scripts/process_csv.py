import Objects
import Tools.tools
import csv
import datetime
import os
import sys

def process_csv(csvfile: str, account: Objects.Account.Account) -> [Objects.Transaction.Transaction]:
    assert type(account) == Objects.Account.Account, "account must be of type Account(Enum)"
    transactions = []
    with open(csvfile, newline='') as f:
        Account = Objects.Account.Account
        Transaction = Objects.Transaction.Transaction
        passed_header_boa = False
        first_line_boa = True
        reader = csv.reader(f)
        for line in reader:
            if account == Account.BoA_Checking:
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
            elif account == Account.BoA_CreditCard:
                # date, ref #, paid to, address, amt
                if first_line_boa:
                    first_line_boa = False
                    continue
                else:
                    if line[0].endswith("2020"):
                        line[0] = line[0][:-2]
                    transactions.append(Transaction(account,
                                                datetime.datetime.strptime(line[0], "%m/%d/%y"),
                                                "{}; {}".format(line[2], line[3]),
                                                float(line[4])))
            elif account in [Account.MFCU_Checking, Account.MFCU_Savings]:
                # m/d/y date, desc, , amount, balance after transaction
                transactions.append(Transaction(account,
                                                datetime.datetime.strptime(line[0], "%m/%d/%y"),
                                                line[1],
                                                float(line[3])))
            elif account == Account.Venmo:
                # username, transaction ID, datetime, type, status, note, from, to, amt, fee, ...
                if line[0] == '' and line[1] != '':
                    desc = "FROM:{}, TO:{}; {}".format(line[6], line[7], line[5])
                    transactions.append(Transaction(account,
                                                    datetime.datetime.strptime(line[2], "%Y-%m-%dT%H:%M:%S"),
                                                    desc,
                                                    float(line[8].replace("$", " ").replace("(", " ").replace(")", " ").replace(" ", ""))))
    return transactions


if __name__ == "__main__":
    Tools.tools.tools.clear_console()
    assert len(sys.argv) == 2, "to run file: python3 process_csv.py [name of csv file]"
    for i, acc in enumerate(Objects.Account.Account):
        print("{}. {}".format(i+1, acc.name))
    response = Tools.tools.tools.validate_user_input("Which account is the csv file associated with? Enter a number: ",
                                   range(1, i+2),
                                   fun=lambda x: int(x.strip()))
    for i, acc in enumerate(Objects.Account.Account):
        if i+1 == response:
            transactions = process_csv(sys.argv[1], acc)
