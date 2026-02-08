# $pageFinder->___getQueryAllowedTemplatesWhere(DatabaseQuerySelect $query, $where): string

Source: `wire/core/PageFinder.php`

Method that allows external hooks to add to or modify the access control WHERE conditions

Called only if it's hooked. To utilize it, modify the $where argument in a BEFORE hook
or the $event->return in an AFTER hook.

## Arguments

- `$query` `DatabaseQuerySelect`
- `$where` `string` SQL string for WHERE statement, not including the actual "WHERE"

## Return value

string
