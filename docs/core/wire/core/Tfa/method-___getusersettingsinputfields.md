# $tfa->getUserSettingsInputfields(User $user, InputfieldWrapper $fieldset, $settings)

Source: `wire/core/Tfa.php`

Get fields needed for a user to configure and confirm TFA from their user profile

This method should be implemented by each TFA module. It is only used when the user has selected
a TFA type and submitted form, but has not yet configured the TFA type.

## Usage

~~~~~
// basic usage
$result = $tfa->getUserSettingsInputfields($user, $fieldset, $settings);

// usage with all arguments
$result = $tfa->getUserSettingsInputfields(User $user, InputfieldWrapper $fieldset, $settings);
~~~~~

## Arguments

- `$user` `User`
- `$fieldset` `InputfieldWrapper`
- `$settings` `array`

## Hooking

- Hookable method name: `getUserSettingsInputfields`
- Implementation: `___getUserSettingsInputfields`
- Hook with: `Tfa::getUserSettingsInputfields`

### Hooking Before

~~~~~
$this->addHookBefore('Tfa::getUserSettingsInputfields', function(HookEvent $event) {
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
$this->addHookAfter('Tfa::getUserSettingsInputfields', function(HookEvent $event) {
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
