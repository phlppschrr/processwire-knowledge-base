# $fieldtype->upgrade($fromVersion, $toVersion)

Source: `wire/core/Fieldtype.php`

Called when module version changes

## Usage

~~~~~
// basic usage
$result = $fieldtype->upgrade($fromVersion, $toVersion);
~~~~~

## Hookable

- Hookable method name: `upgrade`
- Implementation: `___upgrade`
- Hook with: `$fieldtype->upgrade()`

## Arguments

- $fromVersion
- $toVersion

## Exceptions

- `WireException` if upgrade fails
