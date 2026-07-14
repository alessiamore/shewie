from summary import total
from categories import group


def report(expenses):

    print()

    print("Expense Tracker")

    print("-" * 35)

    for item in expenses:

        print(

            f"{item.title:<15}"

            f"{item.category:<15}"

            f"${item.amount:.2f}"

        )

    print()

    print("-" * 35)

    print(

        f"Total expenses : "

        f"${total(expenses):.2f}"

    )

    print()

    for category, amount in group(expenses).items():

        print(

            f"{category:<15}"

            f"${amount:.2f}"

        )
