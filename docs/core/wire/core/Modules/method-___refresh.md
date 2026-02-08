# $modules->___refresh($showMessages = false)

Source: `wire/core/Modules.php`

Refresh the modules cache

This forces the modules file and information cache to be re-created.

## Usage

~~~~~
// basic usage
$result = $modules->___refresh();

// usage with all arguments
$result = $modules->___refresh($showMessages = false);
~~~~~

## Arguments

- `$showMessages` (optional) `bool` Show notification messages about what was found? (default=false) 3.0.172+
