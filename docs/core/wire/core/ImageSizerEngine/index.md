# ImageSizerEngine

Source: `wire/core/ImageSizerEngine.php`

Inherits: `WireData`
Implements: `Module`, `ConfigurableModule`


Groups:
Group: [other](group-other.md)

ImageSizer Engine Module (Abstract)

Copyright (C) 2016-2019 by Horst Nogajski and Ryan Cramer
This file licensed under Mozilla Public License v2.0 http://mozilla.org/MPL/2.0/

Methods:
- [`prepare(string $filename, array $options = array(), null|array $inspectionResult = null)`](method-prepare.md) Prepare the ImageSizer (this should be the first method you call)
- [`supported(string $action = 'imageformat'): bool`](method-supported.md) Is this ImageSizer class ready only means: does the server / system provide all Requirements!
- [`processResize(string $srcFilename, string $dstFilename, int $fullWidth, int $fullHeight, int $finalWidth, int $finalHeight): bool`](method-processresize.md) Process the image resize
- [`processRotate(string $srcFilename, string $dstFilename, int $degrees): bool`](method-processrotate.md) Process rotate of an image
- [`processFlip(string $srcFilename, string $dstFilename, bool $flipVertical): bool`](method-processflip.md) Process vertical or horizontal flip of an image
- [`validSourceImageFormats(): array`](method-validsourceimageformats.md) Get array of image file extensions this ImageSizerModule can process
- [`validTargetImageFormats(): array`](method-validtargetimageformats.md) Get an array of image file extensions this ImageSizerModule can create
- [`getSupportedFormats(string $type = ''): array`](method-getsupportedformats.md) Get an array of image file formats this ImageSizerModule can use as source or target
- [`getEngineInfo(): array`](method-getengineinfo.md) Get array of information about this engine
- [`loadImageInfo(string $filename, bool $reloadAll = false)`](method-loadimageinfo.md) Load all image information from ImageInspector (Module)
- [`getImageInfo(bool $rawData = false): string|array`](method-getimageinfo.md) ImageInformation from Image Inspector in short form or full RawInfoData
- [`writeBackIPTC(string $filename, bool $includeCustomTags = false): bool|null`](method-writebackiptc.md) Default IPTC Handling
- [`setImageInfo(int $width, int $height)`](method-setimageinfo.md) Save the width and height of the image
- [`getWidth(): int`](method-getwidth.md) Return the image width
- [`getHeight(): int`](method-getheight.md) Return the image height
- [`getProportionalWidth(int $targetHeight): int`](method-getproportionalwidth.md) Given a target height, return the proportional width for this image
- [`getProportionalHeight(int $targetWidth): int`](method-getproportionalheight.md) Given a target width, return the proportional height for this image
- [`getResizeDimensions(int $targetWidth, int $targetHeight): array`](method-getresizedimensions.md) Get an array of the 4 dimensions necessary to perform the resize
- [`isModified(): bool`](method-ismodified.md) Was the image modified?
- [`setCropping(bool|string|array $cropping = true): self`](method-setcropping.md) Turn on/off cropping and/or set cropping direction
- [`setCropExtra(array $value): self`](method-setcropextra.md) Set values for cropExtra rectangle, which enables cropping before resizing
- [`setQuality(int $n): self`](method-setquality.md) Set the image quality 1-100, where 100 is highest quality
- [`setWebpQuality(int $n): self`](method-setwebpquality.md) Set the image quality 1-100 for WebP output, where 100 is highest quality
- [`setWebpAdd(bool $webpAdd, bool|null $webpOnly = null): self`](method-setwebpadd.md) Set flag to also create a webp file or not
- [`setWebpOnly($value): self`](method-setwebponly.md) Set flag to only create a webp file
- [`setSharpening(mixed $value): self`](method-setsharpening.md) Set sharpening value: blank (for none), soft, medium, or strong
- [`setAutoRotation(bool $value = true): self`](method-setautorotation.md) Turn on/off auto rotation
- [`setUpscaling(bool $value = true): self`](method-setupscaling.md) Turn on/off upscaling
- [`setInterlace(bool $value = true): self`](method-setinterlace.md) Turn on/off interlace
- [`setDefaultGamma(float|int $value = 2.2): self`](method-setdefaultgamma.md) Set default gamma value: 0.5 - 4.0 | -1
- [`setTimeLimit(int $value = 30): self`](method-settimelimit.md) Set a time limit for manipulating one image (default is 30)
- [`setScale(float $scale): self`](method-setscale.md) Set scale for hidpi (2.0=hidpi, 1.0=normal, or other value if preferred)
- [`setHidpi(bool $hidpi = true): self`](method-sethidpi.md) Enable hidpi mode?
- [`setRotate($degrees): self`](method-setrotate.md) Set rotation degrees
- [`setFlip($flip): self`](method-setflip.md) Set flip
- [`setUseUSM(bool $value = true): self`](method-setuseusm.md) Toggle on/off the usage of USM algorithm for sharpening
- [`setOptions(array $options): self`](method-setoptions.md) Alternative to the above set* functions where you specify all in an array
- [`getBooleanValue(bool|int|string $value): bool`](method-getbooleanvalue.md) Given a value, convert it to a boolean.
- [`getIntegerValue(int $n, int $min, int $max): int`](method-getintegervalue.md) Get integer value within given range
- [`getOptions(): array`](method-getoptions.md) Return an array of the current options
- [`get(string $key): mixed|null`](method-get.md) Get a property
- [`getFilename(): string`](method-getfilename.md) Return the filename
- [`getExtension(): string`](method-getextension.md) Return the file extension
- [`getImageType(): string|null`](method-getimagetype.md) Return the image type constant
- [`iptcPrepareData(bool $includeCustomTags = false): string`](method-iptcpreparedata.md) Prepare IPTC data (@horst)
- [`iptcMakeTag(string $rec, string $dat, string $val): string`](method-iptcmaketag.md) Make IPTC tag (@horst)
- [`checkOrientation(&$correctionArray): bool`](method-checkorientation.md) Check orientation (@horst)
- [`hasAlphaChannel(): bool`](method-hasalphachannel.md) Check for alphachannel in PNGs
- [`setModified(bool $modified): self`](method-setmodified.md) Set whether the image was modified
- [`getModified(): bool`](method-getmodified.md) Get whether the image was modified
- [`getCropDimensions(int &$w1, int &$h1, int $gdWidth, int $targetWidth, int $gdHeight, int $targetHeight)`](method-getcropdimensions.md) Check if cropping is needed, if yes, populate x- and y-position to params $w1 and $h1
- [`resize(int $finalWidth, int $finalHeight): bool`](method-resize.md) Resize the image
- [`rotate(int $degrees, string $dstFilename = ''): bool`](method-rotate.md) Just rotate image by number of degrees
- [`flipVertical(string $dstFilename = ''): bool`](method-flipvertical.md) Flip vertically
- [`flipHorizontal(string $dstFilename = ''): bool`](method-fliphorizontal.md) Flip horizontally
- [`flipBoth(string $dstFilename = ''): bool`](method-flipboth.md) Flip both vertically and horizontally
- [`convertToGreyscale(string $dstFilename = ''): bool`](method-converttogreyscale.md) Convert image to greyscale
- [`convertToSepia(string $dstFilename = '', float|int $sepia = 55): bool`](method-converttosepia.md) Convert image to sepia
- [`getResizeMethod(mixed &$gdWidth, mixed &$gdHeight, mixed &$targetWidth, mixed &$targetHeight, mixed &$x1, mixed &$y1): int`](method-getresizemethod.md) Get an integer representing the resize method to use
- [`getFocusZoomPosition(string $focus, int $sourceDimension, int $cropDimension, int $zoom): int`](method-getfocuszoomposition.md) Helper function to perform a cropExtra / cropBefore cropping
- [`getFocusZoomCropDimensions(int $zoom, int $fullWidth, int $fullHeight, int $finalWidth, int $finalHeight): array`](method-getfocuszoomcropdimensions.md) Get an array of the 4 dimensions necessary to perform a cropExtra / cropBefore cropping
- [`getFocusZoomPercent(): int`](method-getfocuszoompercent.md) Get current zoom percentage setting or 0 if not set
- [`isAutoload(): bool`](method-isautoload.md) Module info: not-autoload
- [`isSingular(): bool`](method-issingular.md) Module info: not singular
- [`setConfigData(array $data)`](method-setconfigdata.md) Set module config data for ConfigurableModule interface
- [`getConfigData(): array`](method-getconfigdata.md) Get module config data
- [`getLibraryVersion(): string`](method-getlibraryversion.md) Get library version string
- [`getModuleConfigInputfields(InputfieldWrapper $inputfields)`](method-getmoduleconfiginputfields.md) Module configuration
