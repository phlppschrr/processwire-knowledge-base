# Textformatter

Source: `wire/core/Textformatter.php`

Inherits: `WireData`
Implements: `Module`

## Summary

ProcessWire Textformatter

Common methods:
- [`format()`](method-format.md)
- [`format()`](method-format.md)
- [`formatValue()`](method-formatvalue.md)
- [`init()`](method-init.md)
- [`install()`](method-___install.md)

Provides the base class for Textformatting Modules

A simple module type that provides formatting of text fields.
Please see the base `Module` interface for all potential methods that a Textformatter module can have.


This file is licensed under the MIT license
https://processwire.com/about/license/mit/

## Methods
- [`format(&$str): array`](method-format.md) Return an array of module information
- [`format(string &$str)`](method-format.md) Format the given text string, outside of specific Page or Field context.
- [`formatValue(Page $page, Field $field, string|mixed &$value)`](method-formatvalue.md) Format the given text string with Page and Field provided.
