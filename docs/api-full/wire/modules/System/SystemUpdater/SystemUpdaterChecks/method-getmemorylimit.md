# $systemUpdaterChecks->getMemoryLimit($getInUnit = 'M'): int|float

Source: `wire/modules/System/SystemUpdater/SystemUpdaterChecks.php`

Get memory limit

## Usage

~~~~~
// basic usage
$int = $systemUpdaterChecks->getMemoryLimit();

// usage with all arguments
$int = $systemUpdaterChecks->getMemoryLimit($getInUnit = 'M');
~~~~~

## Arguments

- `$getInUnit` (optional) `string` Get value in 'K' [kilobytes], 'M' [megabytes], 'G' [gigabytes] (default='M')

## Return value

- `int|float`

## Since

3.0.206
