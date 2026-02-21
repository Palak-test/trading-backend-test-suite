
# trading-backend-test-suite

Welcome to the **Trading Backend Test Suite** — a professional, extensible, and modular test automation framework for backend trading systems. This project leverages Python, pytest, and BDD (Behavior-Driven Development) to deliver robust business logic, API, and web UI test coverage.

## Project Overview

This repository demonstrates:
- Modular domain modeling (e.g., cucumber basket, trading portfolio)
- BDD feature files and step definitions for business logic, API, and web scenarios
- Realistic, production-grade structure for scalable test automation

For detailed documentation, see [tau-pytest-bdd/README.md](tau-pytest-bdd/README.md).

## Architecture

```mermaid
graph TD
   A[Feature Files (Gherkin)] --> B[Step Definitions (pytest-bdd)]
   B --> C[Domain Models (Python)]
   B --> D[API/Web Drivers]
   C --> E[Business Logic]
   D --> F[External Services]
   B --> G[Shared Fixtures & Hooks]
   G --> B
```

**Key Components:**
- **Feature Files:** Describe scenarios in plain English (Gherkin syntax)
- **Step Definitions:** Map steps to Python code using pytest-bdd
- **Domain Models:** Core business logic (e.g., portfolio, basket)
- **API/Web Drivers:** Integrate with REST APIs and web UIs (Selenium)
- **Fixtures & Hooks:** Shared setup/teardown and utilities

## Quick Start

1. **Clone the repository:**
  ```sh
  git clone https://github.com/Palak-test/trading-backend-test-suite.git
  cd trading-backend-test-suite/tau-pytest-bdd
  ```
2. **Install dependencies:**
  ```sh
  pip install -r requirements.txt
  ```
3. **Run all tests:**
  ```sh
  python -m pytest
  ```

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, new features, or bug fixes.

---

For full details, see [tau-pytest-bdd/README.md](tau-pytest-bdd/README.md).
