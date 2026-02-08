# ImageSizerEngineGD::hasEnoughMemory()

Source: `wire/core/ImageSizerEngineGD.php`

Additional functionality on top of existing checkMemoryForImage function for the flip/rotate actions

@param string $filename Filename to check. Default is whatever was set to this ImageSizer.

@param bool $double Need enough for both src and dst files loaded at same time? (default=true)

@param int|float $factor Tweak factor (multiply needed memory by this factor), i.e. 2 for rotate actions. (default=1)

@param string $action Name of action (if something other than "action")

@param bool $throwIfNot Throw WireException if not enough memory? (default=false)

@return bool

@throws WireException
