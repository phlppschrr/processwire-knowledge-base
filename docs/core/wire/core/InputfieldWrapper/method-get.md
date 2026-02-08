# $inputfieldWrapper->get($key): Inputfield|mixed

Source: `wire/core/InputfieldWrapper.php`

Get a child Inputfield having a name attribute matching the given $key.

This method can also get settings, attributes or API variables, so long as they don't
collide with an Inputfield name. For that reason, you may prefer to use the `Inputfield::getSetting()`,
`Inputfield::attr()` or `Wire::wire()` methods for those other purposes.

If you want a method that can only return a matching Inputfield object, use the
`InputfieldWrapper::getChildByName()` method .

## Arguments

- string $key Name of Inputfield or setting/property to retrieve.

## Return value

Inputfield|mixed

## Throws

- WireException Only in core development/debugging, otherwise does not throw exceptions.

## See also

- [InputfieldWrapper::getChildByName()](method-getchildbyname.md)
