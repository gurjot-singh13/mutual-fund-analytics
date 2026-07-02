
import pandas as pd

fund_scorecard = pd.read_csv("../outputs/fund_scorecard.csv")
fund_master = pd.read_csv("../data/raw/01_fund_master.csv")

recommendation_table = fund_scorecard.merge(
    fund_master[["amfi_code","risk_category"]],
    on="amfi_code",
    how="left"
)

def recommend_funds(risk_level):

    recommendations = (
        recommendation_table[
            recommendation_table["risk_category"] == risk_level
        ]
        .sort_values("sharpe_ratio", ascending=False)
        .head(3)
    )

    return recommendations[
        [
            "scheme_name",
            "risk_category",
            "sharpe_ratio",
            "fund_score"
        ]
    ]

if __name__ == "__main__":

    risk = input("Enter Risk Level: ")

    print(recommend_funds(risk))
