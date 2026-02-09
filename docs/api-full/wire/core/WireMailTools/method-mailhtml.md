# $wireMailTools->mailHTML($to, $subject, $messageHTML, $headers = array()): bool

Source: `wire/core/WireMailTools.php`

Send an email with message assumed to be in HTML

This is the same as the `$mail->mail()` method except that the message argument is
assumed to be HTML rather than text. The text version of the email will be auto-generated
from the given HTML.

## Usage

~~~~~
// basic usage
$bool = $wireMailTools->mailHTML($to, $subject, $messageHTML);

// usage with all arguments
$bool = $wireMailTools->mailHTML($to, $subject, $messageHTML, $headers = array());
~~~~~

## Arguments

- `$to` `string|array` Email address TO. For multiple, specify CSV string or array.
- `$subject` `string` Email subject
- string|array Email message in HTML
- `$headers` (optional) `array` Optional additional headers as [name=value] array or "Name: Value" newline-separated string. Use this argument to duplicate PHP mail() style arguments. No need to use if you used $options array for the $message argument.

## Return value

- `bool` True on success, false on fail.

## Since

3.0.109
