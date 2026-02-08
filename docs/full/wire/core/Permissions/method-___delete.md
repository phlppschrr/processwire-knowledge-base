# Permissions::___delete()

Source: `wire/core/Permissions.php`

Permanently delete a Permission


@param Permission|Page $page Permission to delete

@param bool $recursive If set to true, then this will attempt to delete any pages below the Permission too.

@return bool True on success, false on failure

@throws WireException
