Feature: Search product feature

  @search
  Scenario: Search for an vlaid product
    Given the user navigates to the Home Page
    When the user enters valid product into the search box field
    And the user clicks on Search button
    Then valid product shoud get displayed in search results

  @search
  Scenario: Search for an invlaid product
    Given the user navigates to the Home Page
    When the user enters invalid product into the search box field
    And the user clicks on Search button
    Then proper message should display in Search Result

  @search
  Scenario: Search for an empty product
    Given the user navigates to the Home Page
    When the user does not enter any product into the search box field
    And the user clicks on Search button
    Then proper message should display in Search Result