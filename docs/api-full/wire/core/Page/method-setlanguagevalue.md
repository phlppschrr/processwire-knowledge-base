# $page->setLanguageValue($language, $field, $value): Page

Source: `wire/core/Page.php`

Set value for field in language (requires LanguageSupport module). $language may be ID, language name or Language object. Field should be field name (string).

## Usage

~~~~~
// basic usage
$page = $page->setLanguageValue($language, $field, $value);
~~~~~
