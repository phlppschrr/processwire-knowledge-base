# Tfa::hookInputfieldFormRender()

Source: `wire/core/Tfa.php`

Hook before InputfieldForm::render()

This method adds the fields configured in getUserSettingsInputfields() and adds
them to the form being rendered, but only if the form already has a field
named “tfa_type”. It also pulls the settings stored in that field, and
populates the module-specific configuration fields.

@param HookEvent $event
