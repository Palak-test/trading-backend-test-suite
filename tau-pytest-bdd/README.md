
# trading-backend-test-suite

This repository contains a professional example of a behavior-driven test suite for backend trading logic and web automation, using Python, pytest, and pytest-bdd. It demonstrates modular domain modeling, BDD feature files, and step definitions for both business logic and web scenarios.



## Project Purpose

This project is designed to:
- Demonstrate BDD with pytest-bdd for both backend and web automation
- Provide modular, realistic domain models (e.g., cucumber basket, trading portfolio)
- Serve as a template for professional Python test automation projects



## Project Structure

- `cucumbers.py`: Example domain model for a cucumber basket
- `portfolio/portfolio.py`: Trading portfolio domain model (buy/sell stocks, track cash)
- `tests/features/`: BDD feature files for cucumbers, service API, web, and portfolio
- `tests/step_defs/`: Step definitions for each feature, using pytest-bdd, requests, selenium
- `conftest.py`: Shared fixtures and hooks
- `.gitignore`, `LICENSE`, `requirements.txt`, `pytest.ini`: Standard project files



## Getting Started

### Prerequisites
- Python 3.7+
- pip (Python package manager)
- Firefox and geckodriver (for web tests)


### Installation
Clone the repository and install dependencies:

```sh
git clone https://github.com/Palak-test/trading-backend-test-suite.git
cd trading-backend-test-suite/tau-pytest-bdd
pip install -r requirements.txt
```



### Running Tests
From the `tau-pytest-bdd` directory, run:

```sh
python -m pytest
```


## Features

- Cucumber basket domain logic and BDD tests
- Trading portfolio domain logic and BDD tests
- DuckDuckGo API and web search scenarios
- Modular, extensible structure for new features



## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, new features, or bug fixes.



## License

This project is licensed under the Apache 2.0 License.
