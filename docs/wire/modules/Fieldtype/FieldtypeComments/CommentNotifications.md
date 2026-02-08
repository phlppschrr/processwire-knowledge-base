# CommentNotifications

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentNotifications.php`


## other

@method int sendAdminNotificationEmail(Comment $comment)

@method int sendNotificationEmail(Comment $comment, $email, $subcode, array $options = array())

## setMailer()

Set name of WireMail module to use for sending notifications

@param string $mailer

## newMail()

@return WireMail

## ___sendAdminNotificationEmail()

Send notification email to specified admin to review the comment

@param Comment $comment

@return int Number of emails sent

## parseEmails()

Given a string containing emails or references to them, convert to array of emails

Recognized email references are:
	- Regular email address: "email@company.com"
	- Pull email from field on current page: "field:email_field_name"
	- Pull email from user account (field=email): "user:karen"
	- Pull email from page ID and field name: "123:email_field_name"
	- Pull email from page path and field name: "/path/to/page:email_field_name"

@param $str

@return array

## checkActions()

Check for a GET variable comment approval code and take action is valid

@return array(
	'success' => true|false, whether or not comment was updated
	'valid' => true|false, whether or not the request was valid
	'action' => approve|spam|pending|unknown
	'message' => 'string',
	'pageID' => id of page or 0 if not known
	'fieldName' => 'name of field or blank if not known'
	'commentID' => id of comment or 0 if not applicable,
)

## modifyNotifications()

Given a subscriber code, modify notifications on any comments where their email is present

@param string $subcode 40 digit subscriber code

@param bool $enable Whether to enable or disable notifications

@param bool $all Specify true to disable notifications site-wide, rather than just current page

@throws WireException

@return bool

## ___sendNotificationEmail()

Send a user (not admin) notification email

@param Comment $comment

@param string|array $email

@param string $subcode Subscribe/unsubscribe code or blank string if not in use

@param array $options

@return int

## ___sendConfirmationEmail()

Send confirmation/opt-in email for notifications (not yet active)

@param Comment $comment

@param $email

@param $subcode

@return mixed

@throws WireException
