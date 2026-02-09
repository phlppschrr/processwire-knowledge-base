# ProcessWire 3.0.4: Repeaters Revisited + Preview of ProFields Matrix

Source: https://processwire.com/blog/posts/processwire-3.0.4-repeaters-revisited-preview-of-profields-matrix/

## Sections


## Repeaters Revisited + Preview of ProFields Matrix

8 January 2016 by Ryan Cramer [ 29 Comments](/blog/posts/processwire-3.0.4-repeaters-revisited-preview-of-profields-matrix/#comments)


### ProcessWire 3.0.4

This week is all about repeaters, something that we didn't cover on the roadmap last week, and maybe should have. But we always like to save a few surprises so you still have a reason to come and read these blog posts!


## Major upgrades to Repeater fields

This week we have ProcessWire 3.0.4 which brings a major refactoring of the Repeaters Fieldtype/Inputfield to the core. Not to mention several other unrelated tweaks and bug fixes. But we'll focus on the repeaters here. The latest version of Repeaters included with the ProcessWire core adds these new features…


### Summary of changes


### No more need for repeater “ready pages”

Repeaters no longer have to maintain "ready pages", which were one or more pages that it would keep (per your settings) ready-to-edit, hidden in the background. This was undesirable overhead, as it might keep several unused pages for each repeater, on each page. If you had more items to add than you had "ready pages", then you would get a non-editable item labeled with "this item will become editable after you save."

All this was was necessary when repeaters were originally developed because not all core Inputfields could be dynamically inserted into a document, especially those with heavy Javascript components like rich text editors, image fields, and the like. ProcessWire 2.7 largely corrected that, as the core now supports AJAX/dynamic loaded fields in the page editor. That means that Repeaters can now take advantage of it too, and in the latest version, they do. What this means is that the latest repeaters version is significantly more efficient and has a nicer admin UI for the editors.

It's possible there may still be some instance where you've got an Inputfield module that doesn't work well being inserted from Javascript (AJAX). For those cases, a new configuration setting has been added that enables you to disable the AJAX-add mode, reverting back to the "this item will be editable after you save" method. Though our hope is that the instances where you might need that will be rare.


### Screenshots from the latest repeaters version

The following screenshot shows a repeaters field that I setup for managing events. I've configured my repeater to keep the items collapsed by default (requiring a click to open and edit). The collapsed mode makes repeater items easier to keep track of and easier to sort. Note the third item there, which demonstrates an unpublished item–you can now maintain unpublished items in your repeater. To publish or unpublish, you just click the little toggle next to the trash can in the item header.

Next we have the same repeater as above, but with the last item open for editing. Note the "Add New Event" action at the bottom, which is now configurable with the repeater, making it much more context friendly. Previously all repeaters had the same "Add Item" action text.

In this next screenshot below, you'll see the field edit screen for the repeater field shown in the previous two screenshots. If you've used repeaters before, it probably looks pretty familiar, but with several new customization options, and no more field to configure "ready items."


## New ProFields Repeater Matrix Field

One of the items in last week's roadmap was mention of a new ProFields module. Since we're on the topic of repeaters, I thought it made sense to give you a preview of the new Repeater Matrix field. This new field will part of our ProFields package and available for download in our ProFields support board in the near future. If you've already purchased ProFields and have an active ProFields support plan then ProFields Matrix will be free for you to download and use. It fills a gap in the current ProFields modules, providing a new flexible content type that we think you will find useful.

The Repeater Matrix field is a lot like a regular Repeater field, except that it lets you maintain multiple types of repeater items in the same repeater field. So while it may share some similarities with repeaters, it's also an entirely different animal that opens up a whole lot of new flexibility and possibilities for content management. Below are a few screenshots that help to communicate what it does.


### Repeater Matrix details and screenshots

Here's what a Repeater Matrix looks like in your page editor when all the items are collapsed. It looks a lot like a regular repeater field here, but the "Add New" actions at the bottom hint at what's different. The types that you see there are configured with the field, and you can create as many different types as you want. Likewise, in your page editor, you can add any quantity or order of items of varying types that you want.

One use case for a Repeater Matrix is as an alternative to a rich text editor for those cases where you want more fine-grained developer control. For example, you might setup separate headline, body, blockquote, photo and video types, for starters. Because they are all independent fields rather than a big block of HTML, you as the developer have a lot more control over the output.

Below is what the same field looks like with a few of the items open. The "Links" field that you see is actually a ProFields Table field that I added to my Repeater Matrix. Like with regular repeaters, you can maintain unpublished items too–see the last Bodycopy item there as an example. By the way, the labels that you see for each item, like "Blockquote", "Photo gallery", etc., are fully configurable just like with the new repeaters, or they can be auto-generated to reflect just the type (as in these screenshots).

Next we have a screenshot showing you the Field editor (Setup > Fields) where you create and/or configure your Repeater Matrix field. The configuration is very similar to regular repeater fields except that you can add as many different repeater types as you'd like. Something to note is that Repeater Matrix fields are incredibly easy to configure, just as regular repeaters are. You can accomplish some similar things with a PageTable field, but it takes a lot more effort.


### Repeater Matrix from the API

From the API side, your Repeater Matrix is just a PageArray accessed in the same way as any other Page field in ProcessWire, and each of the individual items are just Page objects. Meaning, you likely already know how to use this field from the API side. And you'll likewise already know how to $pages->find() items from it with selectors.

When it comes to outputting values, the main difference is that you'll want to check a type property for each item that you foreach (iterate), since you can have any number of different types in your PageArray value. That type property will indicate what type of item you are dealing with. For instance, the field configured in my screenshots above has types identified by: blockquote, bodycopy, gallery, links and highlights. Depending on the item type, you would use different code to output the values on the front-end. For example:

```
foreach($page->test_matrix as $item) {
  if($item->type == 'blockquote') {
    echo "
      <blockquote>
         <p>$item->quote</p>
         <cite>$item->quote_cite</cite>
      </blockquote>
      ";
  } else if($item->type == 'bodycopy') {
    echo "
      <h2>$item->title</h2>
      $item->body
      ";
  } else if($item->type == 'gallery') {
    // and so on...
  }
}
```

We also have an alternative option available where you can specify PHP files that render the output markup for each type, not unlike baby template files, but we'll cover more on that next time, as it leads into yet another new feature coming to PW3 that we're saving as a surprise. Hope that you all have a great weekend and week ahead and thanks for reading! Remember to read the [ProcessWire Weekly](http://weekly.pw) this Saturday!
