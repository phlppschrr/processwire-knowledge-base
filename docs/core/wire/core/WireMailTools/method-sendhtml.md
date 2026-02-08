# WireMailTools::sendHTML()

Source: `wire/core/WireMailTools.php`

Send an email with given message text assumed to be HTML

This is just like the `$mail->send()` method with the exception that the body argument
is assumed to be HTML rather than text. Note that the text version of the email is auto
generated from the HTML, unless a `body` is provided in the `$options` array.

@param string|array $to Email address TO. For multiple, specify CSV string or array.

@param string $from Email address FROM. This may be an email address, or a combined name and email address.
  Example of combined name and email: `Karen Cramer <karen@processwire.com>`

@param string $subject Email subject

@param string $bodyHTML Email body in HTML

@param array|string $options Array of options OR the $bodyHTML string. Array $options are:
 - `body` (string): Email body (text)
 - `replyTo` (string): Reply-to email address
 - `headers` (array): Associative array of header name => header value
 - Any additional options will be sent along to the WireMail module or class, in tact.

@return int|WireMail Returns number of messages sent or WireMail object if no arguments specified.
