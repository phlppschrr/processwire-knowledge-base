# $pages->___savedPageOrField(Page $page, array $changes = array())

Source: `wire/core/Pages.php`

Hook called after either of Pages::save or Pages::saveField successfully executes

## Usage

~~~~~
// basic usage
$result = $pages->___savedPageOrField($page);

// usage with all arguments
$result = $pages->___savedPageOrField(Page $page, array $changes = array());
~~~~~

## Arguments

- `$page` `Page`
- `$changes` (optional) `array` Names of fields

## See Also

- [Pages::saved()](method-___saved.md)
- [Pages::savedField()](method-___savedfield.md)
