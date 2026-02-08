# $pagesNames->hasAutogenName(Page $page): string|bool

Source: `wire/core/PagesNames.php`

Does the given page have an auto-generated name (during this request)?

## Usage

~~~~~
// basic usage
$string = $pagesNames->hasAutogenName($page);

// usage with all arguments
$string = $pagesNames->hasAutogenName(Page $page);
~~~~~

## Arguments

- `$page` `Page`

## Return value

- `string|bool` Returns auto-generated name if present, or boolean false if not
