# $notificationArray->error($text, $flags = 0): Notification

Source: `wire/modules/System/SystemNotifications/NotificationArray.php`

Record an error notification

## Usage

~~~~~
// basic usage
$notification = $notificationArray->error($text);

// usage with all arguments
$notification = $notificationArray->error($text, $flags = 0);
~~~~~

## Arguments

- `$text` `string`
- `$flags` (optional) `int|bool` See Notification flags

## Return value

- `Notification`
