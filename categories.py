def group(expenses):

    result = {}

    for item in expenses:

        result.setdefault(

            item.category,

            0

        )

        result[item.category] += item.amount

    return result
