from ledger import Ledger

from demo_data import EXPENSES

from printer import report

ledger = Ledger()

for expense in EXPENSES:

    ledger.add(expense)

report(

    ledger.all()

)
