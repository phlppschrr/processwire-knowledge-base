# $notification->flagNamesToFlags($names): array

Source: `wire/modules/System/SystemNotifications/Notification.php`

Given multiple space separated flag names, return array of flag values

## Usage

~~~~~
// basic usage
$array = $notification->flagNamesToFlags($names);
~~~~~

## Arguments

- `$names` `string` space separted, will also accept CSV

## Return value

- `array` of flag name => flag value
