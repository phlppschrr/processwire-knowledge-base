# $tfa->hookInputfieldFormRender(HookEvent $event)

Source: `wire/core/Tfa.php`

Hook before InputfieldForm::render()

This method adds the fields configured in getUserSettingsInputfields() and adds
them to the form being rendered, but only if the form already has a field
named “tfa_type”. It also pulls the settings stored in that field, and
populates the module-specific configuration fields.

## Usage

~~~~~
// basic usage
$result = $tfa->hookInputfieldFormRender($event);

// usage with all arguments
$result = $tfa->hookInputfieldFormRender(HookEvent $event);
~~~~~

## Arguments

- `$event` `HookEvent`
