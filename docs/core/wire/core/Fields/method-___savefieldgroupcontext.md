# $fields->saveFieldgroupContext(Field $field, Fieldgroup $fieldgroup, $namespace = ''): bool

Source: `wire/core/Fields.php`

Save the context of the given field for the given fieldgroup

## Usage

~~~~~
// basic usage
$bool = $fields->saveFieldgroupContext($field, $fieldgroup);

// usage with all arguments
$bool = $fields->saveFieldgroupContext(Field $field, Fieldgroup $fieldgroup, $namespace = '');
~~~~~

## Hookable

- Hookable method name: `saveFieldgroupContext`
- Implementation: `___saveFieldgroupContext`
- Hook with: `$fields->saveFieldgroupContext()`

## Arguments

- `$field` `Field` Field to save context for
- `$fieldgroup` `Fieldgroup` Context for when field is in this fieldgroup
- `$namespace` (optional) `string` An optional namespace for additional context

## Return value

- `bool` True on success

## Exceptions

- `WireException`
