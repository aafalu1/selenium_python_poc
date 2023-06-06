Feature: login feature functionality testing

  @login
  Scenario: the user can login with valid credentials
    Given the user navigates to the login page
    When the user enters valid email address and valid password
    And the user clicks on login button
    Then the user lands in home page

  @login
  Scenario: Login with invalid email and valid password
    Given the user navigates to the login page
    When the user enters invalid email valid password
    And the user clicks on login button
    Then the user should get error meesage

  @login
  Scenario: Login with valid email and invalid password
    Given the user navigates to the login page
    When the user enters valid email invalid password
    And the user clicks on login button
    Then the user should get error meesage





