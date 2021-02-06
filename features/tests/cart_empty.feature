# Created by Beth at 2/6/21
Feature: Test scenario for checking cart is empty

  Scenario: User can check their amazon cart is empty
    Given Open Amazon webpage
    When Click on cart icon
    Then A message your amazon cart is empty should be displayed