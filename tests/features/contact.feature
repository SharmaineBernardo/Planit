Feature: As a user, I want to submit and validate the contact form

    Scenario: Contact form validation
        Given I am on the home page
        When I navigate to the 'Contact' page
        And I submit the form
        Then I should see an error in the header message
        And I should see that the error message 'Forename is required' is displayed
        And I should see that the error message 'Email is required' is displayed
        And I should see that the error message 'Message is required' is displayed
        When I enter the following information in the fields:
            | Forename  | TestData        |
            | Surname   | User            |
            | Email     | tduser@test.com |
            | Telephone | 0212345         |
            | Message   | Test Message    |
        Then I should no longer see an error in the header message
        And I should no longer see the error message 'Forename is required'
        And I should no longer see the error message 'Email is required'
        And I should no longer see the error message 'Message is required'
    
    Scenario Outline: Submit a feedback
        Given I am on the home page
        When I navigate to the 'Contact' page
        And I enter the following information in the fields:
            | Forename  | TestData        |
            | Surname   | User            |
            | Email     | tduser@test.com |
            | Telephone | 02 12345 5678   |
            | Message   | <Message>       |
         And I submit the form
         Then I should see the success message
         And I should see the the back button

         Examples:
             | Message                |
             | Test Message Run One   |
             | Test Message Run Two   |             
             | Test Message Run Three |
             | Test Message Run Four  | 
             | Test Message Run Five  |