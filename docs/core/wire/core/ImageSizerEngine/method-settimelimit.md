# ImageSizerEngine::setTimeLimit()

Source: `wire/core/ImageSizerEngine.php`

Set a time limit for manipulating one image (default is 30)

If specified time limit is less than PHP's max_execution_time, then PHP's setting will be used instead.

@param int $value 10 to 60 recommended, default is 30

@return self
