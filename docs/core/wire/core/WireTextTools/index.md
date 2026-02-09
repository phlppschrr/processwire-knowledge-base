# WireTextTools

Source: `wire/core/WireTextTools.php`

Inherits: `Wire`

ProcessWire Text Tools

Specific text and markup tools for ProcessWire $sanitizer and elsewhere.


@since 3.0.101

Methods:
- [`__construct()`](method-__construct.md)
- [`markupToText(string $str, array $options = array()): string`](method-markuptotext.md)
- [`fixUnclosedTags(string $str, bool $remove = true, array $options = array()): string`](method-fixunclosedtags.md)
- [`collapse(string $str, array $options = array()): string`](method-collapse.md)
- [`truncate(string $str, int|array $maxLength, array|string $options = array()): string`](method-truncate.md)
- [`truncateSentenceTests(string $str, array &$tests, array $endSentenceChars, array $options)`](method-truncatesentencetests.md)
- [`getVisibleLength(string $str): int`](method-getvisiblelength.md)
- [`getPunctuationChars(bool $sentence = false): array`](method-getpunctuationchars.md)
- [`getWordAlternates(string $word, array $options = array()): array`](method-getwordalternates.md)
- [`wordAlternates(string $word, array $options): array`](method-___wordalternates.md) (hookable)
- [`findPlaceholders(string $str, array $options = array()): array|bool`](method-findplaceholders.md)
- [`hasPlaceholders(string $str, array $options = array()): bool`](method-hasplaceholders.md)
- [`populatePlaceholders(string $str, WireData|object|array $vars, array $options = array()): string`](method-populateplaceholders.md)
- [`diffArray(array $oldArray, array $newArray): array`](method-diffarray.md)
- [`diffMarkup(string $old, string $new, array $options = array()): string`](method-diffmarkup.md)
- [`findReplaceEscapeChars(&$str, array $escapeChars, array $options = array()): array`](method-findreplaceescapechars.md)
- [`substr($str, $start, $length = null)`](method-substr.md)
- [`substr(string $str, int $start, int|null $length = null): string`](method-substr.md)
- [`strpos(string $haystack, string $needle, int $offset = 0): bool|false|int`](method-strpos.md)
- [`stripos(string $haystack, string $needle, int $offset = 0): bool|false|int`](method-stripos.md)
- [`strrpos(string $haystack, string $needle, int $offset = 0): bool|false|int`](method-strrpos.md)
- [`strripos(string $haystack, string $needle, int $offset = 0): bool|false|int`](method-strripos.md)
- [`strlen(string $str): int`](method-strlen.md)
- [`strtolower(string $str): string`](method-strtolower.md)
- [`strtoupper(string $str): string`](method-strtoupper.md)
- [`substrCount(string $haystack, string $needle): int`](method-substrcount.md)
- [`strstr(string $haystack, string $needle, bool $beforeNeedle = false): false|string`](method-strstr.md)
- [`stristr(string $haystack, string $needle, bool $beforeNeedle = false): false|string`](method-stristr.md)
- [`strrchr(string $haystack, string $needle): false|string`](method-strrchr.md)
- [`trim(string $str, string $chars = ''): string`](method-trim.md)
- [`ltrim(string $str, string $chars = ''): string`](method-ltrim.md)
- [`rtrim(string $str, string $chars = ''): string`](method-rtrim.md)
