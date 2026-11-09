
from google import genai


def review_code_with_gemini(code, issues, api_key):

    if not api_key:
        return "Gemini API key is missing. Please configure it."

    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
You are an experienced Python code reviewer.

Analyze the following Python code:

{code}

Static analysis findings:
{issues}

Please provide:
1. Explanation of each detected issue.
2. Why each issue is problematic.
3. Recommended solution.
4. Corrected code where appropriate.
5. Best practices to improve code quality.

Use clear, beginner-friendly explanations.
"""

        response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)

        return response.text

    except Exception as error:
        return f"Gemini AI review failed: {error}"
