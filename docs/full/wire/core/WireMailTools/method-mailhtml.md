# WireMailTools::mailHTML()

Source: `wire/core/WireMailTools.php`

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
