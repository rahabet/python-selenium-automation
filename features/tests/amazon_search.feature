# Created by Beth at 1/25/21
Feature: Test Scenario for Amazon search functionality

  Scenario: User is able to search for a product
    Given Open Amazon webpage
    When Enter Books into search field
    And Click on search
    Then Results for "Books" are shown


