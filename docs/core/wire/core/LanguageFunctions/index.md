# LanguageFunctions

Source: `wire/core/LanguageFunctions.php`

ProcessWire Language Functions

Provides GetText-like language translation functions to ProcessWire.

Methods:
- [`__(string|array|bool $text, string|array $textdomain = null, string|bool|array $context = ''): string|array`](method-__.md) Perform a language translation
- [`_x(string $text, string $context, string $textdomain = null): string`](method-_x.md) Perform a language translation in a specific context
- [`_n(string $textSingular, string $textPlural, int $count, string $textdomain = null): string`](method-_n.md) Perform a language translation with singular and plural versions
- [`wireLangEntityEncode(bool|int|string|null $value = ''): bool|int|string|null`](method-wirelangentityencode.md) Set entity encoding state for language translation function calls
- [`wireLangTranslations(array $values = array()): array`](method-wirelangtranslations.md) Set predefined fallback translation values
- [`wireLangReplacements(array $values): array|string`](method-wirelangreplacements.md) Set global translation replacement values
