# WireMailTools

Source: `wire/core/WireMailTools.php`

ProcessWire Mail Tools ($mail API variable)

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

Provides an API interface to email and WireMail.
~~~~~
// Simple usage example
$message = $mail->new();
$message->subject('Hello world')
  ->to('user@domain.com')
  ->from('you@company.com')
  ->body('Hello there big world')
  ->bodyHTML('<h2>Hello there big world</h2>');
$numSent = $message->send();

// ProcessWire 3.0.113 lets you skip the $mail->new() call if you want:
$numSent = $mail->subject('Hello world')
  ->to('user@domain.com')
  ->from('you@company.com')
  ->body('Hello there big world')
  ->bodyHTML('<h2>Hello there big world</h2>')
  ->send();
~~~~~

## other

@method WireMail new($options = array()) Create a new WireMail() instance

@method bool|string isBlacklistEmail($email, array $options = array())

@property WireMail new Get a new WireMail() instance (same as method version)

## ___new()

Get a new WireMail instance for sending email

Note: The `$options` argument added in 3.0.123, previous versions had no $options argument.

~~~~~
$message = $mail->new();
$message->to('user@domain.com')->from('you@company.com');
$message->subject('Mail Subject')->body('Mail Body Text')->bodyHTML('Body HTML');
$numSent = $message->send();
~~~~~


@param array|string $options Optional settings to override defaults, or string for `module` option:
 - `module` (string): Class name of WireMail module you want to use rather than auto detect, or 'WireMail' to force using default PHP mail.
   If requested module is not available, it will fall-back to one that is (or PHP mail), so check class name of returned value if there
   is any doubt about what WireMail module is being used.
 - You may also specify: subject, from, fromName, to, toName, subject or any other WireMail property and it will be populated.

@return WireMail

## send()

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

@param string|array $to Email address TO. For multiple, specify CSV string or array.

@param string $from Email address FROM. This may be an email address, or a combined name and email address.
  Example of combined name and email: `Karen Cramer <karen@processwire.com>`

@param string $subject Email subject

@param string|array $body Email body or omit to move straight to $options

@param array|string $options Array of options OR the $bodyHTML string. Array $options are:
 - `body` (string): Email body (text)
 - `bodyHTML` (string): Email body (HTML)
 - `replyTo` (string): Reply-to email address
 - `headers` (array): Associative array of header name => header value
 - Any additional options will be sent along to the WireMail module or class, in tact.

@return int|WireMail Returns number of messages sent or WireMail object if no arguments specified.

## sendHTML()

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

## mail()

Send an email, drop-in replacement for PHP mail() that uses the same arguments

This is an alternative to using the `$mail->send()` method, and may be simpler for those converting
existing PHP `mail()` calls to WireMail calls.

This function duplicates the same arguments as PHP’s mail function, enabling you to replace an existing
PHP `mail(…)` call with `$mail->mail(…)`.

But unlike PHP’s mail function, this one can also send HTML (or multipart) emails if you provide
an `$options` array for the `$message` argument (rather than a string). See the options array for
the `$mail->send()` method for details.
~~~~~
// 1. Basic PHP mail() style usage
$mail->mail('ryan@processwire.com', 'Subject', 'Message body');

// 2. PHP mail() style usage with with $headers argument
$mail->mail('ryan@processwire.com', 'Subject', 'Message body', 'From: hello@world.com');

// 3. Alternate usage with html and text body
$mail->mail('ryan@processwire.com', 'Subject', [
  'bodyHTML' => '<html><body><h1>Message HTML body</h1></body</html>',
  'body' => 'Message text body',
  'from' => 'hello@world.com',
]);
~~~~~

@param string|array $to Email address TO. For multiple, specify CSV string or array.

@param string $subject Email subject

@param string|array $message Email body (PHP mail style), OR specify $options array with any of the following:
 - `bodyHTML` (string): Email body (HTML)
 - `body` (string): Email body (text). If not specified, and bodyHTML is, then text body will be auto-generated.
 - `from` (string): From email address
 - `replyTo` (string): Reply-to email address
 - `headers` (array): Associative array of header name => header value

@param array $headers Optional additional headers as [name=value] array or "Name: Value" newline-separated string.
  Use this argument to duplicate PHP mail() style arguments. No need to use if you used $options array for the $message argument.

@return bool True on success, false on fail.

## mailHTML()

Send an email with message assumed to be in HTML

This is the same as the `$mail->mail()` method except that the message argument is
assumed to be HTML rather than text. The text version of the email will be auto-generated
from the given HTML.

@param string|array $to Email address TO. For multiple, specify CSV string or array.

@param string $subject Email subject

@param string|array Email message in HTML

@param array $headers Optional additional headers as [name=value] array or "Name: Value" newline-separated string.
  Use this argument to duplicate PHP mail() style arguments. No need to use if you used $options array for the $message argument.

@return bool True on success, false on fail.

@since 3.0.109

## to()

Return new WireMail instance populated with “to” email

@param string|array $email Email to send to–specify any one of the following:
- Single email address
- String like: "John Smith <user@example.com>"
- CSV string of either of the above.
- Regular PHP array of email addresses.
- Associative array of ['user@xample.com' => 'John Smith'].

@param string $name An optional TO name, applies only if your $email argument was just an email address.

@return WireMail

@throws WireException if given invalid email address

@since 3.0.113

## from()

Return new WireMail instance populated with “from” email

@param string $email Must be a single email address or "User Name <user@example.com>" string.

@param string|null An optional FROM name

@return WireMail

@since 3.0.113

## subject()

Return new WireMail instance populated with subject

@param string $subject

@return WireMail

@since 3.0.113

## ___isBlacklistEmail()

Is given email address in the blacklist?

- Returns boolean false if not blacklisted, true if it is.
- Uses `$config->wireMail['blacklist']` array unless given another blacklist array in $options.
- Always independently verify that your blacklist rules are working before assuming they do.
- Specify true for the `why` option if you want to return the matching rule when email is in blacklist.
- Specify true for the `throw` option if you want a WireException thrown when email is blacklisted.

~~~~~
// Define blacklist in /site/config.php
$config->wireMail('blacklist', [
  'email@domain.com', // blacklist this email address
  '@host.domain.com', // blacklist all emails ending with @host.domain.com
  '@domain.com', // blacklist all emails ending with @domain.com
  'domain.com', // blacklist any email address ending with domain.com (would include mydomain.com too).
  '.domain.com', // blacklist any email address at any host off domain.com (domain.com, my.domain.com, but NOT mydomain.com).
  '/something/', // blacklist any email containing "something". PCRE regex assumed when "/" is used as opening/closing delimiter.
  '/.+@really\.bad\.com$/', // another example of using a PCRE regular expression (blocks all "@really.bad.com").
]);

// Test if email in blacklist
$email = 'somebody@domain.com';
$result = $mail->isBlacklistEmail($email, [ 'why' => true ]);
if($result === false) {
  echo "<p>Email address is not blacklisted</p>";
} else {
  echo "<p>Email is blacklisted by rule: $result</p>";
}
~~~~~

@param string $email Email to check

@param array $options
 - `blacklist` (array): Use this blacklist rather than `$config->emailBlacklist` (default=[])
 - `throw` (bool): Throw WireException if email is blacklisted? (default=false)
 - `why` (bool): Return string containing matching rule when email is blacklisted? (default=false)

@return bool|string Returns true if email is blacklisted, false if not. Returns string if `why` option specified + email blacklisted.

@throws WireException if given a blacklist that is not an array, or if requested to via `throw` option.

@since 3.0.129
