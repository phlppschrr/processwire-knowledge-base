# Tfa::hookAfterInputfieldFormProcess()

Source: `wire/core/Tfa.php`

Hook after InputfieldForm::processInput()

This method grabs data from the TFA related fields added by our render() hooks,
and saves them in the user’s “tfa_type” field “settings” column.

@param HookEvent $event
