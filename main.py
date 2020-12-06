from Scripts.process_csv import process_csv
from Objects.Account import Account
import sys

def main(csvfile):
    process_csv(csvfile, Account.BoA_Checking)

if __name__ == "__main__":
    main(sys.argv[1])