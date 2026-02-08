# $systemUpdaterChecks->checkMemoryLimit(): bool

Source: `wire/modules/System/SystemUpdater/SystemUpdaterChecks.php`

Check PHP memory_limit setting

## Usage

~~~~~
// basic usage
$bool = $systemUpdaterChecks->checkMemoryLimit();
~~~~~

## Return value

- `bool` Always returns true as memory_limit errors not considered fatal

## Since

3.0.206
