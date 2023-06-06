Feature: Register Account functionality

  Scenario: Register with mandatory field
    Given the user navigates register page
    When the user enters all mandatory fields
    And the user clicks on continue button
    Then the account should get created

  Scenario: Register with all fields
    Given the user navigates register page
    When the user enters all fields
    And the user clicks on continue button
    Then the account should get created
