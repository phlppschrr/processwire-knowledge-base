# $page->getLanguageValue($language, $field): mixed

Source: `wire/core/Page.php`

Get value for field in language (requires LanguageSupport module). $language may be ID, language name or Language object. Field should be field name (string).

## Usage

~~~~~
// basic usage
$result = $page->getLanguageValue($language, $field);
~~~~~
