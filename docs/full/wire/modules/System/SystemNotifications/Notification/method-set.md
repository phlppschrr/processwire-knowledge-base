# $notification->set($key, $value): self|Notification|WireData

Source: `wire/modules/System/SystemNotifications/Notification.php`

Set a value to the Notification

Note: setting the 'expires' value accepts either a future date, or a quantity of seconds
in the future relative to now.

## Usage

~~~~~
// basic usage
$result = $notification->set($key, $value);
~~~~~

## Arguments

- `$key` `string`
- `$value` `mixed`

## Return value

- `self|Notification|WireData`
