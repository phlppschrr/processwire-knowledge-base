# $page->setLanguageValues($field, array $values): Page

Source: `wire/core/Page.php`

Set value for field in one or more languages (requires LanguageSupport module). $field should be field/property name (string), $values should be array of values indexed by language name. @since 3.0.236

## Usage

~~~~~
// basic usage
$page = $page->setLanguageValues($field, $values);

// usage with all arguments
$page = $page->setLanguageValues($field, array $values);
~~~~~
