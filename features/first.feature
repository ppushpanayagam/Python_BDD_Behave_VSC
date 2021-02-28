Feature: Login scenario
    Scenario: Login with valid values
        Given the user launch the application
        When the user login with valid credentials
        Then user should be able to login successfully