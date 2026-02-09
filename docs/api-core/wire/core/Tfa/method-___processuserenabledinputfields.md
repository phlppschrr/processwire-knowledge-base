# $tfa->processUserEnabledInputfields(User $user, InputfieldWrapper $fieldset, $settings, $settingsPrev): array

Source: `wire/core/Tfa.php`

Called when the user config fieldset has been processed (for enabled user) but before $settings have been saved

## Usage

~~~~~
// basic usage
$array = $tfa->processUserEnabledInputfields($user, $fieldset, $settings, $settingsPrev);

// usage with all arguments
$array = $tfa->processUserEnabledInputfields(User $user, InputfieldWrapper $fieldset, $settings, $settingsPrev);
~~~~~

## Arguments

- `$user` `User`
- `$fieldset` `InputfieldWrapper`
- `$settings` `array` Associative array of new/current settings after processing
- `$settingsPrev` `array` Associative array of previous settings

## Return value

- `array` Return $newSettings array (modified as needed)

## Hooking

- Hookable method name: `processUserEnabledInputfields`
- Implementation: `___processUserEnabledInputfields`
- Hook with: `Tfa::processUserEnabledInputfields`

### Hooking Before

~~~~~
$this->addHookBefore('Tfa::processUserEnabledInputfields', function(HookEvent $event) {
  $tfa = $event->object;

  // Get arguments
  $user = $event->arguments(0);
  $fieldset = $event->arguments(1);
  $settings = $event->arguments(2);
  $settingsPrev = $event->arguments(3);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $user);
  $event->arguments(1, $fieldset);
  $event->arguments(2, $settings);
  $event->arguments(3, $settingsPrev);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Tfa::processUserEnabledInputfields', function(HookEvent $event) {
  $tfa = $event->object;

  // Get arguments
  $user = $event->arguments(0);
  $fieldset = $event->arguments(1);
  $settings = $event->arguments(2);
  $settingsPrev = $event->arguments(3);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
