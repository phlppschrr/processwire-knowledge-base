# $pagesNames->checkNameConflicts(Page $page)

Source: `wire/core/PagesNames.php`

Check given page’s name for conflicts and increment as needed while also triggering a warning notice

## Usage

~~~~~
// basic usage
$result = $pagesNames->checkNameConflicts($page);

// usage with all arguments
$result = $pagesNames->checkNameConflicts(Page $page);
~~~~~

## Arguments

- `$page` `Page`

## Since

3.0.127
