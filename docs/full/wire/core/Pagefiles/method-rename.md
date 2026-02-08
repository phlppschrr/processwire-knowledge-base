# $pagefiles->rename(Pagefile $item, $name): Pagefiles

Source: `wire/core/Pagefiles.php`

Queue a rename of a Pagefile

This only queues a rename. Rename actually occurs when page is saved.
Note this differs from the behavior of `Pagefile::rename()`.

## Arguments

- `$item` `Pagefile`
- `$name` `string`

## Return value

Pagefiles

## See also

- [Pagefile::rename()](../Pagefile/method-rename.md)
