# WireAction

Source: `wire/core/WireAction.php`

Inherits: `WireData`
Implements: `Module`


Groups:
Group: [other](group-other.md)

WireAction

Base class for actions in ProcessWire

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

Methods:
- [`__construct()`](method-__construct.md)
- [`init()`](method-init.md)
- [`getItemType(): string`](method-getitemtype.md)
- [`isValidItem(object $item): bool`](method-isvaliditem.md)
- [`action(Wire $item): bool`](method-___action.md) (hookable)
- [`execute(Wire $item): bool`](method-execute.md)
- [`executeMultiple(array|WireArray $items): int`](method-___executemultiple.md) (hookable)
- [`getConfigInputfields(): InputfieldWrapper`](method-___getconfiginputfields.md) (hookable)
- [`setRunner(Wire $runner)`](method-setrunner.md)
- [`getRunner(): Wire|null`](method-getrunner.md)
- [`summary(string|null $text = null): string`](method-summary.md)
