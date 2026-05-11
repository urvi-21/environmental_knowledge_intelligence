from generator import generate_response


def generate_cross_source_insights(context):

    prompt = """
    You are an environmental research synthesis assistant.

    Analyze the provided multi-source environmental context and generate:

    1. Shared Findings Across Sources
    2. Common Environmental Indicators
    3. Scientific Consensus
    4. Cross-Source Research Insights

    Rules:
    - Use ONLY the provided context
    - Focus on evidence appearing across multiple sources
    - Keep outputs concise
    - Use bullet points
    - Do not hallucinate unsupported claims

    FORMAT:

    Shared Findings:
    - ...

    Common Environmental Indicators:
    - ...

    Scientific Consensus:
    - ...

    Cross-Source Insights:
    - ...
    """

    insights = generate_response(
        context,
        prompt
    )

    return insights