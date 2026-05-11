from generator import generate_response


def extract_environmental_trends(context):

    trend_prompt = """
    You are an environmental trend analysis assistant.

    Analyze the provided environmental context and identify:

    1. Environmental trends
    2. Increasing or decreasing patterns
    3. Long-term environmental observations
    4. Climate-related changes

    Rules:
    - Use ONLY the provided context
    - Keep outputs concise
    - Use bullet points
    - Focus on scientific and environmental trends
    - Do not hallucinate unsupported claims

    FORMAT:

    Detected Environmental Trends:
    - ...
    """

    trends = generate_response(
        context,
        trend_prompt
    )

    return trends