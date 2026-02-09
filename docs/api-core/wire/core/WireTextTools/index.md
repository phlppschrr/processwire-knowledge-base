# WireTextTools

Source: `wire/core/WireTextTools.php`

Inherits: `Wire`

## Summary

ProcessWire Text Tools

Common methods:
- [`markupToText()`](method-markuptotext.md)
- [`fixUnclosedTags()`](method-fixunclosedtags.md)
- [`collapse()`](method-collapse.md)
- [`truncate()`](method-truncate.md)
- [`truncateSentenceTests()`](method-truncatesentencetests.md)

Specific text and markup tools for ProcessWire `$sanitizer` and elsewhere.


@since 3.0.101

## Methods
- [`__construct()`](method-__construct.md) Construct
- [`markupToText(string $str, array $options = array()): string`](method-markuptotext.md) Convert HTML markup to readable text
- [`fixUnclosedTags(string $str, bool $remove = true, array $options = array()): string`](method-fixunclosedtags.md) Remove (or close) unclosed HTML tags from given string
- [`collapse(string $str, array $options = array()): string`](method-collapse.md) Collapse string to plain text that all exists on a single long line without destroying words/punctuation.
- [`truncate(string $str, int|array $maxLength, array|string $options = array()): string`](method-truncate.md) Truncate string to given maximum length without breaking words
- [`truncateSentenceTests(string $str, array &$tests, array $endSentenceChars, array $options)`](method-truncatesentencetests.md) Helper to truncate() method, generate tests/positions for where sentences end
- [`getVisibleLength(string $str): int`](method-getvisiblelength.md) Return visible length of string, which is length not counting markup or entities
- [`getPunctuationChars(bool $sentence = false): array`](method-getpunctuationchars.md) Get array of punctuation characters
- [`getWordAlternates(string $word, array $options = array()): array`](method-getwordalternates.md) Get alternate words for given word
- [`wordAlternates(string $word, array $options): array`](method-___wordalternates.md) (hookable) Hookable method to return alternate words for given word
- [`findPlaceholders(string $str, array $options = array()): array|bool`](method-findplaceholders.md) Find and return all {placeholder} tags found in given string
- [`hasPlaceholders(string $str, array $options = array()): bool`](method-hasplaceholders.md) Does the string have any {placeholder} tags in it?
- [`populatePlaceholders(string $str, WireData|object|array $vars, array $options = array()): string`](method-populateplaceholders.md) Given a string (`$str`) and values (`$vars`), populate placeholder “{tags}” in the string with the values
- [`diffArray(array $oldArray, array $newArray): array`](method-diffarray.md) Given two arrays, return array of the changes with 'ins' and 'del' keys
- [`diffMarkup(string $old, string $new, array $options = array()): string`](method-diffmarkup.md) Given two strings (`$old` and `$new`) return a diff string in HTML markup
- [`findReplaceEscapeChars(&$str, array $escapeChars, array $options = array()): array`](method-findreplaceescapechars.md) Find escaped characters in `$str`, replace them with a placeholder, and return the placeholders
- [`substr($str, $start, $length = null)`](method-substr.md) ******************************************************************************************************** MULTIBYTE PHP STRING FUNCTIONS THAT FALLBACK WHEN MBSTRING NOT AVAILABLE
- [`substr(string $str, int $start, int|null $length = null): string`](method-substr.md) Get part of a string
- [`strpos(string $haystack, string $needle, int $offset = 0): bool|false|int`](method-strpos.md) Find position of first occurrence of string in a string
- [`stripos(string $haystack, string $needle, int $offset = 0): bool|false|int`](method-stripos.md) Find the position of the first occurrence of a case-insensitive substring in a string
- [`strrpos(string $haystack, string $needle, int $offset = 0): bool|false|int`](method-strrpos.md) Find the position of the last occurrence of a substring in a string
- [`strripos(string $haystack, string $needle, int $offset = 0): bool|false|int`](method-strripos.md) Find the position of the last occurrence of a case-insensitive substring in a string
- [`strlen(string $str): int`](method-strlen.md) Get string length
- [`strtolower(string $str): string`](method-strtolower.md) Make a string lowercase
- [`strtoupper(string $str): string`](method-strtoupper.md) Make a string uppercase
- [`substrCount(string $haystack, string $needle): int`](method-substrcount.md) Count the number of substring occurrences
- [`strstr(string $haystack, string $needle, bool $beforeNeedle = false): false|string`](method-strstr.md) Find the first occurrence of a string
- [`stristr(string $haystack, string $needle, bool $beforeNeedle = false): false|string`](method-stristr.md) Find the first occurrence of a string (case insensitive)
- [`strrchr(string $haystack, string $needle): false|string`](method-strrchr.md) Find the last occurrence of a character in a string
- [`trim(string $str, string $chars = ''): string`](method-trim.md) Strip whitespace (or other characters) from the beginning and end of a string
- [`ltrim(string $str, string $chars = ''): string`](method-ltrim.md) Strip whitespace (or other characters) from the beginning of string only (aka left trim)
- [`rtrim(string $str, string $chars = ''): string`](method-rtrim.md) Strip whitespace (or other characters) from the end of string only (aka right trim)
