# $tfa->___buildAuthCodeForm(): InputfieldForm

Source: `wire/core/Tfa.php`

Build the form used for two-factor authentication

This form typically appears on the screen after the user has submitted their login info

At minimum it must have an Inputfield with name “tfa_code”

## Usage

~~~~~
// basic usage
$inputfieldForm = $tfa->___buildAuthCodeForm();
~~~~~

## Return value

- `InputfieldForm`
