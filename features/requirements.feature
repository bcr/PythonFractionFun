Feature: Given requirements

    These were the requirements given

    Scenario: Operands and operators shall be separated by one or more spaces.
        When we have the input "1   +   2"
        Then the output should be "3"

    Scenario: Mixed numbers will be represented by whole_numerator/denominator. e.g. "3_1/4".
        When we have the input "3_1/4 + 0"
        Then the output should be "3_1/4"

    Scenario: Improper fractions and whole numbers are also allowed as operands.
        When we have the input "9/8 + 2"
        Then the output should be "3_1/8"

    Scenario: Multiplication works.
        When we have the input "1/2 * 2"
        Then the output should be "1"

    Scenario: Addition works.
        When we have the input "1/2 + 1/4"
        Then the output should be "3/4"

    Scenario: Subtraction works.
        When we have the input "1/2 - 1/4"
        Then the output should be "1/4"

    Scenario: Division works.
        When we have the input "1/2 / 1/2"
        Then the output should be "1"
