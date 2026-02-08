# $wireMailTools->send($to = '', $from = '', $subject = '', $body = '', $options = array()): int|WireMail

Source: `wire/core/WireMailTools.php`

Send an email

- Note that the order of arguments is slightly different from PHP's `mail()` function.
- If no arguments are specified it simply returns a `WireMail` object (see #5 in examples).
- This function will attempt to use an installed module that extends `WireMail`.
  If no module is installed, `WireMail` (which uses PHP mail) will be used instead.

~~~~~
// 1. Default usage:
$mail->send($to, $from, $subject, $body);

// 2. Default usage with options array:
$mail->send($to, $from, $subject, $body, $options);

// 3. Specify body and/or bodyHTML in $options array (perhaps with other options):
$mail->send($to, $from, $subject, $options);

// 4. Specify both $body and $bodyHTML as arguments, but no $options:
$mail->send($to, $from, $subject, $body, $bodyHTML);

// 5. Specify a blank call to wireMail() to get the WireMail sending module:
$wireMail = $mail->send();
~~~~~

## Arguments

- `$to` (optional) `string|array` Email address TO. For multiple, specify CSV string or array.
- `$from` (optional) `string` Email address FROM. This may be an email address, or a combined name and email address. Example of combined name and email: `Karen Cramer <karen@processwire.com>`
- `$subject` (optional) `string` Email subject
- `$body` (optional) `string|array` Email body or omit to move straight to $options
- `$options` (optional) `array|string` Array of options OR the $bodyHTML string. Array $options are: - `body` (string): Email body (text) - `bodyHTML` (string): Email body (HTML) - `replyTo` (string): Reply-to email address - `headers` (array): Associative array of header name => header value - Any additional options will be sent along to the WireMail module or class, in tact.

## Return value

int|WireMail Returns number of messages sent or WireMail object if no arguments specified.
