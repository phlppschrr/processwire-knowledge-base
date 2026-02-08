# $commentNotifications->modifyNotifications($subcode, $enable, $all = false): bool

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentNotifications.php`

Given a subscriber code, modify notifications on any comments where their email is present

## Arguments

- string $subcode 40 digit subscriber code
- bool $enable Whether to enable or disable notifications
- bool $all Specify true to disable notifications site-wide, rather than just current page

## Return value

bool

## Throws

- WireException
