from generator import generate_response


def generate_research_insights(context):

    insight_prompt = """
    You are an environmental research assistant.

    Analyze the provided environmental context and generate:

    1. Key Findings
    2. Environmental Indicators
    3. Scientific Evidence
    4. Research Insights

    Rules:
    - Use ONLY the provided context
    - Keep outputs concise
    - Use bullet points
    - Focus on scientific and environmental relevance
    - Do not hallucinate unsupported claims

    FORMAT:

    Key Findings:
    - ...

    Environmental Indicators:
    - ...

    Scientific Evidence:
    - ...

    Research Insights:
    - ...
    """

    insights = generate_response(
        context,
        insight_prompt
    )

    return insights