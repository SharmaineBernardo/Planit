Feature: As a user, I want to add items to cart and verify that the pricing is correct

    Scenario: TC3 - Add items to cart and verify pricing
        Given I am on the home page
        When I navigate to the 'Shop' page
        And I buy '2' pieces of 'Stuffed Frog'
        And I buy '5' pieces of 'Fluffy Bunny'
        And I buy '3' pieces of 'Valentine Bear'
        And I checkout the items
        Then I should see that the following details for each item are displayed:
            | Item           | Price | Subtotal |
            | Stuffed Frog   | 10.99 | 21.98    |
            | Fluffy Bunny   | 9.99  | 49.95    |
            | Valentine Bear | 14.99 | 44.97    |
        And I should see that total cost of '116.9' is displayed
        And I should see that subtotals for these items are correct:
            | Item           | Subtotal |
            | Stuffed Frog   | 21.98    |
            | Fluffy Bunny   | 49.95    |
            | Valentine Bear | 44.97    |
        And I should see that total cost '116.9' equals the sum of subtotals of these items:
            | Stuffed Frog   |
            | Fluffy Bunny   |
            | Valentine Bear |