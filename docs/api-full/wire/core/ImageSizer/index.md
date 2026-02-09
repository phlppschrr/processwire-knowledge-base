# ImageSizer

Source: `wire/core/ImageSizer.php`

Inherits: `Wire`

## Summary

ProcessWire ImageSizer with Engines for ProcessWire 3.x

Common methods:
- [`getEngines()`](method-getengines.md)
- [`getEngineInfo()`](method-getengineinfo.md)
- [`newImageSizerEngine()`](method-newimagesizerengine.md)
- [`newDefaultImageSizerEngine()`](method-newdefaultimagesizerengine.md)
- [`resize()`](method-___resize.md)

Groups:
Group: [other](group-other.md)

ImageSizer handles resizing of a single JPG, GIF, or PNG image using GD2
or another supported and configured engine. (Imagick, ImageMagick, Netpbm)

Code for IPTC, auto rotation and sharpening by Horst Nogajski.
http://nogajski.de/

Other user contributions as noted.

Copyright (C) 2016-2019 by Horst Nogajski and Ryan Cramer
This file licensed under Mozilla Public License v2.0 http://mozilla.org/MPL/2.0/

## Methods
- [`__construct(string $filename = '', array $options = array())`](method-__construct.md) Construct the ImageSizer for a single image
- [`getEngines(bool $forceReload = false): array`](method-getengines.md) Get array of all available ImageSizer engine names in order of priority
- [`getEngineInfo(string $name = ''): array`](method-getengineinfo.md) Get array of information for all ImageSizer engines (or optionally a specific ImageSizer engine)
- [`newImageSizerEngine(string $filename = '', array $options = array(), null|array $inspectionResult = null): ImageSizerEngine|null`](method-newimagesizerengine.md) Instantiate an ImageSizerEngine
- [`newDefaultImageSizerEngine(string $filename = '', array $options = array(), null|array $inspectionResult = null): ImageSizerEngine|null`](method-newdefaultimagesizerengine.md) Get the default/fallback ImageSizer engine
- [`resize(int $targetWidth, int $targetHeight = 0): bool`](method-___resize.md) (hookable) Resize the image proportionally to the given width/height
- [`resizeFallback(mixed $targetWidth, mixed $targetHeight = 0): bool`](method-resizefallback.md) GD is the fallback ImageEngine, it gets invoked if there is no other Engine defined,
- [`setFilename($filename): $this`](method-setfilename.md) Set the filename
- [`setForceEngine($engineName): $this`](method-setforceengine.md) Force the use of a specific engine
- [`setOptions(array $options): $this`](method-setoptions.md) Set multiple resize options
- [`setModified($modified): $this`](method-setmodified.md) Set whether a modification was made
- [`getEngine(string $engineName = ''): ImageSizerEngine|null`](method-getengine.md) Get the current ImageSizerEngine
- [`getImageInfo(bool $rawData = false): string|array`](method-getimageinfo.md) ImageInformation from Image Inspector in short form or full RawInfoData
- [`rotate(int $degrees): bool`](method-rotate.md) Rotate image by given degrees
- [`flipVertical(): bool`](method-flipvertical.md) Flip image vertically
- [`flipHorizontal(): bool`](method-fliphorizontal.md) Flip image horizontally
- [`flipBoth(): bool`](method-flipboth.md) Flip both vertically and horizontally
- [`convertToGreyscale(): bool`](method-converttogreyscale.md) Convert image to greyscale (black and white)
- [`convertToSepia(int $sepia = 55): bool`](method-converttosepia.md) Convert image to sepia tone
