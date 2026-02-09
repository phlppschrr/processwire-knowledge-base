# $tfa->hookBeforeInputfieldFormProcess(HookEvent $event)

Source: `wire/core/Tfa.php`

Hook before InputfieldForm::processInput()

## Usage

~~~~~
// basic usage
$result = $tfa->hookBeforeInputfieldFormProcess($event);

// usage with all arguments
$result = $tfa->hookBeforeInputfieldFormProcess(HookEvent $event);
~~~~~

## Arguments

- `$event` `HookEvent`
