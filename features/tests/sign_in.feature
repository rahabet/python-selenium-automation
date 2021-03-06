# Created by Beth at 3/5/21
Feature: Test scenario for opening sign in page from orders link

   Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon webpage
    When Click Amazon Orders link
    Then Verify Sign-In page is opened



