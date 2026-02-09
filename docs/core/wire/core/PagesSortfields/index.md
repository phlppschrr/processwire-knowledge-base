# PagesSortfields

Source: `wire/core/PagesSortfields.php`

Inherits: `Wire`

ProcessWire PagesSortfields

Pages Sortfields
Manages the table for the sortfield property for Page children.

Methods:
- [`get(int|Page $page): string`](method-get.md) Get sortfield for given Page from DB
- [`save(Page $page): bool`](method-save.md) Save the sortfield for a given Page
- [`delete(Page $page): bool`](method-delete.md) Delete the sortfield for a given Page
- [`decode(string|int $sortfield, string $default = 'sort'): string`](method-decode.md) Decodes a sortfield from a signed integer or string to a field name
- [`encode(string $sortfield, string $default = 'sort'): string|int`](method-encode.md) Encodes a sortfield from a fieldname to a signed integer (ID) representing a custom field, or native field name
