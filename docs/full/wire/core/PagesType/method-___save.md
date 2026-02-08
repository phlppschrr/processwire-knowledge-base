# $pagesType->___save(Page $page): bool

Source: `wire/core/PagesType.php`

Save a page object and its fields to database.

- This is the same as calling $page->save()
- If the page is new, it will be inserted. If existing, it will be updated.
- If you want to just save a particular field in a Page, use `$page->save($fieldName)` instead.

Hook note:
If you want to hook this method, please hook the `saveReady`, `saved`, or one of
the `Pages::save*` methods instead, as hooking this method will not hook relevant pages
saved directly through $pages->save().

## Arguments

- `$page` `Page`

## Return value

bool True on success

## Throws

- WireException
