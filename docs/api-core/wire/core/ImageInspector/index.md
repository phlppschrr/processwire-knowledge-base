# ImageInspector

Source: `wire/core/ImageInspector.php`

Inherits: `WireData`

Image Inspector

Upgrades ImageSizer and ImageSizerEngines with more in depth information of imagefiles and -formats.

Copyright (C) 2016 by Horst Nogajski and Ryan Cramer
This file licensed under Mozilla Public License v2.0 http://mozilla.org/MPL/2.0/

For modules that extend this, use: autoload=false, singular=false.

Methods:
- [`__construct(string $filename = '')`](method-__construct.md) Construct
- [`inspect(string $filename = '', bool $parseAppmarker = false): null|false|array`](method-inspect.md) parse Image and return information
- [`checkOrientation($filename): array`](method-checkorientation.md) Check orientation (@horst)
- [`loadImageInfoPng(): bool`](method-loadimageinfopng.md) parse PNG Image and collect information into $this->info
- [`loadImageInfoGif(): bool`](method-loadimageinfogif.md) parse GIF Image and collect information into $this->info
- [`loadImageInfoJpg()`](method-loadimageinfojpg.md) parse JPEG Image and collect information into $this->info
