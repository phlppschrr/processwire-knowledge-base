# ProcessWire 3.0.37 and ProFields Text Blocks

Source: https://processwire.com/blog/posts/text-blocks/

## Sections


## ProcessWire 3.0.37 and ProFields Text Blocks

14 October 2016 by Ryan Cramer [ 5 Comments](/blog/posts/text-blocks/#comments)


### ProcessWire 3.0.37

Like last week, updates to the core continued this week with commits primarily related to covering issue reports and pull requests. For a full list of core updates this week see our [commit log](https://github.com/processwire/processwire/commits/dev). The 3.0.37 version will remain on our [dev branch](https://github.com/processwire/processwire/tree/dev) for another week before we merge to master and tag it. So far we're really pleased with how the 3.x release has gone, as everything has been smooth and no reports of any significant problems thus far. Because we don't have anything major to write about in terms of the core, we'll tell you about a small new addition to ProFields this week.


## ProFields Text Blocks

Last week we mentioned there is a new ProFields Fieldtype/Inputfield module in the works. **This isn't that one**–we'll tell you more about that one later. Rather, this is something a little different. Text Blocks is a Textformatter module that fits right in with the intentions of ProFields (“do more with fewer fields”). Some might find it really useful, while others might have no use for it. But because I've found it pretty useful lately, I thought it would be good to go ahead and add it to ProFields set of modules and talk a little about it here.


### About Text Blocks

This module enables you to assign a name to any block/region of text in a Textarea field. They are defined by typing `start_name` where you want the block to start, and `stop_name` where you want the block to stop. The block(s) of text can then be shown in any other Textarea field at runtime (site-wide) simply by typing the block name on its own line in the format `show_name`. Blocks can also be retrieved from the API.

Text Blocks can be defined within and pulled from regular Textarea fields, CKEditor fields, and multi-language Textarea fields. A Textarea field can have any number of text blocks within it.

*By the way, you can change the terms that start, stop and show blocks – this is part of the module configuration. For instance, perhaps you prefer the terms "begin", "end" and "reveal" or something like that – you can choose.*

Like most of the ProFields modules, this module helps you to reduce the number of fields necessary to accommodate various content management needs. It also helps to reduce content redundancy. Unlike regular content fields in ProcessWire, blocks are globally unique and don't really have anything to do with specific pages or the tree hierarchy. In this sense, they are like global variables for Textarea fields.

Regular fields in ProcessWire require superuser access to create and define. Whereas Text Blocks can be created and used by any user with page edit access. As a result, they can be a handy tool for content editors that want to reduce the number of places they have to manage a particular block of repeated text.

Text blocks can be defined and shown from different fields in ProcessWire. The only requirement is that both fields have "Text Blocks" selected in the "Text formatters" section of the field editor.


### Example 1: Reusing a postal address

Lets say that you are editing a contact page that contains a mailing address somewhere in the body copy (textarea) field. You can define that postal address as a block named "address", making it available to anywhere else in the site. For instance, you might repeat that mailing address on the "About Us" page (and perhaps others). Rather than re-typing the whole address in each of those locations, you can just type `show_address`. Because it is pulled at runtime, any changes to the mailing address on the contact page also update anywhere else the address might appear.

On the /contact/ page:

Please send any correspondence to our mailing address is below:

**start_address**

FooBar Widgets 204 Clairemont Avenue Atlanta, GA 30338

**stop_address**

Then on the /about/ page (or anywhere else):

Visit us at:

**show_address**

Why not just use a regular ProcessWire field to hold this address? You certainly could, but then you might be creating a single-use field that appears only on 1 page (the /contact/ page), and only ever have one entry in the database. It's not ideal to maintain an entire field for a single use case. Whereas using a text block may be more appropriate.

Another thing to consider is that using text blocks requires no web development. Meaning, text blocks are a handy tool not just for you, but content editors and clients too.


### Example 2: Reusing a requirements list

Let's say that we maintain a list of requirements for a piece of software. By necessity, it might appear on a few different pages in the site. Every time the list changes, we'd have to update all the pages where it appears. With Text Blocks, we could just define it on one page and then show it on any others:

**start_requirements**

• Foo v123 or newer • Bar v456 or newer • Baz v789 or newer

**stop_requirements**

Anytime we want to show it, we could just type: `show_requirements` wherever we want it to appear, anywhere in the site.


### Other use cases

The examples above are just basic use cases, but the reality is that anything you can think to re-use in multiple places on a site are potential use cases for Text Blocks. Examples include:

- Shared photo(s) or photo galleries
- Action buttons that use specific markup (like PayPal Buy Now or Donate buttons)
- Shared contact information or directions
- Definition of intro or summary copy
- Common disclaimers or terms


### Comment blocks

Another thing that the Text Blocks module can do is enable you to have comment blocks in your textarea fields. The comment blocks appear in the back-end when editing, but are automatically removed from the front-end when the content is viewed. For example, lets say you entered this in the page editor:

This text is visible on the front-end.

<-- This comment and text are automatically removed on the front-end. -->

As the text above indicates, only the first sentence will remain in the markup that is output on the front-end. *Side note:* use the HTML comment format instead–our open comment tag is lacking the "!" only because our example above would be commented out and thus disappear! :)

Note that this works whether in a regular Textarea field or a TinyMCE/CKEditor (rich text) field. You do NOT have to be in the "source" dialog box in TinyMCE/CKEditor to do this because Text Blocks recognizes comment tags whether they are entity encoded or not.

You may define also Text Blocks within comments. This is useful if you want to define text blocks but not have them appear in the page's textarea content on the front-end.


### What happens if there is more than one definition for a text block?

Mentioned earlier was that text blocks are like global variables for textarea fields. There can only be one definition per block name, site-wide. This removes any ambiguity about what you are referring to when you show a block.

If you try to define a text block using the same name as one that is already defined, it won't accept it. Instead, it will convert it to what we call a multi-value block. Multi-value blocks do not collide with single value blocks, even if they have the same name. Read on for more about multi-value blocks…


### Multi-value/multi-page text blocks

Multi-value text blocks concatenate all definitions of the block. Meaning, the block can be defined as many times as you want, and when shown, it will be merged with all of the other definitions. Multi-value blocks are defined and shown the same way as regular text blocks, except with two underscores rather than one, i.e `start__name`, `stop__name`, and `show__name`.

An example of where you might utilize a multi-value block is in keeping track of a to-do list for content edits across many pages in a site. Then you could have another page that has a `show__todo` that shows the compiled list of them. If you didn't want these to-do's to appear on the actual page content where they are defined, you would just surround them in a comment block:

<-- **start__todo** • Rewrite the features section • Ask Karen to proofread the highlights page • Find new photos for the widgets section **stop__todo** -->

On the page where you want to show the to-do lists, you'd type this:

**show__todo**

Note that the opening comment tag above lacks the "!" that you'd usually have in an HTML comment, only so that our example doesn't get "commented out" of this post.


### Text block template files

Text blocks can optionally be populated or manipulated from a custom template file. This custom template file can generate the entirety of the text block, or–if the block has already been defined elsewhere–it will receive a copy of the existing definition, should it want to use that.

To use a text block template file, create the directory /site/templates/text-blocks/ and place a php file in there having the same name as the text block you want to use, i.e. /site/templates/text-blocks/hello.php for a text block named "hello".

Edit that hello.php file and place the text "Hello World" in it. In the ProcessWire admin, go and edit a page and type `show_hello` on its own line somewhere in a textarea field. View the page, and you should see the "Hello World" text from your hello.php file.

Lets say that the "hello" block had already been defined. The block template file will receive that in a variable called `$value`. It can optionally output that value too. For example, here's our updated hello.php file:

```php
<?php
echo "<h2>Hello World</h2>";
echo $value;
```


### API usage

While you can `show_name` any text block where you want it to appear, there may be instances where you would instead like to pull text blocks from the API side. To do that, use the `getBlock()` function:

```
$b = $modules->get('TextformatterTextBlocks');
$address = $b->getBlock('address');
echo "<h2>Mailing address</h2>" . $address;
```

If you want to retrieve a multi-value text block, use the `getMultiBlock()` function instead:

```
$todo = $b->getMultiBlock('todo'); // get as string
$todo = $b->getMultiBlock('todo', true); // get as array
```


### Download Text Blocks

Text Blocks module is available for download to registered ProFields users in the [ProFields board download area](/talk/topic/6413-profields-download/) (requires login). It is designed for ProcessWire 3.x.

Hope that everyone has a great weekend, and as always enjoy reading the fantastic [ProcessWire Weekly](https://weekly.pw) this weekend.
