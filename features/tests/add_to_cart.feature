# Created by Beth at 2/9/21
Feature: Test adding product to the cart

  Scenario: User can add a product to the cart
    Given Open Amazon webpage
    When Search for a shoes
    And Click on the first product
    And Click on add to cart button
    Then Verify cart has 1 item