# $page->setName($value, $language = null): $this

Source: `wire/core/Page.php`

Set the page name, optionally for specific language

~~~~~
// Set page name (default language)
$page->setName('my-page-name');

// This is equivalent to the above
$page->name = 'my-page-name';

// Set page name for Spanish language
$page->setName('la-cerveza', 'es');
~~~~~

## Arguments

- string $value Page name that you want to set
- Language|string|int|null $language Set language for name (can also be language name or string in format "name1234")

## Return value

$this
