# $pagesNames->hasNumberSuffix($name, $getNamePrefix = false): int|bool|string

Source: `wire/core/PagesNames.php`

Does the given name or Page have a number suffix? Returns the number if yes, or false if not

## Arguments

- string|Page $name
- bool $getNamePrefix Return the name prefix rather than the number suffix? (default=false)

## Return value

int|bool|string Returns false if no number suffix, or int for number suffix or string for name prefix (if requested)
