# ImageSizerEngineGD

Source: `wire/core/ImageSizerEngineGD.php`

Inherits: `ImageSizerEngine`

## Summary

ProcessWire ImageSizerGD

Common methods:
- [`validSourceImageFormats()`](method-validsourceimageformats.md)
- [`validTargetImageFormats()`](method-validtargetimageformats.md)
- [`getLibraryVersion()`](method-getlibraryversion.md)
- [`supported()`](method-supported.md)
- [`processResize()`](method-processresize.md)

Groups:
Group: [other](group-other.md)

Code for IPTC, auto rotation and sharpening by Horst Nogajski.
http://nogajski.de/

Other user contributions as noted.

Copyright (C) 2016-2019 by Horst Nogajski and Ryan Cramer
This file licensed under Mozilla Public License v2.0 http://mozilla.org/MPL/2.0/

## Methods
- [`validSourceImageFormats(): array`](method-validsourceimageformats.md) Get formats GD and resize
- [`validTargetImageFormats(): array`](method-validtargetimageformats.md) Get an array of image file extensions this ImageSizerModule can create
- [`getLibraryVersion(): string`](method-getlibraryversion.md) Get library version string
- [`supported(string $action = 'imageformat'): bool`](method-supported.md) Return whether or not GD can proceed - Is the current image(sub)format supported?
- [`processResize(string $srcFilename, string $dstFilename, int $fullWidth, int $fullHeight, int $finalWidth, int $finalHeight): bool`](method-processresize.md) Process the image resize
- [`imSaveReady(resource $im, string $filename): bool`](method-___imsaveready.md) (hookable) Called before saving of image, returns true if save should proceed, false if not
- [`imSaveWebP(resource $im, string $filename, int $quality = 90): boolean`](method-imsavewebp.md) Create WebP image (@horst) Is requested by image options: ["webpAdd" => true] OR ["webpOnly" => true]
- [`imRotate(resource $im, int $degree): resource`](method-imrotate.md) Rotate image (@horst)
- [`imFlip(resource $im, bool $vertical = false): resource`](method-imflip.md) Flip image (@horst)
- [`imSharpen(resource $im, string $mode): resource|bool`](method-imsharpen.md) Sharpen image (@horst)
- [`gammaCorrection(resource &$image, bool $mode)`](method-gammacorrection.md) apply GammaCorrection to an image (@horst)
- [`unsharpMask(resource $img, int $amount, int $radius, int $threshold): resource`](method-unsharpmask.md) Unsharp Mask for PHP - version 2.1.1
- [`calculateUSMfactor(mixed $targetWidth, mixed $targetHeight, mixed $origWidth = null, mixed $origHeight = null): int`](method-calculateusmfactor.md) Calculate USM factor
- [`prepareImageLayer(resource &$im, resource &$image)`](method-prepareimagelayer.md) Prepares a new created GD image resource according to the IMAGETYPE
- [`hasEnoughMemory(string $filename = '', bool $double = true, int|float $factor = 1, string $action = 'action', bool $throwIfNot = false): bool`](method-hasenoughmemory.md) Additional functionality on top of existing checkMemoryForImage function for the flip/rotate actions
- [`processAction(string $srcFilename, string $dstFilename, string $action, int|string $value): bool`](method-processaction.md) Process a rotate or flip action
- [`_processActionFlip(resource &$img, string $flipType): bool|resource`](method-_processactionflip.md) Process flip action (internal)
- [`_processActionRotate(resource &$img, $degrees): bool|resource`](method-_processactionrotate.md) Process rotate action (internal)
- [`processRotate(string $srcFilename, string $dstFilename, int $degrees): bool`](method-processrotate.md) Process rotate of an image
- [`processFlip(string $srcFilename, string $dstFilename, string $flipType): bool`](method-processflip.md) Process vertical or horizontal flip of an image
- [`convertToGreyscale(string $dstFilename = ''): bool`](method-converttogreyscale.md) Convert image to greyscale
- [`convertToSepia(string $dstFilename = '', float|int $sepia = 55): bool`](method-converttosepia.md) Convert image to sepia
