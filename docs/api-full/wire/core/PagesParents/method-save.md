# $pagesParents->save(Page $page): int

Source: `wire/core/PagesParents.php`

Check if saved page needs any pages_parents updates and perform them when applicable

## Usage

~~~~~
// basic usage
$int = $pagesParents->save($page);

// usage with all arguments
$int = $pagesParents->save(Page $page);
~~~~~

## Arguments

- `$page` `Page`

## Return value

- `int` Number of rows updated
