# ImageSizerEngineGD

Source: `wire/core/ImageSizerEngineGD.php`

ProcessWire ImageSizerGD

Code for IPTC, auto rotation and sharpening by Horst Nogajski.
http://nogajski.de/

Other user contributions as noted.

Copyright (C) 2016-2019 by Horst Nogajski and Ryan Cramer
This file licensed under Mozilla Public License v2.0 http://mozilla.org/MPL/2.0/

https://processwire.com

## other

@method bool imSaveReady($im, $filename)

## validSourceImageFormats()

Get formats GD and resize

@return array

## validTargetImageFormats()

Get an array of image file extensions this ImageSizerModule can create

@return array of uppercase file extensions, i.e. ['PNG', 'JPG']

## getLibraryVersion()

Get library version string

@return string Returns version string or blank string if not applicable/available

@since 3.0.138

## supported()

Return whether or not GD can proceed - Is the current image(sub)format supported?

@param string $action

@return bool

## processResize()

Process the image resize

@param string $srcFilename Source file

@param string $dstFilename Destination file

@param int $fullWidth Current width

@param int $fullHeight Current height

@param int $finalWidth Requested final width

@param int $finalHeight Requested final height

@return bool

@throws WireException

## ___imSaveReady()

Called before saving of image, returns true if save should proceed, false if not

Also Creates a webp file when settings indicate it should.

@param resource $im

@param string $filename Source filename

@return bool

## imSaveWebP()

Create WebP image (@horst)
Is requested by image options: ["webpAdd" => true] OR ["webpOnly" => true]

@param resource $im

@param string $filename

@param int $quality

@return boolean true | false

## imRotate()

Rotate image (@horst)

@param resource $im

@param int $degree

@return resource

## imFlip()

Flip image (@horst)

@param resource $im

@param bool $vertical (default = false)

@return resource

## imSharpen()

Sharpen image (@horst)

@param resource $im

@param string $mode May be: none | soft | medium | strong

@return resource|bool

## gammaCorrection()

apply GammaCorrection to an image (@horst)

with mode = true it linearizes an image to 1
with mode = false it set it back to the originating gamma value

@param resource $image

@param bool $mode

## unsharpMask()

Unsharp Mask for PHP - version 2.1.1

Unsharp mask algorithm by Torstein Hønsi 2003-07.
thoensi_at_netcom_dot_no.
Please leave this notice.

http://vikjavev.no/computing/ump.php

@param resource $img

@param int $amount

@param int $radius

@param int $threshold

@return resource

## calculateUSMfactor()

Calculate USM factor

Return an integer value indicating how much an image should be sharpened
according to resizing scalevalue and absolute target dimensions

@param mixed $targetWidth width of the targetimage

@param mixed $targetHeight height of the targetimage

@param mixed $origWidth

@param mixed $origHeight

@return int

## prepareImageLayer()

Prepares a new created GD image resource according to the IMAGETYPE

Intended for use by the resize() method

@param resource $im, destination resource needs to be prepared

@param resource $image, with GIF we need to read from source resource

## hasEnoughMemory()

Additional functionality on top of existing checkMemoryForImage function for the flip/rotate actions

@param string $filename Filename to check. Default is whatever was set to this ImageSizer.

@param bool $double Need enough for both src and dst files loaded at same time? (default=true)

@param int|float $factor Tweak factor (multiply needed memory by this factor), i.e. 2 for rotate actions. (default=1)

@param string $action Name of action (if something other than "action")

@param bool $throwIfNot Throw WireException if not enough memory? (default=false)

@return bool

@throws WireException

## processAction()

Process a rotate or flip action

@param string $srcFilename

@param string $dstFilename

@param string $action One of 'rotate' or 'flip'

@param int|string $value If rotate, specify int of degrees. If flip, specify one of 'vertical', 'horizontal' or 'both'.

@return bool

@throws WireException

## _processActionFlip()

Process flip action (internal)

@param resource $img

@param string $flipType vertical, horizontal or both

@return bool|resource

## _processActionRotate()

Process rotate action (internal)

@param resource $img

@param $degrees

@return bool|resource

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

@param string $flipType Specify vertical, horizontal, or both

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
