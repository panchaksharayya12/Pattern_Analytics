def add_age_group(df):
    df = df.copy()

    def age_group(age):
        if age < 30:
            return "Under 30"
        elif age <= 45:
            return "30-45"
        elif age <= 60:
            return "46-60"
        else:
            return "60+"

    df["AgeGroup"] = df["Age"].apply(age_group)
    return df
