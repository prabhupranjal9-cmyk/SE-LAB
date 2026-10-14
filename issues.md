\# Static Code Analysis – Issues and Fixes



\## Baseline Analysis



The original `music\_catalog.py` program was executed successfully. It displayed the playlist message and returned the expected popularity labels, selected song ID, and total play count for the test data.



\### Issues Identified



| No. | Tool | Issue | Severity | Planned Fix |

|---:|---|---|---|---|

| 1 | Bandit | SQL query built using string formatting, creating a possible SQL injection vulnerability | Medium | Use parameterized SQL queries |

| 2 | Bandit | `pickle.loads()` can execute unsafe deserialization of untrusted data | Medium | Replace pickle serialization with JSON |

| 3 | Pylint | Mutable default argument `playlist=\[]` | Medium | Use `None` as the default and create a new list when needed |

| 4 | Pylint / Flake8 | Bare `except:` does not specify the exception type | Medium | Catch an appropriate exception explicitly |

| 5 | Pylint / Flake8 | Long lines exceed the recommended line length | Low | Split statements across multiple lines |

| 6 | Pylint | Function names do not follow snake\_case | Low | Rename functions using snake\_case |

| 7 | Flake8 | Variable name `l` is ambiguous | Low | Replace it with a descriptive name |

| 8 | Pylint / Flake8 | Multiple statements on one line | Low | Put each statement on its own line |

| 9 | Pylint | Missing module and function docstrings | Low | Add concise documentation strings |

| 10 | Bandit | `random.choice()` is flagged because the random generator is unsuitable for cryptographic purposes | Low | Assess intended use; cryptographic randomness is unnecessary for selecting a song in this project |



\## Verification



After applying the fixes, the program will be executed again and Pylint, Bandit, and Flake8 will be rerun. Their final reports will be compared against the baseline reports.



\## Pylint Verification



The final Pylint score was 10.00/10. The code-quality findings were addressed by adding docstrings, using snake\_case function names, removing the mutable default argument, and correcting formatting and exception handling.



