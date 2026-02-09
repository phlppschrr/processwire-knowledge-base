# ImageSizerEngineGD

Source: `wire/core/ImageSizerEngineGD.php`

Inherits: `ImageSizerEngine`


Groups:
Group: [other](group-other.md)

ProcessWire ImageSizerGD

Code for IPTC, auto rotation and sharpening by Horst Nogajski.
http://nogajski.de/

Other user contributions as noted.

Copyright (C) 2016-2019 by Horst Nogajski and Ryan Cramer
This file licensed under Mozilla Public License v2.0 http://mozilla.org/MPL/2.0/

Methods:
- [`validSourceImageFormats(): array`](method-validsourceimageformats.md)
- [`validTargetImageFormats(): array`](method-validtargetimageformats.md)
- [`getLibraryVersion(): string`](method-getlibraryversion.md)
- [`supported(string $action = 'imageformat'): bool`](method-supported.md)
- [`processResize(string $srcFilename, string $dstFilename, int $fullWidth, int $fullHeight, int $finalWidth, int $finalHeight): bool`](method-processresize.md)
- [`imSaveReady(resource $im, string $filename): bool`](method-___imsaveready.md) (hookable)
- [`imSaveWebP(resource $im, string $filename, int $quality = 90): boolean`](method-imsavewebp.md)
- [`imRotate(resource $im, int $degree): resource`](method-imrotate.md)
- [`imFlip(resource $im, bool $vertical = false): resource`](method-imflip.md)
- [`imSharpen(resource $im, string $mode): resource|bool`](method-imsharpen.md)
- [`gammaCorrection(resource &$image, bool $mode)`](method-gammacorrection.md)
- [`unsharpMask(resource $img, int $amount, int $radius, int $threshold): resource`](method-unsharpmask.md)
- [`calculateUSMfactor(mixed $targetWidth, mixed $targetHeight, mixed $origWidth = null, mixed $origHeight = null): int`](method-calculateusmfactor.md)
- [`prepareImageLayer(resource &$im, resource &$image)`](method-prepareimagelayer.md)
- [`hasEnoughMemory(string $filename = '', bool $double = true, int|float $factor = 1, string $action = 'action', bool $throwIfNot = false): bool`](method-hasenoughmemory.md)
- [`processAction(string $srcFilename, string $dstFilename, string $action, int|string $value): bool`](method-processaction.md)
- [`_processActionFlip(resource &$img, string $flipType): bool|resource`](method-_processactionflip.md)
- [`_processActionRotate(resource &$img, $degrees): bool|resource`](method-_processactionrotate.md)
- [`processRotate(string $srcFilename, string $dstFilename, int $degrees): bool`](method-processrotate.md)
- [`processFlip(string $srcFilename, string $dstFilename, string $flipType): bool`](method-processflip.md)
- [`convertToGreyscale(string $dstFilename = ''): bool`](method-converttogreyscale.md)
- [`convertToSepia(string $dstFilename = '', float|int $sepia = 55): bool`](method-converttosepia.md)
