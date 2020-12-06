from enum import Enum

class MonthlyExpense(Enum):
    Spotify = 1

class Category(Enum):
    Rent = 1
    Grocery = 2
    Restaurant = 3
    Entertainment = 4
    Moving = 5
    HomeMaintenance = 6
    Utilities = 7
    Internet = 8
    Spotify = 9
    MonthlyExpenses = MonthlyExpense
    Transportation = 10
    Clothing = 11
    InternalTransfer = 12   # for transfers between accounts
    CashBack = 13
    Banking = 14    # for fees, not transfers