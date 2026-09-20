def churn_rate(df):
    return df["Exited"].mean() * 100


def churn_by_group(df, group_column):
    result = df.groupby(group_column)["Exited"].agg(
        Customers="count",
        Churned="sum",
        Churn_Rate="mean"
    )

    result["Churn_Rate"] = (
        result["Churn_Rate"] * 100
    ).round(2)

    return result


def geographic_risk_index(df):
    overall = df["Exited"].mean()

    result = df.groupby("Geography")["Exited"].agg(
        Customers="count",
        Churned="sum",
        Churn_Rate="mean"
    )

    result["Risk_Index"] = (
        result["Churn_Rate"] / overall
    ).round(2)

    result["Churn_Rate"] = (
        result["Churn_Rate"] * 100
    ).round(2)

    return result


def high_value_analysis(df):
    high_value = df[df["HighValue"]]

    return {
        "customers": int(len(high_value)),

        "churned": int(
            high_value["Exited"].sum()
        ),

        "churn_rate": round(
            float(
                high_value["Exited"].mean() * 100
            ),
            2
        ),

        "balance_exposure": round(
            float(
                high_value.loc[
                    high_value["Exited"] == 1,
                    "Balance"
                ].sum()
            ),
            2
        )
    }


def churn_contribution(df, group_column):
    result = df.groupby(group_column)["Exited"].agg(
        Customers="count",
        Churned="sum"
    )

    total_churned = df["Exited"].sum()

    result["Churn_Contribution"] = (
        result["Churned"] /
        total_churned *
        100
    ).round(2)

    return result


def segment_summary(df):
    return {
        "age": churn_by_group(
            df,
            "AgeGroup"
        ),

        "tenure": churn_by_group(
            df,
            "TenureGroup"
        ),

        "credit_score": churn_by_group(
            df,
            "CreditScoreGroup"
        ),

        "balance": churn_by_group(
            df,
            "BalanceGroup"
        ),

        "gender": churn_by_group(
            df,
            "Gender"
        ),

        "activity": churn_by_group(
            df,
            "IsActiveMember"
        ),

        "products": churn_by_group(
            df,
            "NumOfProducts"
        )
    }