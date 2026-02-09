# $tfa->getUserEnabledInputfields(User $user, InputfieldWrapper $fieldset, $settings)

Source: `wire/core/Tfa.php`

Get fields for when user already has TFA enabled

This method does not need to be implemented by TFA modules unless they want to add something to it.

## Usage

~~~~~
// basic usage
$result = $tfa->getUserEnabledInputfields($user, $fieldset, $settings);

// usage with all arguments
$result = $tfa->getUserEnabledInputfields(User $user, InputfieldWrapper $fieldset, $settings);
~~~~~

## Arguments

- `$user` `User`
- `$fieldset` `InputfieldWrapper`
- `$settings` `array`

## Hooking

- Hookable method name: `getUserEnabledInputfields`
- Implementation: `___getUserEnabledInputfields`
- Hook with: `Tfa::getUserEnabledInputfields`

### Hooking Before

~~~~~
$this->addHookBefore('Tfa::getUserEnabledInputfields', function(HookEvent $event) {
  $tfa = $event->object;

  // Get arguments
  $user = $event->arguments(0);
  $fieldset = $event->arguments(1);
  $settings = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $user);
  $event->arguments(1, $fieldset);
  $event->arguments(2, $settings);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Tfa::getUserEnabledInputfields', function(HookEvent $event) {
  $tfa = $event->object;

  // Get arguments
  $user = $event->arguments(0);
  $fieldset = $event->arguments(1);
  $settings = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
