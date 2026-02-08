# $hookEvent->removeHook($hookId): HookEvent|WireData

Source: `wire/core/HookEvent.php`

Remove a hook by ID

To remove the hook that this event is for, call it with the $hookId argument as null or blank.

## Example

~~~~~
// Remove this hook event, preventing it from executing again
$event->removeHook(null);
~~~~~

## Usage

~~~~~
// basic usage
$hookEvent = $hookEvent->removeHook($hookId);
~~~~~

## Arguments

- `$hookId` `string|HookEvent|null`

## Return value

- `HookEvent|WireData` $this
