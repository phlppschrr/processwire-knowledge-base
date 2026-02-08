# Front-end editing (PageFrontEdit module)

Source: https://processwire.com/docs/front-end/front-end-editing/

## Summary

Edit pages on the front-end of your site with the core PageFrontEdit module.

## Key Points

- Edit pages on the front-end of your site with the core PageFrontEdit module.
- ProcessWire provides a few different options for you here, which we'll cover in detail below. Regardless of which option you choose, front-end editing will only appear when the user has appropriate permissions to the page and field. Required permissions are page-edit and page-edit-front. When a field is editable, hovering it shows a context mouse pointer rather than a regular pointer. To edit the field on the front-end, you must double click it.
- When the formatted value of the field is retrieved from a $page, it will be editable without you having to write any markup/code for it. This is a good option for fields like a "body" copy or "sidebar" field, that you might only output once on the page. The main benefit here is that you can make the field editable just by checking a box in the admin. It becomes editable wherever and however you are outputting it. It doesn't matter if it's coming from another page or not, as PW keeps track of it.

## Sections


### Requirements


## Enabling front-end editing

ProcessWire provides a few different options for you here, which we'll cover in detail below. Regardless of which option you choose, front-end editing will only appear when the user has appropriate permissions to the page and field. Required permissions are page-edit and page-edit-front. When a field is editable, hovering it shows a context mouse pointer rather than a regular pointer. To edit the field on the front-end, you must double click it.


### Option A: Automatic editing

When the formatted value of the field is retrieved from a $page, it will be editable without you having to write any markup/code for it. This is a good option for fields like a "body" copy or "sidebar" field, that you might only output once on the page. The main benefit here is that you can make the field editable just by checking a box in the admin. It becomes editable wherever and however you are outputting it. It doesn't matter if it's coming from another page or not, as PW keeps track of it.


### Avoid using option A for your "title" field and similar

The drawback is that the field is editable wherever you output it (to a user with permission to edit), so it's not ideal for fields like "title" that might be great in an editable headline, but could be problematic if it also makes appearances in navigation, a <title> tag or in a breadcrumb trail. Though you can do this:


### Option B: API method call

As you probably know, you can pull the value of any field on a page with $page->field_name; or $page->get('field_name'); – If you want to pull an editable version of that field, you can instead use $page->edit('field_name'); for example:


### Option C: HTML edit tags

HTML <edit> tags enable you to create editable regions in your markup. Make the <edit>...</edit> tags wrap any markup that you wish, and double clicking whatever is contained within it will open up an editor to that field. For example, here is how you might make an image field named "photo" editable:


### Option D: HTML edit attributes

These work about the same as <edit> tags except they are an attribute you can add to an existing tag in your markup, such as <div>, <span> or whatever you'd like.


## Configuring front-end editing

All of the front-end editing features are provided by a module included with the ProcessWire 3.0 core called PageFrontEdit. Once this module is installed, you can use any of the above options. The module is not installed by default.
