# ImageSizer

Source: `wire/core/ImageSizer.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

ProcessWire ImageSizer with Engines for ProcessWire 3.x

ImageSizer handles resizing of a single JPG, GIF, or PNG image using GD2
or another supported and configured engine. (Imagick, ImageMagick, Netpbm)

Code for IPTC, auto rotation and sharpening by Horst Nogajski.
http://nogajski.de/

Other user contributions as noted.

Copyright (C) 2016-2019 by Horst Nogajski and Ryan Cramer
This file licensed under Mozilla Public License v2.0 http://mozilla.org/MPL/2.0/

Methods:
- [`__construct(string $filename = '', array $options = array())`](method-__construct.md)
- [`getEngines(bool $forceReload = false): array`](method-getengines.md)
- [`getEngineInfo(string $name = ''): array`](method-getengineinfo.md)
- [`newImageSizerEngine(string $filename = '', array $options = array(), null|array $inspectionResult = null): ImageSizerEngine|null`](method-newimagesizerengine.md)
- [`newDefaultImageSizerEngine(string $filename = '', array $options = array(), null|array $inspectionResult = null): ImageSizerEngine|null`](method-newdefaultimagesizerengine.md)
- [`resize(int $targetWidth, int $targetHeight = 0): bool`](method-___resize.md) (hookable)
- [`resizeFallback(mixed $targetWidth, mixed $targetHeight = 0): bool`](method-resizefallback.md)
- [`setFilename($filename): $this`](method-setfilename.md)
- [`setForceEngine($engineName): $this`](method-setforceengine.md)
- [`setOptions(array $options): $this`](method-setoptions.md)
- [`setModified($modified): $this`](method-setmodified.md)
- [`getEngine(string $engineName = ''): ImageSizerEngine|null`](method-getengine.md)
- [`getImageInfo(bool $rawData = false): string|array`](method-getimageinfo.md)
- [`rotate(int $degrees): bool`](method-rotate.md)
- [`flipVertical(): bool`](method-flipvertical.md)
- [`flipHorizontal(): bool`](method-fliphorizontal.md)
- [`flipBoth(): bool`](method-flipboth.md)
- [`convertToGreyscale(): bool`](method-converttogreyscale.md)
- [`convertToSepia(int $sepia = 55): bool`](method-converttosepia.md)
