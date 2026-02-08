# ImageSizerEngine

Source: `wire/core/ImageSizerEngine.php`

ImageSizer Engine Module (Abstract)

Copyright (C) 2016-2019 by Horst Nogajski and Ryan Cramer
This file licensed under Mozilla Public License v2.0 http://mozilla.org/MPL/2.0/

## other

@property bool $autoRotation

@property bool $upscaling

@property bool $interlace

@property array|string|bool $cropping

@property int $quality

@property string $sharpening

@property float $defaultGamma

@property float $scale

@property int $rotate

@property string $flip

@property bool $useUSM

@property int $enginePriority Priority for use among other ImageSizerEngine modules (0=disabled, 1=first, 2=second, 3=and so on)

@property bool $webpAdd

@property int $webpQuality

@property bool|null $webpResult

@property bool|null $webpOnly

## __construct()

**************************************************************************************************

## prepare()

Prepare the ImageSizer (this should be the first method you call)

This is used as a replacement for __construct() since modules can't have required arguments
to their constructor.

@param string $filename

@param array $options

@param null|array $inspectionResult

## supported()

**********************************************************************************************
ABSTRACT AND TEMPLATE METHODS

## supported()

Is this ImageSizer class ready only means: does the server / system provide all Requirements!

@param string $action Optional type of action supported.

@return bool

## processResize()

Process the image resize

Processing is as follows:
   1. first do a check if the given image(type) can be processed, if not do an early return false
   2. than (try) to process all required steps, if one failes, return false
   3. if all is successful, finally return true

@param string $srcFilename Source file

@param string $dstFilename Destination file

@param int $fullWidth Current width

@param int $fullHeight Current height

@param int $finalWidth Requested final width

@param int $finalHeight Requested final height

@return bool True if successful, false if not

@throws WireException

## processRotate()

Process rotate of an image

@param string $srcFilename

@param string $dstFilename

@param int $degrees Clockwise degrees, i.e. 90, 180, 270, -90, -180, -270

@return bool

## processFlip()

Process vertical or horizontal flip of an image

@param string $srcFilename

@param string $dstFilename

@param bool $flipVertical True if flip is vertical, false if flip is horizontal

@return bool

## validSourceImageFormats()

Get array of image file extensions this ImageSizerModule can process

@return array of uppercase file extensions, i.e. ['PNG', 'JPG']

## validTargetImageFormats()

Get an array of image file extensions this ImageSizerModule can create

@return array of uppercase file extensions, i.e. ['PNG', 'JPG']

## getSupportedFormats()

Get an array of image file formats this ImageSizerModule can use as source or target

Unless using the $type argument, returned array contains 'source' and 'target' indexes,
each an array of image file types/extensions in uppercase.

@param string $type Specify 'source' or 'target' to get just those formats, or omit to get all.

@return array

@since 3.0.138

## getEngineInfo()

Get array of information about this engine

@return array

@since 3.0.138

## loadImageInfo()

**********************************************************************************************
COMMON IMPLEMENTATION METHODS

## loadImageInfo()

Load all image information from ImageInspector (Module)

@param string $filename

@param bool $reloadAll

@throws WireException

## getImageInfo()

ImageInformation from Image Inspector
in short form or full RawInfoData

@param bool $rawData

@return string|array

@todo this appears to be a duplicate of what's in ImageSizer class?

## writeBackIPTC()

Default IPTC Handling

If we've retrieved IPTC-Metadata from sourcefile, we write it into the variation here but we omit
custom tags for internal use (@horst)

@param string $filename the file we want write the IPTC data to

@param bool $includeCustomTags default is FALSE

@return bool|null

## setImageInfo()

Save the width and height of the image

@param int $width

@param int $height

## getWidth()

Return the image width

@return int

## getHeight()

Return the image height

@return int

## getProportionalWidth()

Given a target height, return the proportional width for this image

@param int $targetHeight

@return int

## getProportionalHeight()

Given a target width, return the proportional height for this image

@param int $targetWidth

@return int

## getResizeDimensions()

