# Created by Beth at 1/25/21
Feature: Test Scenario for Amazon search functionality

  Scenario: User is able to search for a product
    Given Open Amazon website
    When Input Books into search field
    And Click on search icon
    Then Product results for Books are shown


