# CommentStars

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentStars.php`

Class CommentStars

Handles rendering of star ratings for comments.
Additional code in comments.js and comments.css accompanies this.

Copyright 2016 by Ryan Cramer for ProcessWire

## other

@property int $numStars Max number of stars

@property string $star Default star output (can be overridden with HTML)

@property string $starOn Optionally use this star/HTML for ON state

@property string $starOff Optionally use this star/HTML for OFF state

@property string $starClass Class for stars whether on or off

@property string $starOnClass Class for active/on stars

@property string $starOffClass Class for inactive/off stars

@property string $starPartialClass Class for partial (half lit star)

@property string $wrapClass Wrapping element class, required for JS and CSS

@property string $wrapClassInput Wrapping input element class, required for JS and CSS

@property string $countClass Class used for the renderCount() method

@property string $detailsLabel Star details label

@property string $countLabelSingular Single count label

@property string $countLabelPlural Plural count label

@property string $unratedLabel Unrated label

## __construct()

Construct comment stars

## setDefault()

Change one of the defaults (see $defaults)

Example: CommentStars::setDefault('star', '<i class="fa fa-star"></i>');

@param $key

@param $value

## render()

Render stars

If given a float for $stars, it will render partial stars.
If given an int for $stars, it will only render whole stars.

@param int|float|null $stars Number of stars that are in active state

@param bool $allowInput Whether to allow input of stars

@return string

## renderCount()

Render a count of ratings

@param int $count

@param float|int $stars

@param string $schema May be "rdfa" or "microdata" or blank (default) to omit.

@return string