Get an array of the 4 dimensions necessary to perform the resize

Note: Some code used in this method is adapted from code found in comments at php.net for the GD functions

Intended for use by the resize() method

@param int $targetWidth

@param int $targetHeight

@return array

## isModified()

Was the image modified?

@return bool

## setCropping()

Turn on/off cropping and/or set cropping direction

@param bool|string|array $cropping Specify one of: northwest, north, northeast, west, center, east, southwest,
    south, southeast. Or a string of: 50%,50% (x and y percentages to crop from) Or an array('50%', '50%') Or to
    disable cropping, specify boolean false. To enable cropping with default (center), you may also specify
    boolean true.

@return self

## setCropExtra()

Set values for cropExtra rectangle, which enables cropping before resizing

Added by @horst

@param array $value containing 4 params (x y w h) indexed or associative

@return self

@throws WireException when given invalid value

## setQuality()

Set the image quality 1-100, where 100 is highest quality

@param int $n

@return self

## setWebpQuality()

Set the image quality 1-100 for WebP output, where 100 is highest quality

@param int $n

@return self

## setWebpAdd()

Set flag to also create a webp file or not

@param bool $webpAdd

@param bool|null $webpOnly

@return self

## setWebpOnly()

Set flag to only create a webp file

@param bool value$

@return self

## setSharpening()

Set sharpening value: blank (for none), soft, medium, or strong

@param mixed $value

@return self

@throws WireException

## setAutoRotation()

Turn on/off auto rotation

@param bool $value Whether to auto-rotate or not (default = true)

@return self

## setUpscaling()

Turn on/off upscaling

@param bool $value Whether to upscale or not (default = true)

@return self

## setInterlace()

Turn on/off interlace

@param bool $value Whether to upscale or not (default = true)

@return self

## setDefaultGamma()

Set default gamma value: 0.5 - 4.0 | -1

@param float|int $value 0.5 to 4.0 or -1 to disable

@return self

@throws WireException when given invalid value

## setTimeLimit()

Set a time limit for manipulating one image (default is 30)

If specified time limit is less than PHP's max_execution_time, then PHP's setting will be used instead.

@param int $value 10 to 60 recommended, default is 30

@return self

## setScale()

Set scale for hidpi (2.0=hidpi, 1.0=normal, or other value if preferred)

@param float $scale

@return self

## setHidpi()

Enable hidpi mode?

Just a shortcut for calling $this->scale()

@param bool $hidpi True or false (default=true)

@return self

## setRotate()

Set rotation degrees

Specify one of: -270, -180, -90, 90, 180, 270

@param $degrees

@return self

## setFlip()

Set flip

Specify one of: 'vertical' or 'horizontal', also accepts
shorter versions like, 'vert', 'horiz', 'v', 'h', etc.

@param $flip

@return self

## setUseUSM()

Toggle on/off the usage of USM algorithm for sharpening

@param bool $value Whether to USM is used or not (default = true)

@return self

## setOptions()

Alternative to the above set* functions where you specify all in an array

@param array $options May contain the following (show with default values):
   'quality' => 90,
   'webpQuality' => 90,
   'cropping' => true,
   'upscaling' => true,
   'autoRotation' => true,
   'sharpening' => 'soft' (none|soft|medium|string)
   'scale' => 1.0 (use 2.0 for hidpi or 1.0 for normal-default)
   'hidpi' => false, (alternative to scale, specify true to enable hidpi)
   'rotate' => 0 (90, 180, 270 or negative versions of those)
   'flip' => '', (vertical|horizontal)

@return self

## getBooleanValue()

Given a value, convert it to a boolean.

Value can be string representations like: 0, 1 off, on, yes, no, y, n, false, true.

@param bool|int|string $value

@return bool

## getIntegerValue()

Get integer value within given range

@param int $n Number to require in given range

@param int $min Minimum allowed number

@param int $max Maximum allowed number

@return int

## getOptions()

Return an array of the current options

@return array

## get()

Get a property

@param string $key

@return mixed|null

