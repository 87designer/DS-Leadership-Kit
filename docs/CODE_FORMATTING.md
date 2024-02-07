# Python Formatting Policy using Black

## Introduction:

This policy outlines the conventions and guidelines for code formatting using the Black code formatter. Adhering to these standards ensures a consistent and clean codebase.

## 1. Installation:

Ensure that Black is installed in your development environment:

```bash
pip install black
```

## 2. Code Formatting:

- Run Black on all Python files in your project:

```bash
black .
```

- Configure your editor to run Black upon saving files for real-time formatting.

## 3. Policy Guidelines:

- **Line Length:**
  - Limit line length to 88 characters.
  - Exception: Allow up to 100 characters for docstrings.

- **Indentation:**
  - Use 4 spaces for indentation.

- **Imports:**
  - Use separate lines for each import.
  - Sort imports in alphabetical order.

- **String Quotes:**
  - Prefer single quotes for string literals.

- **Whitespace:**
  - Avoid trailing whitespace.

- **Blank Lines:**
  - Use two blank lines before top-level functions and classes.
  - Use one blank line before class methods and inside function bodies.

- **Docstrings:**
  - Use triple double-quotes for docstrings.
  - Include type hints in docstrings.

## 4. Example Configuration File (pyproject.toml):

```toml
[tool.black]
line-length = 88
target-version = ['py36', 'py37', 'py38']
```

## 5. Enforcement:

- Code reviews should include Black formatting checks.
- CI/CD pipelines must run Black as part of the build process.

## Conclusion:

Consistent code formatting enhances readability and maintainability. By following this policy and utilizing Black, we ensure a unified coding style throughout the project.

---

This policy serves as a foundation for maintaining a clean and readable Python codebase using the Black code formatter. Adjustments can be made based on project-specific requirements and preferences.