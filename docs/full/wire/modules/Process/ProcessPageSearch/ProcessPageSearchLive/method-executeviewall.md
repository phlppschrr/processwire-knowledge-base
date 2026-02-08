# $processPageSearchLive->executeViewAll(): string

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Render output for landing page to view all items of a particular type

Expects these GET vars to be present:
 - type
 - operator
 - property
 - q

## Usage

~~~~~
// basic usage
$string = $processPageSearchLive->executeViewAll();
~~~~~

## Return value

- `string`

## Exceptions

- `WireException`