## getFilename()

Return the filename

@return string

## getExtension()

Return the file extension

@return string

## getImageType()

Return the image type constant

@return string|null

## iptcPrepareData()

Prepare IPTC data (@horst)

@param bool $includeCustomTags (default=false)

@return string $iptcNew

## iptcMakeTag()

Make IPTC tag (@horst)

@param string $rec

@param string $dat

@param string $val

@return string

## checkOrientation()

Check orientation (@horst)

@param array

@return bool

## hasAlphaChannel()

Check for alphachannel in PNGs

@return bool

## setModified()

Set whether the image was modified

Public so that other modules/hooks can adjust this property if needed.
Not for general API use

@param bool $modified

@return self

## getModified()

Get whether the image was modified

@return bool

## getCropDimensions()

Check if cropping is needed, if yes, populate x- and y-position to params $w1 and $h1

Intended for use by the resize() method

@param int $w1 - byReference

@param int $h1 - byReference

@param int $gdWidth

@param int $targetWidth

@param int $gdHeight

@param int $targetHeight

## resize()

*********************************************************************************************

## resize()

Resize the image

The resize method does all pre and post-processing for the engines + calls the engine's
processResize() method.

Pre-processing is:
  Calculate and set dimensions, create a tempfile.

Post-processing is:
  Copy back and delete tempfile, write IPTC if necessary, reload imageinfo, set the modified flag.

@param int $finalWidth

@param int $finalHeight

@return bool

## rotate()

Just rotate image by number of degrees

@param int $degrees

@param string $dstFilename Optional destination filename. If not present, source will be overwritten.

@return bool True on success, false on fail

## flipVertical()

Flip vertically

@param string $dstFilename

@return bool

## flipHorizontal()

Flip horizontally

@param string $dstFilename

@return bool

## flipBoth()

Flip both vertically and horizontally

@param string $dstFilename

@return bool

## convertToGreyscale()

Convert image to greyscale

@param string $dstFilename If different from source file

@return bool

## convertToSepia()

Convert image to sepia

@param string $dstFilename If different from source file

@param float|int $sepia Sepia value

@return bool

## getResizeMethod()

Get an integer representing the resize method to use

This method calculates all dimensions at first. It is called before any of the main image operations,
but after rotation and crop_before_resize. As result it returns an integer [0|2|4] that indicates which
steps should be processed:

0 = this is the case if the original size is requested or a greater size but upscaling is set to false
2 = only resize with aspect ratio
4 = resize and crop with aspect ratio

@param mixed $gdWidth

@param mixed $gdHeight

@param mixed $targetWidth

@param mixed $targetHeight

@param mixed $x1

@param mixed $y1

@return int 0|2|4

## getFocusZoomPosition()

Helper function to perform a cropExtra / cropBefore cropping

Intended for use by the getFocusZoomCropDimensions() method

@param string $focus (focus point in percent, like: 54.7%)

@param int $sourceDimension (source image width or height)

@param int $cropDimension (target crop-image width or height)

@param int $zoom

@return int $position (crop position x or y in pixel)

## getFocusZoomCropDimensions()

Get an array of the 4 dimensions necessary to perform a cropExtra / cropBefore cropping

Intended for use by the resize() method

@param int $zoom

@param int $fullWidth

@param int $fullHeight

@param int $finalWidth

@param int $finalHeight

@return array

## getFocusZoomPercent()

Get current zoom percentage setting or 0 if not set

Value is determined from the $this->cropping array index 2 and is used only if index 0 and
index 1 are percentages (and indicated as such with a percent sign).

@return int

## isAutoload()

Module info: not-autoload

@return bool

## isSingular()

Module info: not singular

@return bool

## setConfigData()

Set module config data for ConfigurableModule interface

@param array $data

## getConfigData()

Get module config data

@return array

## getLibraryVersion()

Get library version string

@return string Returns version string or blank string if not applicable/available

@since 3.0.138

## getModuleConfigInputfields()

Module configuration

@param InputfieldWrapper $inputfields
