# HTMLPurifier_Zipper

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

A zipper is a purely-functional data structure which contains
a focus that can be efficiently manipulated.  It is known as
a "one-hole context".  This mutable variant implements a zipper
for a list as a pair of two arrays, laid out as follows:

     Base list: 1 2 3 4 [ ] 6 7 8 9
     Front list: 1 2 3 4
     Back list: 9 8 7 6

User is expected to keep track of the "current element" and properly
fill it back in as necessary.  (ToDo: Maybe it's more user friendly
to implicitly track the current element?)

Nota bene: the current class gets confused if you try to store NULLs
in the list.

## next()

Move hole to the next element.
@param $t Element to fill hole with
@return Original contents of new hole.

## advance()

Iterated hole advancement.
@param $t Element to fill hole with
@param $i How many forward to advance hole
@return Original contents of new hole, i away

## prev()

Move hole to the previous element
@param $t Element to fill hole with
@return Original contents of new hole.

## delete()

Delete contents of current hole, shifting hole to
next element.
@return Original contents of new hole.

## done()

Returns true if we are at the end of the list.
@return bool

## insertBefore()

Insert element before hole.
@param Element to insert

## insertAfter()

Insert element after hole.
@param Element to insert

## splice()

Splice in multiple elements at hole.  Functional specification
in terms of array_splice:

     $arr1 = $arr;
     $old1 = array_splice($arr1, $i, $delete, $replacement);

     list($z, $t) = HTMLPurifier_Zipper::fromArray($arr);
     $t = $z->advance($t, $i);
     list($old2, $t) = $z->splice($t, $delete, $replacement);
     $arr2 = $z->toArray($t);

     assert($old1 === $old2);
     assert($arr1 === $arr2);

NB: the absolute index location after this operation is
*unchanged!*

@param Current contents of hole.
