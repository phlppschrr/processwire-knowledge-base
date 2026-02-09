# WireTranslatable

Source: `wire/core/Interfaces.php`

Interface that indicates a class contains gettext() like translation methods

Methods:
- [`_(string $text): string`](method-_.md) Translate the given text string into the current language if available.
- [`_x(string $text, string $context): string`](method-_x.md) Perform a language translation in a specific context
- [`_n(string $textSingular, string $textPlural, int $count): string`](method-_n.md) Perform a language translation with singular and plural versions
