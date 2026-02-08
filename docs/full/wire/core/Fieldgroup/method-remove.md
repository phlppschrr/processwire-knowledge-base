# $fieldgroup->remove($key): bool

Source: `wire/core/Fieldgroup.php`

Remove a field from this fieldgroup

Note that this must be followed up with a `$fieldgroup->save()` before it does anything destructive.
This method does nothing more than queue the removal.

_Technical Details_
Performs a deletion by finding all templates using this fieldgroup, then finding all pages using the template, then
calling upon the Fieldtype to delete them one at a time. This is a potentially expensive/time consuming method, and
may need further consideration.

## Arguments

- Field|string $key Field object or field name, or id.

## Return value

bool True on success, false on failure.
