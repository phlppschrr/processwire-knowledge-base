# $tfa->processUserSettingsInputfields(User $user, InputfieldWrapper $fieldset, $settings, $settingsPrev): array

Source: `wire/core/Tfa.php`

Called when the user config fieldset has been processed but before $settings have been saved

## Usage

~~~~~
// basic usage
$array = $tfa->processUserSettingsInputfields($user, $fieldset, $settings, $settingsPrev);

// usage with all arguments
$array = $tfa->processUserSettingsInputfields(User $user, InputfieldWrapper $fieldset, $settings, $settingsPrev);
~~~~~

## Hookable

- Hookable method name: `processUserSettingsInputfields`
- Implementation: `___processUserSettingsInputfields`
- Hook with: `$tfa->processUserSettingsInputfields()`

## Arguments

- `$user` `User`
- `$fieldset` `InputfieldWrapper`
- `$settings` `array` Associative array of new/current settings after processing
- `$settingsPrev` `array` Associative array of previous settings

## Return value

- `array` Return $newSettings array (modified as needed)
