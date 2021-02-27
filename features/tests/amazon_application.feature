# Created by Beth at 2/25/21
Feature: Test for opening Amazon Applications

  Scenario: User can open and close Amazon Applications
    Given Open the webpage for amazon application T&C page
    When Store original windows
    And Click on Amazon Application link
    And Switch to the newly opened window
    Then Amazon app page is opened
    And User can close new window and switch back to original window

