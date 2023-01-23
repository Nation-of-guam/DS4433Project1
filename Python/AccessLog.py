import random
import pandas as pd
def access_log_generate():
    types = ["viewed", "commented", "added", "liked", "other"]

    out = []

    for i in range(1, 10000001):
        byWho = random.randint(1, 200000)
        whatPage = random.randint(1,200000)
        accesstype = random.choice(types)
        accesstime = random.randint(1,1000000)

        while byWho == whatPage:
            byWho = random.randint(1,200000)
            whatPage = random.randint(1,200000)

        cell = [str(i), str(byWho), str(whatPage), accesstype, str(accesstime)]
        out.append(",".join(cell))

    df = pd.DataFrame(out, columns = ["AccessId", "ByWho", "WhatPage", "TypeOfAccess", "AccessTime"])
    df.to_csv("AccessLog")

