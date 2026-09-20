def add_segments(df):
    df = df.copy()

    df["TenureGroup"] = df["Tenure"].apply(
        lambda x: "New" if x <= 2 else ("Mid-term" if x <= 5 else "Long-term")
    )

    df["CreditScoreGroup"] = df["CreditScore"].apply(
        lambda x: "Low" if x < 580 else ("Medium" if x < 700 else "High")
    )

    df["BalanceGroup"] = df["Balance"].apply(
        lambda x: "Zero Balance" if x == 0
        else ("Low Balance" if x <= 50000 else "High Balance")
    )

    df["HighValue"] = (
        (df["Balance"] > 50000) &
        (df["EstimatedSalary"] > 100000)
    )

    return df
