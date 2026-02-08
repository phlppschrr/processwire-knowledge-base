# CommentNotifications::modifyNotifications()

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentNotifications.php`

Given a subscriber code, modify notifications on any comments where their email is present

@param string $subcode 40 digit subscriber code

@param bool $enable Whether to enable or disable notifications

@param bool $all Specify true to disable notifications site-wide, rather than just current page

@throws WireException

@return bool
