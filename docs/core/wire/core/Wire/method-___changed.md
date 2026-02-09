# $wire->changed($what, $old = null, $new = null)

Source: `wire/core/Wire.php`

Hookable method that is called whenever a property has changed while change tracking is enabled.

- Enables hooks to monitor changes to the object.
- Do not call this method directly, as the `Wire::trackChange()` method already does so.
- Descending classes should call `$this->trackChange('name', $oldValue, $newValue);` when a property they are tracking has changed.

## Usage

~~~~~
// basic usage
$result = $wire->changed($what);

// usage with all arguments
$result = $wire->changed($what, $old = null, $new = null);
~~~~~

## Hookable

- Hookable method name: `changed`
- Implementation: `___changed`
- Hook with: `$wire->changed()`

## Hooking Before

~~~~~
$this->addHookBefore('Wire::changed', function(HookEvent $event) {
  $wire = $event->object;

  // Get arguments
  $what = $event->arguments(0);
  $old = $event->arguments(1);
  $new = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $what);
  $event->arguments(1, $old);
  $event->arguments(2, $new);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Wire::changed', function(HookEvent $event) {
  $wire = $event->object;

  // Get arguments
  $what = $event->arguments(0);
  $old = $event->arguments(1);
  $new = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$what` `string` Name of property that changed
- `$old` (optional) `mixed` Previous value before change
- `$new` (optional) `mixed` New value

## See Also

- [Wire::trackChange()](method-trackchange.md)
