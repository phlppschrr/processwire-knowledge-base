# Tfa::___processUserSettingsInputfields()

Source: `wire/core/Tfa.php`

Called when the user config fieldset has been processed but before $settings have been saved

@param User $user

@param InputfieldWrapper $fieldset

@param array $settings Associative array of new/current settings after processing

@param array $settingsPrev Associative array of previous settings

@return array Return $newSettings array (modified as needed)
