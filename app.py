
import streamlit as st

from analyzer import analyze_code
from bug_prediction import predict_bug_type
from ai_review import review_code_with_gemini


# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="Reviewly | AI Code Review",
    page_icon="🔍",
    layout="wide"
)


# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #0b1120;
    color: #f8fafc;
}

.main-title {
    font-size: 48px;
    font-weight: 800;
    color: #60a5fa;
    text-align: center;
}

.subtitle {
    font-size: 18px;
    color: #cbd5e1;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------------
# HEADER
# -----------------------------------

st.markdown(
    '<div class="main-title">Reviewly</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-Powered Smart Code Review and Bug Prediction System'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# -----------------------------------
# WELCOME SECTION
# -----------------------------------

st.subheader("Welcome to Reviewly")

st.write(
    "Analyze your Python code, detect potential bugs, "
    "predict bug categories, and receive intelligent "
    "AI-powered recommendations."
)


# -----------------------------------
# CODE INPUT SECTION
# -----------------------------------

st.subheader("Submit Your Python Code")

input_method = st.radio(
    "Choose input method:",
    ["Write or paste code", "Upload Python file"],
    horizontal=True
)

code = ""

if input_method == "Write or paste code":

    code = st.text_area(
        "Enter your Python code:",
        height=300,
        placeholder="def example():\n    print('Hello Reviewly')"
    )

else:

    uploaded_file = st.file_uploader(
        "Upload a Python file",
        type=["py"]
    )

    if uploaded_file:

        try:
            code = uploaded_file.getvalue().decode("utf-8")
            st.code(code, language="python")

        except UnicodeDecodeError:
            st.error(
                "Unable to read the file. "
                "Please upload a UTF-8 encoded Python file."
            )


# -----------------------------------
# CODE ANALYSIS
# -----------------------------------

if st.button("Analyze Code", type="primary"):

    if not code.strip():

        st.warning("Please enter or upload Python code first.")

    else:

        with st.spinner("Reviewly is analyzing your code..."):

            issues = analyze_code(code)

        st.divider()

        st.header("Code Analysis Results")

        if issues:

            st.warning(f"Found {len(issues)} issue(s).")

            for index, issue in enumerate(issues, start=1):

                st.markdown(f"### Issue {index}")

                st.write("**Type:**", issue["type"])
                st.write("**Severity:**", issue["severity"])
                st.write("**Line:**", issue["line"])
                st.write("**Description:**", issue["message"])

                st.info(
                    "Suggestion: " + issue["suggestion"]
                )

        else:

            st.success(
                "No issues detected by the current static analyzer!"
            )


        # -----------------------------------
        # BUG PREDICTION
        # -----------------------------------

        st.divider()

        st.header("Bug Prediction Results")

        if issues:

            predictions = predict_bug_type(issues)

            for prediction in predictions:

                st.markdown(
                    f"### {prediction['bug_type']}"
                )

                st.write(
                    "**Severity:**",
                    prediction["severity"]
                )

                st.write(
                    "**Line:**",
                    prediction["line"]
                )

                st.write(
                    "**Description:**",
                    prediction["description"]
                )

        else:

            st.success(
                "No bug categories predicted from the detected issues."
            )


        # -----------------------------------
        # GEMINI AI CODE REVIEW
        # -----------------------------------

        st.divider()

        st.header("Gemini AI Code Review")

        try:

            api_key = st.secrets["GEMINI_API_KEY"]

            with st.spinner(
                "Gemini AI is reviewing your code..."
            ):

                ai_result = review_code_with_gemini(
                    code,
                    issues,
                    api_key
                )

            st.markdown(ai_result)

        except KeyError:

            st.error(
                "Gemini API key not found. "
                "Please check .streamlit/secrets.toml"
            )

        except Exception as error:

            st.error(
                f"Gemini AI review error: {error}"
            )


# -----------------------------------
# FOOTER
# -----------------------------------

st.divider()

st.markdown(
    "<center>Reviewly | Smart Code Review System</center>",
    unsafe_allow_html=True
)
