# $wireHooks->removeHook(Wire $object, $hookID): Wire

Source: `wire/core/WireHooks.php`

Given a Hook ID provided by addHook() this removes the hook

To have a hook function remove itself within the hook function, say this is your hook function:
function(HookEvent $event) {
  $event->removeHook(null); // remove self
}

## Arguments

- Wire $object
- string|array|null $hookID Can be single hook ID, array of hook IDs, or CSV string of hook IDs

## Return value

Wire
