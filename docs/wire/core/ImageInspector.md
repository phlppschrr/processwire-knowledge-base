# ImageInspector

Source: `wire/core/ImageInspector.php`

Image Inspector

Upgrades ImageSizer and ImageSizerEngines with more in depth information of imagefiles and -formats.

Copyright (C) 2016 by Horst Nogajski and Ryan Cramer
This file licensed under Mozilla Public License v2.0 http://mozilla.org/MPL/2.0/

For modules that extend this, use: autoload=false, singular=false.

## __construct()

Construct

@param string $filename

## inspect()

parse Image and return information

@param string $filename the file we want to inspect

@param bool $parseAppmarker (IPTC), default is FALSE

@return null|false|array

## checkOrientation()

Check orientation (@horst)

@param array

@return array

@todo there is already a checkOrientation method in ImageSizerEngine - do we need both?

## loadImageInfoPng()

parse PNG Image and collect information into $this->info

@return bool

## loadImageInfoGif()

parse GIF Image and collect information into $this->info

@return bool

## loadImageInfoJpg()

parse JPEG Image and collect information into $this->info
