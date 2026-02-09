# ProcessWire 2.5.7 creepy core updates

Source: https://processwire.com/blog/posts/processwire-2.5.7-core-updates/

## Sections


## ProcessWire 2.5.7 creepy core updates

31 October 2014 by Ryan Cramer [ 4 Comments](/blog/posts/processwire-2.5.7-core-updates/#comments)


### AJAX file upload drafts

When you make a change to a field that saves via AJAX, that change is saved by the AJAX request, not by you clicking the Save button. For example, when you drag and drop a file into a PW files field, it immediately sends to the server and saves with the page.

This is the nature of an AJAX save, and could be seen as a compromise or a benefit depending on your goal. But in the case of file/image fields, there seems to be a consensus that most would prefer having the convenience of an AJAX upload without the compromise of an AJAX save. This meant placing files in some temporary storage or draft status. The plan was to make that happen with our published-page drafts system, currently in progress. But as development on that system matures, I've found that it can be implemented in the core more easily than in the drafts system, and provide benefits to both the drafts system and outside of it.

ProcessWire 2.5.7 brings drafts of uploaded files. Now when you upload a file (or files) they still get saved with the page, but they take on a special draft status. That status prevents them from showing up on the front-end of your site before you click "save". If you never happen to click "save" then the files will be removed from the page automatically, after a period of time.

There is an exception to this, and that is when using the new "overwrite" mode available to file fields. If you have that "overwrite" box checked in your file field settings, then the behavior stays the same as before. Though I've not yet heard of anyone actually using the overwrite mode, so have considered removing it. It's one of those things that sounded useful, but hasn't turned out to have as much practical value as I thought. Though if I'm wrong about that please let me know. But overwrite mode and file drafts were going to add more complexity to the system than we wanted to maintain, so they've been left out. However, the new drafts system will largely solve that one, as it keeps its own copy of a page's files when you have a draft open.

One of the benefits of having the files get saved in the page right away was the fact that you could upload photos and then have them available for selection immediately in the CKEditor or TinyMCE image dialog pop-up, before even saving the page. That's a feature I use almost every time I write one of these blog posts, and I know other people likely depend on it too. For example, we're writing something in CKEditor and realize we need a photo or a screenshot in the text, so we upload it and place it in the copy without having to go through a save cycle and page reload. It's a great convenience. So it was a priority to make sure that capability remained, and it drove the approach that was taken here. If you have a chance to try out 2.5.7 (dev branch) please let us know how it works for you.


### Field/template context now available for any field property

Many of you know about the ability change a field's label, description and other predefined properties depending on what template the field happens to be used in. When editing a template (in Setup > Templates) click on the name of any field in your list and a modal dialog pops up enabling you to customize the properties of that field when used with that template.

It's a nice convenience and can help to reduce the quantity of fields necessary to meet your content needs. But thus far, it has been limited to predefined properties: field label, description, visibility, column width, and required state. I've been reluctant to go further than that, because I think there's a fine line between what's useful and what's problematic here. Taken too far, you could easily end up with a confusing mess. Ultimately, the best ones to determine what's useful for field/template context and what's not, are the developers of Fieldtypes and Inputfields. So this week we've added a means by which Fieldtype/Inputfield module developers can tell ProcessWire which of their configuration properties should be made available to field/template context.

When building a Fieldtype or Inputfield module, the developer sets up a method called `getConfigInputfields()` that basically returns a group of form fields (called Inputfields) used to configure the field. Now there is a new optional companion method called `getConfigAllowContext()` that simply returns an array of field names (strings) that are allowed to be used in field/template context. The field names of course refer to the names of fields defined in `getConfigInputfields()`. [Here's an example](https://github.com/ryancramerdesign/ProcessWire/blob/dev/wire/modules/Inputfield/InputfieldText.module#L146) in InputfieldText.module that tells ProcessWire that it can make the initValue, pattern, placeholder and maxlength configuration properties available for customization in field/template context settings.

We've also sparingly updated some other core modules for this capability, with more coming soon (ProFields especially).


### Configurable labels for "Content" and "Children" tabs in page editor

A request came in on GitHub from Netcarver to provide for the option of customizing the "Content" tab label in the page editor. While they were already customizable with language packs, you couldn't change the label on a per-template basis like Netcarver requested. It's actually a great idea, and I can't believe it's not come up before (and wondering why I never thought of it!). This feature has been added. You'll see it in your Template settings on the "Advanced" tab. As a bonus, the label for the "Children" tab is also customizable. Both labels are multi-language of course.


### More scary updates

- The Page Table module now provides a "no close" option for keeping the modal dialog window open rather than closing it when you save. [more](https://github.com/ryancramerdesign/ProcessWire/commit/bc8dfe1b7d26c8d73ecfa9564e94c775df5fec38)
- The System Notifications module now supports both right-aligned and left-aligned notification ghosts. The consensus seems to be that right-aligned works a little better, so we've switched that to be the default. [more](https://github.com/ryancramerdesign/ProcessWire/commit/bc8dfe1b7d26c8d73ecfa9564e94c775df5fec38)
- The System Notifications module now lets you specify a [ghost limit](https://github.com/ryancramerdesign/ProcessWire/commit/bc647b31a242c755af5487960a81616b41b90e21) in the module settings, to prevent your screen being taken over by monsters and ghosts.


### Happy halloween

Hope everyone has a happy and safe Halloween. Now back to pumpkin carving…
