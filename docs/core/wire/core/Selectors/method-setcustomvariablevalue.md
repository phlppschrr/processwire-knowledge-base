# Selectors::setCustomVariableValue($name, $value)

Source: `wire/core/Selectors.php`

Set a custom [variable] value available to all Selectors and PageFinder class instances

~~~~
Selectors::setCustomVariableValue('foo', 'bar');
$s = new Selectors("name=[foo]");
echo $s; // outputs: "name=bar"
$pages->find("name=[foo]"); // finds pages with name=bar
~~~~

## Arguments

- string $name
- string|int|array|WireData|float|null|bool $value

## Meta

- @since 3.0.255
