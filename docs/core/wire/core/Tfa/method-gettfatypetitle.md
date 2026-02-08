# $tfa->getTfaTypeTitle(): string

Source: `wire/core/Tfa.php`

Get translated Tfa type title (longer name)

This is generally the same or similar to the module title, though in a $this->_('…'); call
so that it is translatable. When a module implements this, it should not make a
parent::getTfaTypeLabel() call.

## Return value

string

## Meta

- @since 3.0.160
