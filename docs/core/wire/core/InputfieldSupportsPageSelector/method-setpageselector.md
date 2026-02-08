# $inputfieldSupportsPageSelector->setPageSelector($selector): bool

Source: `wire/core/Interfaces.php`

Set page selector or test if feature is disabledd

## Usage

~~~~~
// basic usage
$bool = $inputfieldSupportsPageSelector->setPageSelector($selector);
~~~~~

## Arguments

- `$selector` `string` Selector string or blank string when testing if feature is disabled

## Return value

- `bool` Return boolean false if feature disabled, otherwise boolean true
