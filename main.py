import Scripts.process_csv
import Objects.Account
import Tools.tools
import os

def main():
    running = True
    while running:
        Tools.tools.clear_console()
        print("Here are your options:")
        print("\t1. Process new transactions")
        print("\t2. Generate monthly report")
        print("\t3. Generate yearly report")
        print("\t4. Exit program")
        response = Tools.tools.validate_user_input(
            "Enter a number corresponding with your desired choice: ",
            range(1,5),
            fun=lambda x: int(x.strip()))
        if response == 1:
            files_to_process = [file for file in os.listdir("ProcessQueue") if file.endswith(".csv")]
            if len(files_to_process) == 0:
                print("No files to process!")
                print("Put CSV files in the ProcessQueue folder to be processed.")
                input("Press enter to go back to the main menu")
            else:
                process_new_transactions(files_to_process)
        elif response == 2:
            ## TODO
            pass
        elif response == 3:
            ## TODO
            pass
        else:
            print("Exiting program...")
            running = False

def process_new_transactions(files_to_process):
    # ask user if they want to serialize all files
    response = Tools.tools.validate_user_input(
        "Do you want to save all the transactions processed? y/n/m: ",
        ["y", "n", "m"],
        fun=lambda x: x.strip().lower())
    serialize = {"y": True, "m": None, "n": False}[response]

    # process files
    Account = Objects.Account.Account
    tools = Tools.tools
    for filename in files_to_process:
        print("Processing file: {}".format(filename))
        for i, acc in enumerate(Account):
            print("{}. {}".format(i + 1, acc.name))
        response = tools.validate_user_input(
            "Which account is the csv file associated with? Enter a number: ",
            range(1, i + 2),
            fun=lambda x: int(x.strip()))
        for i, acc in enumerate(Account):
            if i + 1 == response:
                transactions = Scripts.process_csv.process_csv(os.path.join("ProcessQueue", filename),
                                                               acc)
        if serialize == True:
            old_transactions = tools.deserialize()
            tools.serialize(old_transactions + transactions)
        elif serialize == None:
            response = tools.validate_user_input(
                "Save transactions from this file? y/n: ", ["y", "n"], fun=lambda x: x.strip().lower())
            if response == "y":
                old_transactions = tools.deserialize()
                tools.serialize(old_transactions + transactions)


if __name__ == "__main__":
    main()
