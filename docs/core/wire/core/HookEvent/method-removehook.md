# $hookEvent->removeHook($hookId): HookEvent|WireData

Source: `wire/core/HookEvent.php`

Remove a hook by ID

To remove the hook that this event is for, call it with the $hookId argument as null or blank.

~~~~~
// Remove this hook event, preventing it from executing again
$event->removeHook(null);
~~~~~

## Arguments

- string|HookEvent|null $hookId

## Return value

HookEvent|WireData $this
