# $modules->refresh($showMessages = false)

Source: `wire/core/Modules.php`

Refresh the modules cache

This forces the modules file and information cache to be re-created.

## Usage

~~~~~
// basic usage
$result = $modules->refresh();

// usage with all arguments
$result = $modules->refresh($showMessages = false);
~~~~~

## Hookable

- Hookable method name: `refresh`
- Implementation: `___refresh`
- Hook with: `$modules->refresh()`

## Arguments

- `$showMessages` (optional) `bool` Show notification messages about what was found? (default=false) 3.0.172+
