# ImageSizerEngineGD::processAction()

Source: `wire/core/ImageSizerEngineGD.php`

Process a rotate or flip action

@param string $srcFilename

@param string $dstFilename

@param string $action One of 'rotate' or 'flip'

@param int|string $value If rotate, specify int of degrees. If flip, specify one of 'vertical', 'horizontal' or 'both'.

@return bool

@throws WireException
