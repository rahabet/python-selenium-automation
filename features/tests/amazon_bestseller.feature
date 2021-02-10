# Created by Beth at 2/10/21
Feature: Test case for verifying amazon bestsellers tabs

  Scenario: Verify Amazon Bestseller links
    Given Open amazon bestseller page
    Then Verify 5 links are there displayed in the header
