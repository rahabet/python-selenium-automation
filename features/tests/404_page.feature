# Created by Beth at 2/24/21
Feature: test for 404 page

  Scenario: Amazon 404 page opens blog in another window
    Given Open amazon Dress b0777k16r9v3 page
    When Store original windows
    And Click to open blog
    And Switch to the newly opened window
    Then User can close new window and switch back to original window

