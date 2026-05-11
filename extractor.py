from generator import generate_response


def extract_environmental_information(context):

    extraction_prompt = """
    Extract the following information from the provided environmental context.

    Return the output in this format:

    1. Key Environmental Concepts
    2. Key Scientific Findings
    3. Environmental Indicators

    Keep the output concise and structured.
    """

    extracted_info = generate_response(
        context,
        extraction_prompt
    )

    return extracted_info