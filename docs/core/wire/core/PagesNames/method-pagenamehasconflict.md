# $pagesNames->pageNameHasConflict(Page $page): string|bool

Source: `wire/core/PagesNames.php`

Does given page have a name that has a conflict/collision?

In multi-language environment this applies to default language only.

## Arguments

- `$page` `Page` Page to check

## Return value

string|bool Returns string with conflict reason or boolean false if no conflict

## Throws

- WireException If given invalid $options argument

## Since

3.0.127
