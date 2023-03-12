# Created by thomaschiari at 12/03/2023
Feature: Login
Scenario: Successful Login
Given I am on the login page
When I enter my valid username and password
And I click on the login button
Then I should be redirected to the home page
And I should see a welcome message
