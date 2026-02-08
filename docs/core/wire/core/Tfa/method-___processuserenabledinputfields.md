# $tfa->___processUserEnabledInputfields(User $user, InputfieldWrapper $fieldset, $settings, $settingsPrev): array

Source: `wire/core/Tfa.php`

Called when the user config fieldset has been processed (for enabled user) but before $settings have been saved

## Arguments

- User $user
- InputfieldWrapper $fieldset
- array $settings Associative array of new/current settings after processing
- array $settingsPrev Associative array of previous settings

## Return value

array Return $newSettings array (modified as needed)
