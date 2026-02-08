# $wireMail->bodyHTML($body): $this

Source: `wire/core/WireMail.php`

Set the email message body (HTML only)

This should be the text from an entire HTML document, not just an element.

## Example

~~~~~
$m = wireMail();
$m->bodyHTML('<html><body><h1>Hello world</h1></body></html>');
~~~~~

## Usage

~~~~~
// basic usage
$result = $wireMail->bodyHTML($body);
~~~~~

## Arguments

- `$body` `string` Email body in HTML

## Return value

- `$this`
