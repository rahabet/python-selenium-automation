# Created by Beth at 2/16/21
Feature: Test scenario for sign in page using the popup functionality

  Scenario: sign in page can be opened from sign in popup
    Given Open Amazon webpage
    When Click on sign in from popup
    Then Verify that sign in page opens
