# $wireMail->body($body): $this

Source: `wire/core/WireMail.php`

Set the email message body (text only)

## Example

~~~~~
$m = wireMail();
$m->body('Hello world');
~~~~~

## Usage

~~~~~
// basic usage
$result = $wireMail->body($body);
~~~~~

## Arguments

- `$body` `string` Email body in text only

## Return value

- `$this`
