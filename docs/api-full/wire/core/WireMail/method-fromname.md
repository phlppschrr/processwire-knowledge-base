# $wireMail->fromName($name): $this

Source: `wire/core/WireMail.php`

Set the 'from' name

It is preferable to do this with the from() method, but this is provided to ensure that
all properties can be set with direct access, i.e. $mailer->fromName = 'User Name';

## Usage

~~~~~
// basic usage
$result = $wireMail->fromName($name);
~~~~~

## Arguments

- `$name` `string` The 'from' name

## Return value

- `$this`
