# $fieldtype->___upgrade($fromVersion, $toVersion)

Source: `wire/core/Fieldtype.php`

Called when module version changes

## Usage

~~~~~
// basic usage
$result = $fieldtype->___upgrade($fromVersion, $toVersion);
~~~~~

## Arguments

- $fromVersion
- $toVersion

## Exceptions

- `WireException` if upgrade fails
