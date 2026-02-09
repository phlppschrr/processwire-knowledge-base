# $selectors->getCustomVariableValue($name): null|string

Source: `wire/core/Selectors.php`

Get the value for a custom [var] to populate in a selector (also works in PageFinder)

This can be useful for cases where the variable would be stored somewhere in
a configuration, like a Lister selector or Page reference field selector, where PHP
variables typically wouldn't be available.

If hooking this method, /site/ready.php is recommended.

## Usage

~~~~~
// basic usage
$selectors->getCustomVariableValue($name);
~~~~~

## Arguments

- `$name` `string`

## Return value

- `null|string`

## Hooking

- Hookable method name: `getCustomVariableValue`
- Implementation: `___getCustomVariableValue`
- Hook with: `Selectors::getCustomVariableValue`

### Hooking Before

~~~~~
$this->addHookBefore('Selectors::getCustomVariableValue', function(HookEvent $event) {
  $selectors = $event->object;

  // Get arguments
  $name = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $name);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Selectors::getCustomVariableValue', function(HookEvent $event) {
  $selectors = $event->object;

  // Get arguments
  $name = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.255
