# $templates->getParentPage(Template $template, $checkAccess = false, $getAll = false): Page|NullPage|null|PageArray

Source: `wire/core/Templates.php`

Return the parent page that this template assumes new pages are added to

- This is based on family settings, when applicable.
- It also takes into account user access, if requested (see arg 1).
- If there is no defined parent, NULL is returned.
- If there are multiple defined parents, a NullPage is returned (use $getAll to get them).

## Arguments

- `$template` `Template`
- `$checkAccess` (optional) `bool` Whether or not to check for user access to do this (default=false).
- `$getAll` (optional) `bool|int` Specify true to return all possible parents (makes method always return a PageArray) Or specify int of maximum allowed `Page::status*` constant for items in returned PageArray (since 3.0.138).

## Return value

Page|NullPage|null|PageArray
