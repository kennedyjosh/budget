from Scripts.process_csv import process_csv
from Objects.Account import Account
from Tools.tools import validate_user_input
import sys
import os

def main():
    for filename in os.listdir("ProcessQueue"):
        if filename.endswith(".csv"):
            print("Processing file: {}".format(filename))
            for i, acc in enumerate(Account):
                print("{}. {}".format(i + 1, acc.name))
            response = validate_user_input("Which account is the csv file associated with? Enter a number: ",
                                           range(1, i + 2),
                                           fun=lambda x: int(x.strip()))
            for i, acc in enumerate(Account):
                if i + 1 == response:
                    transactions = process_csv(os.path.join("ProcessQueue", filename), acc)
            print(len(transactions))


if __name__ == "__main__":
    main()