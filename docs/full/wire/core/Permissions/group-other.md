# Permissions: other

Source: `wire/core/Permissions.php`

@method PageArray find($selector) Return the permissions(s) matching the the given selector query.

@method Permission|NullPage get($selector) Return permission by given name, numeric ID or a selector string.

@method array saveReady(Page $page) Hook called just before a Permission is saved

@method void saved(Page $page, array $changes = array(), $values = [])

@method void added(Page $page) Hook called just after a Permission is added

@method void deleteReady(Page $page) Hook called before a Permission is deleted

@method void deleted(Page $page) Hook called after a permission is deleted

@method Permission new($options = []) Create new Permission instance in memory (3.0.249+)
