# WireTranslatable

Source: `wire/core/Interfaces.php`

## Summary

Interface that indicates a class contains gettext() like translation methods

Common methods:
- [`_()`](method-_.md)
- [`_x()`](method-_x.md)
- [`_n()`](method-_n.md)

## Methods
- [`_(string $text): string`](method-_.md) Translate the given text string into the current language if available.
- [`_x(string $text, string $context): string`](method-_x.md) Perform a language translation in a specific context
- [`_n(string $textSingular, string $textPlural, int $count): string`](method-_n.md) Perform a language translation with singular and plural versions
