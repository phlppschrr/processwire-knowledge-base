# $imageSizerEngine->setCropping($cropping = true): self

Source: `wire/core/ImageSizerEngine.php`

Turn on/off cropping and/or set cropping direction

## Arguments

- bool|string|array $cropping Specify one of: northwest, north, northeast, west, center, east, southwest, south, southeast. Or a string of: 50%,50% (x and y percentages to crop from) Or an array('50%', '50%') Or to disable cropping, specify boolean false. To enable cropping with default (center), you may also specify boolean true.

## Return value

self
