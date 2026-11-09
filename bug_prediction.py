
def predict_bug_type(issues):

    predictions = []

    for issue in issues:
        issue_type = issue["type"]

        if issue_type == "Security Risk":
            bug_type = "Security Vulnerability"

        elif issue_type == "Syntax Error":
            bug_type = "Syntax Bug"

        elif issue_type == "Code Quality":
            bug_type = "Exception Handling Issue"

        else:
            bug_type = "General Code Issue"

        predictions.append({
            "bug_type": bug_type,
            "severity": issue["severity"],
            "line": issue["line"],
            "description": issue["message"]
        })

    return predictions
