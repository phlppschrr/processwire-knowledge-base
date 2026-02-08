# $template->getParentPage($checkAccess = false): Page|NullPage|null

Source: `wire/core/Template.php`

Return the parent page that this template assumes new pages are added to

This is based on family settings, when applicable.
It also takes into account user access, if requested (see arg 1).

If there is no defined parent, NULL is returned.
If there are multiple defined parents, a NullPage is returned.

## Arguments

- `$checkAccess` (optional) `bool` Whether or not to check for user access to do this (default=false).

## Return value

Page|NullPage|null
