# FieldSelectorInfo

Source: `wire/core/FieldSelectorInfo.php`

Class that provides information about selectors for Fieldtypes

This is primarily a helper for the base Fieldtype class getSelectorInfo method

This originated with the InputfieldSelector module and the need for Fieldtypes to
provide information about what properties can be selected, what operators, are used,
and so on. In the future this class will likely come in handy in providing selector
validation and improved help and error messaging when building/testing selectors.

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## __construct()

Construct

## getSelectorInfo()

Return array with information about what properties and operators can be used with this field

@param Field $field

@return array

## getSelectorInfoTemplate()

Return the default selector info template array

@return array

## getOperators()

Get array of operators

@param string $inputType Specify: number, text, fulltext or select, or omit to return all possible operators at once

@return array of operators or blank array if invalid type specified

## getOperatorLabels()

Get array of operators mapped to text labels

@return array
