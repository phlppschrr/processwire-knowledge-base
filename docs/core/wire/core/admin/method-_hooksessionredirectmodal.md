# $admin->_hookSessionRedirectModal(HookEvent $event)

Source: `wire/core/admin.php`

Ensures a modal GET variable is retained through redirects, when appropriate

## Usage

~~~~~
// basic usage
$result = $admin->_hookSessionRedirectModal($event);

// usage with all arguments
$result = $admin->_hookSessionRedirectModal(HookEvent $event);
~~~~~

## Arguments

- `$event` `HookEvent`
