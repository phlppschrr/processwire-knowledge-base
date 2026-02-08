# $commentNotifications->parseEmails($str): array

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentNotifications.php`

Given a string containing emails or references to them, convert to array of emails

Recognized email references are:
	- Regular email address: "email@company.com"
	- Pull email from field on current page: "field:email_field_name"
	- Pull email from user account (field=email): "user:karen"
	- Pull email from page ID and field name: "123:email_field_name"
	- Pull email from page path and field name: "/path/to/page:email_field_name"

## Arguments

- $str

## Return value

array
