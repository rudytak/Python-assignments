import re
import numpy as np
import functools as f

lmap = lambda f, x: list(map(f, x))

database = {
    "customers": [
        {"id": 1, "first_name": "Matúš", "last_name": "Debil", "age": 23},
        {"id": 2, "first_name": "Topení", "last_name": "Kretén", "age": 54},
        {"id": 3, "first_name": "Sedlič", "last_name": "Kokot", "age": 78},
        {"id": 4, "first_name": "Dan", "last_name": "Blázen", "age": 32},
        {"id": 5, "first_name": "Jiří", "last_name": "Kvapil", "age": 17},
    ],
    "orders": [
        {"id": 2, "first_name": "Matúš", "last_name": "Debil", "address": "cde"},
        {"id": 3, "first_name": "Jiří", "last_name": "Kvapil", "address": "efg"},
        {"id": 4, "first_name": "Dan", "last_name": "Blázen", "address": "ghi"},
        {"id": 5, "first_name": "Sedlič", "last_name": "Kokot", "address": "ijk"},
    ],
    "balls": [
        {"id": 3, "first_name": "Jiří", "last_name": "Kvapil", "address": "efg"},
        {"id": 4, "first_name": "Dan", "last_name": "Blázen", "address": "ghi"},
        {"id": 5, "first_name": "Sedlič", "last_name": "Kokot", "address": "ijk"},
    ],
    "empty": [],
}


def parse(query):
    query = query.lower()
    split_query = re.split("select|from|where", query)

    q_args = {
        "from": list(
            filter(
                lambda x: len(database[x]) > 0,
                set(re.sub(r"\s+", "", split_query[2]).strip().split(",")),
            )
        ),
    }

    q_args["select"] = (
        re.sub(r"\s+", "", split_query[1])
        .replace(
            "*",
            f.reduce(
                lambda acc, b: acc
                + f.reduce(
                    lambda accc, d: accc + b + "." + d + ",", database[b][0].keys(), ""
                ),
                filter(lambda key: len(database[key]) > 0, q_args["from"]),
                "",
            )[0:-1],
        )
        .strip()
        .split(",")
    )

    q_args["where"] = split_query[3].strip() if len(split_query) > 3 else None

    print(q_args)

    # if there is just one table used, cast all keys to table.key
    if len(q_args["from"]) == 1:
        for key in database[q_args["from"][0]][0].keys():
            # get all keys without "" and replace them with table.key
            q_args["where"] = re.sub(
                f'{key}(?=[^"]*(?:"[^"]*"[^"]*)*$)',
                f'{q_args["from"][0]}.{key}',
                q_args["where"],
            )

            # clean up possible table.table.key doublecasts
            q_args["where"] = q_args["where"].replace(
                f'{q_args["from"][0]}.{q_args["from"][0]}.', f'{q_args["from"][0]}.'
            )

            for s in range(len(q_args["select"])):
                # get all keys without "" and replace them with table.key
                q_args["select"][s] = re.sub(
                    f'{key}(?=[^"]*(?:"[^"]*"[^"]*)*$)',
                    f'{q_args["from"][0]}.{key}',
                    q_args["select"][s],
                )

                # clean up possible table.table.key doublecasts
                q_args["select"][s] = q_args["select"][s].replace(
                    f'{q_args["from"][0]}.{q_args["from"][0]}.', f'{q_args["from"][0]}.'
                )

    # convert object.key to object["key"] syntac
    for table in q_args["from"]:
        for key in database[table][0].keys():
            q_args["where"] = q_args["where"].replace(
                f"{table}.{key}", f'{table}["{key}"]'
            )

            for s in range(len(q_args["select"])):
                q_args["select"][s] = q_args["select"][s].replace(
                    f"{table}.{key}", f'{table}["{key}"]'
                )

    # print(q_args)

    passing = []

    j = 0
    while j < f.reduce(
        lambda a, b: a * b, lmap(lambda key: len(database[key]), q_args["from"])
    ):
        indexes = lmap(
            lambda l: j % len(database[q_args["from"][l]])
            if l == 0
            else j
            // f.reduce(
                lambda a, b: a * b,
                lmap(lambda i: len(database[q_args["from"][i]]), range(l)),
            )
            % len(database[q_args["from"][l]]),
            range(len(q_args["from"])),
        )
        # i_1 = j % len(database[q_args["from"][0]])
        # i_2 = j // len(database[q_args["from"][0]]) % len(database[q_args["from"][1]])
        # i_3 = j // (len(database[q_args["from"][0]]) * len(database[q_args["from"][1]])) % len(database[q_args["from"][2]])
        # ...

        def _f(a, key):
            a[key] = database[key][indexes[q_args["from"].index(key)]]
            return a

        if eval(q_args["where"], f.reduce(_f, q_args["from"], {})):
            # passing.append(indexes)

            passing.append(
                eval(
                    (
                        "{"
                        + f.reduce(
                            lambda acc, d: acc
                            + "'"
                            + d.replace('["', ".").replace('"]', "")
                            + f"' : {d},",
                            q_args["select"],
                            "",
                        )
                        + "}"
                    ),
                    f.reduce(_f, q_args["from"], {}),
                )
            )
            pass
        j += 1

    return passing


parsed = parse(
    "SELECT customers.id, orders.id FROM CUSTOMERS, orders WHERE customers.id >= 3 or (orders.id < 5 and orders.id > 2)"
)

for p in parsed:
    print(p)
