# $systemUpdaterChecks->checkWelcome(): bool

Source: `wire/modules/System/SystemUpdater/SystemUpdaterChecks.php`

Check if this is the first call to checkWelcome and show a welcome message and add an active.php file if so

## Usage

~~~~~
// basic usage
$bool = $systemUpdaterChecks->checkWelcome();
~~~~~

## Return value

- `bool` Returns false if active.php does not yet exist or true if it does
