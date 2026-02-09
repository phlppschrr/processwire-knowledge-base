# ImageInspector

Source: `wire/core/ImageInspector.php`

Inherits: `WireData`

Image Inspector

Upgrades ImageSizer and ImageSizerEngines with more in depth information of imagefiles and -formats.

Copyright (C) 2016 by Horst Nogajski and Ryan Cramer
This file licensed under Mozilla Public License v2.0 http://mozilla.org/MPL/2.0/

For modules that extend this, use: autoload=false, singular=false.

Methods:
- [`__construct(string $filename = '')`](method-__construct.md)
- [`inspect(string $filename = '', bool $parseAppmarker = false): null|false|array`](method-inspect.md)
- [`checkOrientation($filename): array`](method-checkorientation.md)
- [`loadImageInfoPng(): bool`](method-loadimageinfopng.md)
- [`loadImageInfoGif(): bool`](method-loadimageinfogif.md)
- [`loadImageInfoJpg()`](method-loadimageinfojpg.md)
