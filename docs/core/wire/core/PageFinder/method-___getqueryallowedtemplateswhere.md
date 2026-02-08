# $pageFinder->getQueryAllowedTemplatesWhere(DatabaseQuerySelect $query, $where): string

Source: `wire/core/PageFinder.php`

Method that allows external hooks to add to or modify the access control WHERE conditions

Called only if it's hooked. To utilize it, modify the $where argument in a BEFORE hook
or the $event->return in an AFTER hook.

## Usage

~~~~~
// basic usage
$string = $pageFinder->getQueryAllowedTemplatesWhere($query, $where);

// usage with all arguments
$string = $pageFinder->getQueryAllowedTemplatesWhere(DatabaseQuerySelect $query, $where);
~~~~~

## Hookable

- Hookable method name: `getQueryAllowedTemplatesWhere`
- Implementation: `___getQueryAllowedTemplatesWhere`
- Hook with: `$pageFinder->getQueryAllowedTemplatesWhere()`

## Arguments

- `$query` `DatabaseQuerySelect`
- `$where` `string` SQL string for WHERE statement, not including the actual "WHERE"

## Return value

- `string`
