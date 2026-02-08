# $pagesEditor->savePageFinish(Page $page, $isNew, array $options): bool

Source: `wire/core/PagesEditor.php`

Save individual Page fields and supporting actions

triggers hooks: saved, added, moved, renamed, templateChanged

## Usage

~~~~~
// basic usage
$bool = $pagesEditor->savePageFinish($page, $isNew, $options);

// usage with all arguments
$bool = $pagesEditor->savePageFinish(Page $page, $isNew, array $options);
~~~~~

## Arguments

- `$page` `Page`
- `$isNew` `bool`
- `$options` `array`

## Return value

- `bool`

## Exceptions

- `\Exception|WireException|\PDOException` If any field-saving failure occurs while in a DB transaction
