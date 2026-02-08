# $admin->_checkForMaxInputVars(WireInput $input)

Source: `wire/core/admin.php`

Check if POST request exceeds PHP’s max_input_vars

## Usage

~~~~~
// basic usage
$result = $admin->_checkForMaxInputVars($input);

// usage with all arguments
$result = $admin->_checkForMaxInputVars(WireInput $input);
~~~~~

## Arguments

- `$input` `WireInput`
