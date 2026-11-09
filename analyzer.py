
import ast


def analyze_code(code):
    issues = []

    # Check syntax errors
    try:
        tree = ast.parse(code)
    except SyntaxError as error:
        issues.append({
            "type": "Syntax Error",
            "severity": "High",
            "line": error.lineno,
            "message": error.msg,
            "suggestion": "Correct the syntax error."
        })
        return issues

    # Detect potentially unsafe functions
    for node in ast.walk(tree):

        if isinstance(node, ast.Call):

            if isinstance(node.func, ast.Name):

                if node.func.id in ["eval", "exec"]:
                    issues.append({
                        "type": "Security Risk",
                        "severity": "High",
                        "line": node.lineno,
                        "message": (
                            f"Use of {node.func.id}() detected."
                        ),
                        "suggestion": (
                            "Avoid eval() and exec() when possible. "
                            "Use safer alternatives."
                        )
                    })

        # Detect bare except blocks
        if isinstance(node, ast.ExceptHandler):
            if node.type is None:
                issues.append({
                    "type": "Code Quality",
                    "severity": "Medium",
                    "line": node.lineno,
                    "message": "Bare except block detected.",
                    "suggestion": (
                        "Catch specific exceptions instead."
                    )
                })

    return issues
