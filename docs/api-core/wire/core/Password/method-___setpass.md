# $password->setPass($value)

Source: `wire/core/Password.php`

Set the 'pass' to the given value

## Usage

~~~~~
// basic usage
$result = $password->setPass($value);
~~~~~

## Arguments

- `$value` `string`

## Hooking

- Hookable method name: `setPass`
- Implementation: `___setPass`
- Hook with: `Password::setPass`

### Hooking Before

~~~~~
$this->addHookBefore('Password::setPass', function(HookEvent $event) {
  $password = $event->object;

  // Get arguments
  $value = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $value);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Password::setPass', function(HookEvent $event) {
  $password = $event->object;

  // Get arguments
  $value = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException` if given invalid $value
