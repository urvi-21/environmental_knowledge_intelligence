def calculate_confidence(retrieved_results):

    if not retrieved_results:

        return (
            "Low",
            "No supporting evidence retrieved."
        )

    total_score = 0

    for result in retrieved_results:

        (
            chunk,
            final_score,
            env_score,
            sci_score,
            semantic_score
        ) = result

        total_score += final_score

    average_score = (
        total_score / len(retrieved_results)
    )

    # ----------------------------------------
    # CONFIDENCE LOGIC
    # ----------------------------------------

    if average_score >= 7:

        confidence = "High"

        reason = (
            "Multiple highly relevant and "
            "scientifically informative "
            "chunks support the response."
        )

    elif average_score >= 5:

        confidence = "Medium"

        reason = (
            "Retrieved evidence is moderately "
            "relevant with partial scientific support."
        )

    else:

        confidence = "Low"

        reason = (
            "Limited or weak contextual evidence "
            "was retrieved."
        )

    return confidence, reason