# $wireMail->___send(): int

Source: `wire/core/WireMail.php`

Send the email

Call this method only after you have specified at least the `subject`, `to` and `body`.

## Usage

~~~~~
// basic usage
$int = $wireMail->___send();
~~~~~

## Return value

- `int` Returns a positive number (indicating number of addresses emailed) or 0 on failure.
