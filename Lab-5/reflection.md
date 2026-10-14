# Reflection - Static Code Analysis

## 1. What issues did the tools identify?

Pylint identified code-quality issues such as missing docstrings, non-standard function names, a mutable default argument, long lines, and a bare exception handler. Flake8 identified formatting violations. Bandit identified potential security issues involving SQL query construction and unsafe pickle deserialization.

## 2. How were the issues fixed?

Parameterized SQL queries were used to prevent unsafe query construction. Pickle serialization was replaced with JSON. The mutable default argument was replaced with `None`, function names were changed to snake_case, docstrings were added, and formatting violations were corrected.

## 3. What did the analysis results show?

The original Pylint score was 4.57/10. After the changes, Pylint reported 10/10. The final Flake8 run produced no violations, and Bandit reported no issues identified. The program also executed successfully after the changes.

## 4. What did you learn?

Static analysis tools help identify code-quality, formatting, and potential security problems before deployment. Using multiple tools provides complementary checks and makes the code easier to maintain and review.
