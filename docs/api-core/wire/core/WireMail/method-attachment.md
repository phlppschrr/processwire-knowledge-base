# $wireMail->attachment($value, $filename = ''): $this

Source: `wire/core/WireMail.php`

Add a file to be attached to the email



- Multiple calls will append attachments.
- To remove the supplied attachments, specify NULL as the value.
- Attachments may or may not be supported by 3rd party WireMail modules.

## Example

~~~~~~
$m = wireMail();
$m->to('user@domain.com')->from('hello@world.com');
$m->subject('Test attachment');
$m->body('This is just a test of a file attachment');
$m->attachment('/path/to/file.jpg');
$m->send();
~~~~~~

## Usage

~~~~~
// basic usage
$result = $wireMail->attachment($value);

// usage with all arguments
$result = $wireMail->attachment($value, $filename = '');
~~~~~

## Arguments

- `$value` `string` Full path and filename of file attachment
- `$filename` (optional) `string` Optional different basename for file as it appears in the mail

## Return value

- `$this`
