# ImageSizer

Source: `wire/core/ImageSizer.php`

ProcessWire ImageSizer with Engines for ProcessWire 3.x

ImageSizer handles resizing of a single JPG, GIF, or PNG image using GD2
or another supported and configured engine. (Imagick, ImageMagick, Netpbm)

Code for IPTC, auto rotation and sharpening by Horst Nogajski.
http://nogajski.de/

Other user contributions as noted.

Copyright (C) 2016-2019 by Horst Nogajski and Ryan Cramer
This file licensed under Mozilla Public License v2.0 http://mozilla.org/MPL/2.0/

## other

@method bool resize($targetWidth, $targetHeight = 0)

## __construct()

Construct the ImageSizer for a single image

@param string $filename Filename to resize. Omit only if instantiating class for a getEngines() call.

@param array $options Initial options to the engine.

## getEngines()

Get array of all available ImageSizer engine names in order of priority

Note that the returned value excludes the default engine (ImageSizerEngineGD).

@param bool $forceReload Specify true only if you want to prevent it from using cached result from previous call.

@return array of module names

## getEngineInfo()

Get array of information for all ImageSizer engines (or optionally a specific ImageSizer engine)

Returns array of arrays indexed by engine name, each with the following:

 - `name` (string): engine name
 - `title` (string): engine title
 - `class` (string): PHP class name for engine
 - `summary` (string): Single sentence summary of the engine
 - `author` (string): Authr name (if available)
 - `moduleVersion` (string): Version of the module that powers this engine
 - `libraryVersion` (string): Version of the library that powers this engine
 - `sources` (array): Supported formats for source images it reads (i.e. JPG, JPEG, PNG, PNG24, GIF, GIF87, etc.)
 - `targets` (array): Supported formats for target images it creates (i.e. JPG, PNG, PNG24, WEBP, etc.)
 - `quality` (int): Current quality setting configured with the engine
 - `sharpening` (string): Current sharpening setting configured with the engine
 - `priority` (int): Engine priority (lower is higher priority)
 - `runOrder` (int): Order ImageSizer will try this engine in relative to others (lower runs first), derived from priority.

@param string $name Specify engine name to get info just for that engine or omit to get info for all engines (default)

@return array Array of arrays indexed by engine name, or if $name specified then just array of info for that engine.
  Returns empty array on error.

@since 3.0.138

## newImageSizerEngine()

Instantiate an ImageSizerEngine

@param string $filename

@param array $options

@param null|array $inspectionResult

@return ImageSizerEngine|null

@throws WireException

## newDefaultImageSizerEngine()

Get the default/fallback ImageSizer engine

@param string $filename

@param array $options

@param null|array $inspectionResult

@return ImageSizerEngine|null

@throws WireException

## ___resize()

Resize the image proportionally to the given width/height

@param int $targetWidth Target width in pixels, or 0 for proportional to height

@param int $targetHeight Target height in pixels, or 0 for proportional to width. Optional-if not specified, 0
    is assumed.

@return bool True if the resize was successful, false if not

@throws WireException when not enough memory to load image or missing required data

## resizeFallback()

GD is the fallback ImageEngine, it gets invoked if there is no other Engine defined,

or if a defined Engine is not available,
or if an invoked Engine failes with the image manipulation.

@param mixed $targetWidth

@param mixed $targetHeight

@return bool

## setFilename()

Set the filename

@param $filename

@return $this

## setForceEngine()

Force the use of a specific engine

@param $engineName Module name of engine you want to force

@return $this

## setOptions()

Set multiple resize options

@param array $options

@return $this

## setModified()

Set whether a modification was made

@param $modified

@return $this

## getEngine()

Get the current ImageSizerEngine

@param string $engineName Optionally specify a specific engine name to get a new instance of that engine
  When used, returned engine is in an unprepared state (no filename assigned, etc.). Since 3.0.138.

@return ImageSizerEngine|null Returns ImageSizerEngine or null only if requested $engineName is not found.
  If no $engineName is specified this method may return an existing instance from a previous call.

@throws WireException

## getImageInfo()

ImageInformation from Image Inspector in short form or full RawInfoData

@param bool $rawData

@return string|array

## rotate()

Rotate image by given degrees

@param int $degrees

@return bool

## flipVertical()

Flip image vertically

@return bool

## flipHorizontal()

Flip image horizontally

@return bool

## flipBoth()

Flip both vertically and horizontally

@return bool

## convertToGreyscale()

Convert image to greyscale (black and white)

@return bool

## convertToSepia()

Convert image to sepia tone

@param int $sepia Sepia amount

@return bool
