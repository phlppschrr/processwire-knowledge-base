# $page->setName($value, $language = null): $this

Source: `wire/core/Page.php`

Set the page name, optionally for specific language

## Example

~~~~~
// Set page name (default language)
$page->setName('my-page-name');

// This is equivalent to the above
$page->name = 'my-page-name';

// Set page name for Spanish language
$page->setName('la-cerveza', 'es');
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->setName($value);

// usage with all arguments
$result = $page->setName($value, $language = null);
~~~~~

## Arguments

- `$value` `string` Page name that you want to set
- `$language` (optional) `Language|string|int|null` Set language for name (can also be language name or string in format "name1234")

## Return value

- `$this`
