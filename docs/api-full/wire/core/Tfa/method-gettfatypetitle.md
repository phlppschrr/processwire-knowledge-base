# $tfa->getTfaTypeTitle(): string

Source: `wire/core/Tfa.php`

Get translated Tfa type title (longer name)

This is generally the same or similar to the module title, though in a $this->_('…'); call
so that it is translatable. When a module implements this, it should not make a
parent::getTfaTypeLabel() call.

## Usage

~~~~~
// basic usage
$string = $tfa->getTfaTypeTitle();
~~~~~

## Return value

- `string`

## Since

3.0.160
