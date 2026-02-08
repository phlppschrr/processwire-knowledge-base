# $pagesEditor->insertBefore(Page $page, Page $sibling, $after = false)

Source: `wire/core/PagesEditor.php`

Sort one page before another (for pages using manual sort)

Note that if given $sibling parent is different from `$page` parent, then the `$pages->save()`
method will also be called to perform that movement.

## Arguments

- Page $page Page to move/sort
- Page $sibling Sibling that page will be moved/sorted before
- bool $after Specify true to make $page move after $sibling instead of before (default=false)

## Throws

- WireException When conditions don't allow page insertions
