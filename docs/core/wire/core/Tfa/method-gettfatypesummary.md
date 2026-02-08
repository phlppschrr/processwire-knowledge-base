# Tfa::getTfaTypeSummary()

Source: `wire/core/Tfa.php`

Get translated Tfa type summary

This is generally the same or similar to the module summary, though in a $this->_('…'); call
so that it is translatable. When a module implements this, it should not make a
parent::getTfaTypeLabel() call.

@return string

@since 3.0.160
