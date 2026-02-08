# $notificationArray->getNew($flag = 'message', $addNow = true): Notification

Source: `wire/modules/System/SystemNotifications/NotificationArray.php`

Get a new Notification

## Usage

~~~~~
// basic usage
$notification = $notificationArray->getNew();

// usage with all arguments
$notification = $notificationArray->getNew($flag = 'message', $addNow = true);
~~~~~

## Arguments

- `$flag` (optional) `string` Specify any flag, flag name or space-separated combination of flag names
- `$addNow` (optional) `bool` Add it to this NotificationArray now?

## Return value

- `Notification`
