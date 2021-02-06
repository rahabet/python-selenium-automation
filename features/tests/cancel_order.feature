# Created by Beth at 2/6/21
Feature: Canceling an amazon order

  Scenario Outline: Cancel order page from amazon website
    Given Open what can i help you with page from amazon website
    When Enter <search_query> into search field
#    And Press Enter key
    Then result for <search_query> should be displayed

    Examples:
    |search_query|
    |Cancel order|






