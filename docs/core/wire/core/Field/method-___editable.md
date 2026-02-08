# $field->editable(?Page $page = null, ?User $user = null): bool

Source: `wire/core/Field.php`

Is this field editable?

- To maximize efficiency check that `$field->useRoles` is true before calling this.
- If you have already verified that the page is editable, omit or specify null for $page argument.
- **Please note:** this does not check that the provided $page itself is editable. If you want that
  check, then use `$page->editable($field)` instead.

## Usage

~~~~~
// basic usage
$bool = $field->editable();

// usage with all arguments
$bool = $field->editable(?Page $page = null, ?User $user = null);
~~~~~

## Hookable

- Hookable method name: `editable`
- Implementation: `___editable`
- Hook with: `$field->editable()`

## Arguments

- `$page` (optional) `Page|null` Optionally specify a Page for context
- `$user` (optional) `User|null` Optionally specify a different user (default = current user)

## Return value

- `bool`
