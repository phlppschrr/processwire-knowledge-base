# $tfa->success(): bool

Source: `wire/core/Tfa.php`

Returns true when TFA has successfully completed and user is now logged in

Note that this method functions as part of the TFA flow control and will
perform redirects during processing.

## Usage

~~~~~
// basic usage
$bool = $tfa->success();
~~~~~

## Return value

- `bool`
