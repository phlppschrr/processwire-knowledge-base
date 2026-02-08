# $selector->evaluate($matches): bool

Source: `wire/core/Selector.php`

Provides the opportunity to override or NOT the condition

Selectors should include a call to this in their matches function

## Usage

~~~~~
// basic usage
$bool = $selector->evaluate($matches);
~~~~~

## Arguments

- `$matches` `bool`

## Return value

- `bool`
