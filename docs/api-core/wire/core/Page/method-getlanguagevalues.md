# $page->getLanguageValues($field, array $langs = []): array

Source: `wire/core/Page.php`

Get values for field or one or more languages (requires LanguageSupport module). $field should be field/property name (string), $langs should be array of language names, or omit for all languages. Returns array of values indexed by language name. @since 3.0.236

## Usage

~~~~~
// basic usage
$array = $page->getLanguageValues($field);

// usage with all arguments
$array = $page->getLanguageValues($field, array $langs = []);
~~~~~
