# $commentNotifications->modifyNotifications($subcode, $enable, $all = false): bool

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentNotifications.php`

Given a subscriber code, modify notifications on any comments where their email is present

## Usage

~~~~~
// basic usage
$bool = $commentNotifications->modifyNotifications($subcode, $enable);

// usage with all arguments
$bool = $commentNotifications->modifyNotifications($subcode, $enable, $all = false);
~~~~~

## Arguments

- `$subcode` `string` 40 digit subscriber code
- `$enable` `bool` Whether to enable or disable notifications
- `$all` (optional) `bool` Specify true to disable notifications site-wide, rather than just current page

## Return value

- `bool`

## Exceptions

- `WireException`
