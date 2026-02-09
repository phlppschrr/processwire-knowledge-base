# WireAction

Source: `wire/core/WireAction.php`

Inherits: `WireData`
Implements: `Module`

## Summary

WireAction

Common methods:
- [`init()`](method-init.md)
- [`getItemType()`](method-getitemtype.md)
- [`isValidItem()`](method-isvaliditem.md)
- [`action()`](method-___action.md)
- [`execute()`](method-execute.md)

Groups:
Group: [other](group-other.md)

Base class for actions in ProcessWire

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

## Methods
- [`__construct()`](method-__construct.md) Define any default values for configuration
- [`init()`](method-init.md) Module initialization
- [`getItemType(): string`](method-getitemtype.md) Return the string type (class name) of items that this action operates upon
- [`isValidItem(object $item): bool`](method-isvaliditem.md) Is the given item valid for use by this action?
- [`action(Wire $item): bool`](method-___action.md) (hookable) Perform the action on the given item
- [`execute(Wire $item): bool`](method-execute.md) Execute the action for the given item
- [`executeMultiple(array|WireArray $items): int`](method-___executemultiple.md) (hookable) Execute the action for multiple items at once
- [`getConfigInputfields(): InputfieldWrapper`](method-___getconfiginputfields.md) (hookable) Return any Inputfields needed to configure this action
- [`setRunner(Wire $runner)`](method-setrunner.md) Set the object instance that is running this action
- [`getRunner(): Wire|null`](method-getrunner.md) Get the object instance that is running this action
- [`summary(string|null $text = null): string`](method-summary.md) Get or set a text summary of what this action did
