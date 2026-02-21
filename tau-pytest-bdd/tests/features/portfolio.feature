@portfolio
Feature: Trading Portfolio
  As a trader,
  I want to manage my portfolio by buying and selling stocks,
  So that I can track my investments and cash balance.

  Scenario: Buy shares with sufficient cash
    Given a portfolio with $10000 cash
    When I buy 10 shares of "AAPL" at $150 each
    Then my portfolio has 10 shares of "AAPL"
    And my cash balance is $8500

  Scenario: Attempt to buy shares with insufficient cash
    Given a portfolio with $500 cash
    When I buy 10 shares of "GOOG" at $100 each
    Then an error should be raised

  Scenario: Sell shares held in portfolio
    Given a portfolio with $2000 cash
    And I buy 5 shares of "TSLA" at $400 each
    When I sell 2 shares of "TSLA" at $500 each
    Then my portfolio has 3 shares of "TSLA"
    And my cash balance is $1900

  Scenario: Attempt to sell more shares than owned
    Given a portfolio with $1000 cash
    And I buy 2 shares of "MSFT" at $200 each
    When I sell 5 shares of "MSFT" at $250 each
    Then an error should be raised
