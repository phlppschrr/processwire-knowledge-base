# $wireMailTools->___new($options = array()): WireMail

Source: `wire/core/WireMailTools.php`

Get a new WireMail instance for sending email

Note: The `$options` argument added in 3.0.123, previous versions had no $options argument.

~~~~~
$message = $mail->new();
$message->to('user@domain.com')->from('you@company.com');
$message->subject('Mail Subject')->body('Mail Body Text')->bodyHTML('Body HTML');
$numSent = $message->send();
~~~~~

## Arguments

- `$options` (optional) `array|string` Optional settings to override defaults, or string for `module` option: - `module` (string): Class name of WireMail module you want to use rather than auto detect, or 'WireMail' to force using default PHP mail. If requested module is not available, it will fall-back to one that is (or PHP mail), so check class name of returned value if there is any doubt about what WireMail module is being used. - You may also specify: subject, from, fromName, to, toName, subject or any other WireMail property and it will be populated.

## Return value

WireMail
