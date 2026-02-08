# ImageSizer::getEngines()

Source: `wire/core/ImageSizer.php`

Get array of all available ImageSizer engine names in order of priority

Note that the returned value excludes the default engine (ImageSizerEngineGD).

@param bool $forceReload Specify true only if you want to prevent it from using cached result from previous call.

@return array of module names
