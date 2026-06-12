def generate_recommendations(feature_list):

    recommendations = []

    for feature in feature_list:

        if feature == "OverTime":

            recommendations.append(
                "Reduce employee workload and overtime."
            )

        elif feature == "MonthlyIncome":

            recommendations.append(
                "Review employee compensation package."
            )

        elif feature == "JobSatisfaction":

            recommendations.append(
                "Conduct HR engagement and counseling."
            )

        elif feature == "DistanceFromHome":

            recommendations.append(
                "Consider remote or hybrid work options."
            )

        elif feature == "YearsAtCompany":

            recommendations.append(
                "Provide career growth opportunities."
            )

        elif feature == "WorkLifeBalance":

            recommendations.append(
                "Improve work-life balance initiatives."
            )

    return recommendations


if __name__ == "__main__":

    top_features = [
        "OverTime",
        "MonthlyIncome",
        "JobSatisfaction"
    ]

    recommendations = generate_recommendations(
        top_features
    )

    print("\nRecommendations:\n")

    for r in recommendations:

        print("-", r)