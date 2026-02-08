# $functions->wireMail($to = '', $from = '', $subject = '', $body = '', $options = array()): int|WireMail

Source: `wire/core/Functions.php`

Send an email or get a WireMail object to populate before send

- Please note that the order of arguments is different from PHP’s mail() function.
- If no arguments are specified it simply returns a WireMail object (see #4 below).
- This is a procedural version of functions provided by the `$mail` API variable (see that for more options).
- This function will attempt to use an installed module that extends WireMail.
- If no other WireMail module is installed, the default `WireMail` (which uses PHP mail) will be used instead.

~~~~~~
// Default usage:
wireMail($to, $from, $subject, $body, $options);

// Specify body and/or bodyHTML in $options array (perhaps with other options):
$options = [ 'body' => $body, 'bodyHTML' => $bodyHTML ];
wireMail($to, $from, $subject, $options);

// Specify both $body and $bodyHTML as arguments, but no $options:
wireMail($to, $from, $subject, $body, $bodyHTML);

// Specify a blank call to wireMail() to get the WireMail sending object. This can
// be either WireMail() or a class descending from it. If a WireMail descending
// module is installed, it will be returned rather than WireMail():
$mail = wireMail();
$mail->to('user@domain.com')->from('you@company.com');
$mail->subject('Mail Subject')->body('Mail Body Text')->bodyHTML('Body HTML');
$numSent = $mail->send();

## Usage

~~~~~
// basic usage
$int = $functions->wireMail();

// usage with all arguments
$int = $functions->wireMail($to = '', $from = '', $subject = '', $body = '', $options = array());
~~~~~

## Arguments

- `$to` (optional) `string|array` Email address TO. For multiple, specify CSV string or array.
- `$from` (optional) `string` Email address FROM. This may be an email address, or a combined name and email address. Example of combined name and email: `Karen Cramer <karen@processwire.com>`
- `$subject` (optional) `string` Email subject
- `$body` (optional) `string|array` Email body or omit to move straight to $options array
- `$options` (optional) `array|string` Array of options OR the $bodyHTML string. Array $options are: - `bodyHTML` (string): Email body as HTML. - `body` (string): Email body as plain text. This is created automatically if you only provide $bodyHTML. - `headers` (array): Associative array of ['header name' => 'header value'] - Any additional options you provide will be sent along to the WireMail module or class, in tact.

## Return value

- `int|WireMail` Returns number of messages sent or WireMail object if no arguments specified.
