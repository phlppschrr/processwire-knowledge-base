# $pagesEditor->savePageQuery(Page $page, array $options): bool

Source: `wire/core/PagesEditor.php`

Execute query to save to pages table

triggers hooks: addReady, saveReady, statusChangeReady (when status changed)

## Usage

~~~~~
// basic usage
$bool = $pagesEditor->savePageQuery($page, $options);

// usage with all arguments
$bool = $pagesEditor->savePageQuery(Page $page, array $options);
~~~~~

## Arguments

- `$page` `Page`
- `$options` `array`

## Return value

- `bool`

## Exceptions

- `WireException|\Exception`
