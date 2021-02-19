# Created by Beth at 2/19/21
Feature: Test case to verify that every product
  on the Wholefoods page has a text ‘Regular’ and a product name

  Scenario: Verify whole food products
    Given Open wholefoods page from amazon website
    Then Verify 36 wholefoods products has a name and Regular text