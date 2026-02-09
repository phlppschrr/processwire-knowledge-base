# $databaseQuerySelectFulltext->matchArrayValue(array $value)

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Match when given $value is an array

Note: PageFinder uses its own array-to-value conversion, so this case applies only to other usages outside PageFinder,
such as FieldtypeMulti::getLoadQueryWhere()

## Usage

~~~~~
// basic usage
$result = $databaseQuerySelectFulltext->matchArrayValue($value);

// usage with all arguments
$result = $databaseQuerySelectFulltext->matchArrayValue(array $value);
~~~~~

## Arguments

- `$value` `array`

## Exceptions

- `WireException`

## Since

3.0.141
