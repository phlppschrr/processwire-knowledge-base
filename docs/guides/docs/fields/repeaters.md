# Repeatable Fields / Matrix Fields

Source: https://processwire.com/docs/fields/repeaters/

## Summary

The repeater fieldtype enables you to create a group of fields and make it repeatable in any quantity on your page. This opens many new possibilities with how you might manage and structure data.

## Key Points

- The repeater fieldtype enables you to create a group of fields and make it repeatable in any quantity on your page. This opens many new possibilities with how you might manage and structure data.
- Repeatable fields are also referred to as matrix fields in some other platforms. We refer to them as repeatable fields or repeaters, but they are all the same thing. Below is a video that demonstratates how to create and use a repeater field. I suggest viewing the video full screen to see the higher resolution version.
- While this is an old video, it still does a good job of demonstrating the basics of repeaters.

## Sections


### When to use repeaters

Repeaters are ideal for managing simple-to-complex groups of information in smaller known or unknown quantities. Things like rate tables, locations, product variations, staff directories, photo galleries with meta data, and so on might be a good fit with repeaters. The sky is the limit.


### When not to use repeaters

Repeaters aren't infinitely scalable in quantity, so avoid repeaters for quantities of items that you think may need to be infinitely scalable. When you edit a repeater field in your page, you edit all items at once. As a result, you probably don't want to use a repeater if you expect hundreds of items, as that may slow your editing experience. It's better to use pages without repeaters when dealing with huge quantities of items.


## How to use repeaters


### How to create a repeatable field

The repeaters fieldtype is not installed by default. To install, login to your ProcessWire admin and click to Modules. Locate the Fieldtype section and click the Install button for the Repeater fieldtype.


### Outputting repeatable fields

The individual items contained in a repeater field are technically pages in ProcessWire. The value of a repeater field is a PageArray. As a result, you may interact with them exactly like you would any other group of pages in ProcessWire. You might iterate through and output the group of items like this (using the fictional buildings repeater, created in the previous section):


### Testing for an empty value

Like with any other PageArray, you can tell how many items there are by using count():


### Finding pages by repeater value (using selectors)

Use selector subfields to locate pages by a value in a repeater field. Subfields are those that are split with a period, like "field.subfield". This is best demonstrated by examples, again continuing with our buildings field, we will locate pages that have a buildings repeater field by properties of the individual buildings within that repeater field:


### Using the API to add or remove repeater items

Unlike other pages in ProcessWire, new repeater items must be created by ProcessWire rather than you. As a result, a helper method is provided called getNew(). You may call getNew() on any repeater field to get a new item. The item that it returns is ready to populate and has already been added to the repeater. Once populated, you simply save the page that the repeater field is on.
