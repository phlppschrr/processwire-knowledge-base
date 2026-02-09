# WireHooks::___debug

Source: `wire/core/WireHooks.php`

Debug hooks

## Hookable

- Hookable method name: `debug`
- Implementation: `___debug`
- Hook with: `$wireHooks->debug()`

## Hooking Before

~~~~~
$this->addHookBefore('WireHooks::debug', function(HookEvent $event) {
  $wireHooks = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('WireHooks::debug', function(HookEvent $event) {
  $wireHooks = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
