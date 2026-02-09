# CommentFilter

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentFilter.php`

Inherits: `WireData`


Groups:
Group: [other](group-other.md)

ProcessWire FieldtypeComments > CommentFilter

A base class for filtering comments from an external service.

Primarily for Akismet (and CommentFilterAkismet), but kept as a base abstract class to
serve as an interface for adding more in the future.

Note that portions of code in here arefrom Akismet API examples.

Methods:
- [`httpPost($request, $host, $path, int $port = 80): array|string`](method-httppost.md)
