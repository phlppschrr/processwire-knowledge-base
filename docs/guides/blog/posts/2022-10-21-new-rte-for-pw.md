# New rich text editor for ProcessWire

Source: https://processwire.com/blog/posts/new-rte-for-pw/

## Sections


## New rich text editor for ProcessWire

21 October 2022 by Ryan Cramer [ 6 Comments](/blog/posts/new-rte-for-pw/#comments)

This week we take a look at a new rich text editor for ProcessWire, why we chose it, some highlights, screenshots, and why we think you’ll like it.

As mentioned in previous posts, CKEditor 4 has an end-of-life scheduled for 2023. Soon we've got to use something else for the core rich text editor. The obvious editor to migrate to would be CKEditor 5. But in [last week's post](/blog/posts/reconsidering-the-ckeditor-5-upgrade/) we talked about why that's not ideal. And at the end of that post I mentioned that I found an editor that really is an ideal next step and upgrade.


### Some things we’ve been looking for in a rich text editor

At least when it comes to the clients I work with, the rich text editor is a really important part of the editing experience in ProcessWire, so it's a decision that I take seriously and spent a lot of time with. Here are some of the things I was looking for:

Those are some of the biggest things I was looking for, or that I thought we were looking for. Luckily I found something that meets all of these needs really nicely, but I've been reluctant to reveal what it is until I could *show* you rather than just *tell* you.


### Timeless tools and a decade of evolution

It may be kind of a controversial editor choice in that it appears like a step backward, while actually being a step forward. It's an editor that has in fact been around longer than ProcessWire, and was even in the first version of ProcessWire. Perhaps it is even the most well known RTE in existence?

Does that make it obvious [what it is](https://www.tiny.cloud/)? It's returning to our roots in a way, but the TinyMCE of today (version 6.2.0) is a completely different animal than the version 3.x that last appeared in ProcessWire. And yet, it's that same editor we started with, but with a decade of evolution. It has evolved in the same way ProcessWire has.

It's not an editor that was thrown out and then replaced by another different editor under the same name (looking at you CKEditor). Some people value the kind of change that CKEditor has taken (out with the old, in with the new). But I place more value on the kind of evolutionary change that TinyMCE has adopted. To me it says a lot about how they got it right the first time around. I'm always on the hunt for timeless tools, and TinyMCE appears to be one of them.


### An easy upgrade

I've been using InputfieldTinyMCE in ProcessWire for 2 weeks now (this post is written in it) and TinyMCE 6 feels like a big upgrade from CKEditor 4. Yet it's also a direct replacement for CKEditor 4 because CKEditor and TinyMCE have been 2 leading RTE's for a very long time. They've followed a similar path, and in many ways duplicated features and capabilities to remain competitive with one another (think Honda and Toyota). It seems like CKEditor 5 marks the point at which they started to go in a different direction. TinyMCE has continued moving forward, evolving on the same path, while CKEditor 5 started off on a different path. In any case TinyMCE 6 is a nice upgrade from CKEditor 4, and when it comes to the ProcessWire context, I think a better upgrade than CKEditor 5.


### A closer look

In the last post I mentioned you'd be able to start using the new rich text editor this month. I stand by that and it'll be available to install by or before this time next week. I've got it working quite nicely now though am going to give it a few more days before releasing it, just to make sure I've fixed any obvious bugs before asking others to test it. After all, I've spent a lot of time testing it and coding for it, but not yet a lot of time using it in real life editing situations, so that's what I'll be doing this week.


### Module configuration

When you first install InputfieldTinyMCE, you can choose what UI style and Content style you'd like to start with. Yes there's a dark mode! We'll have a look at these different styles a a bit later.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_15_17_pm.png)


### Field configuration

Here's the field configuration screen. It's more than I can fit in one screenshot so it's split into a few.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_18_12_pm.png)


### Toolbar configuration

The toolbar configuration lets you select which tools you want to use (via InputfieldTextTags) and lets you drag to order them. Following that is a list of all the tools available for the toolbar. Hovering them provides a short description while clicking them takes you to TinyMCE’s full documentation on the tool.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_18_49_pm.png)


### Plugin selection

Editor plugins are selectable from checkboxes:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_20_40_pm.png)

That's a big screenshot! Here's the rest:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_21_07_pm.png)


### Other settings

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_21_51_pm.png)


### Editor with menubar and toolbar

Here's a screenshot of the Regular editor using the default Oxide UI skin and with both menubar and toolbar enabled.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_40_53_pm.png)


### Menubar drop downs

The optional menubar provides drop-downs that give you access to all features added by your selected plugins.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_41_27_pm.png)


### Styles dropdown

The Styles dropdown, which is an optional part of the toolbar:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_42_13_pm.png)


### Image and link dialogs

The Image and Link tools work exactly the same as they do in CKEditor (since both features are mostly powered by the ProcessWire admin rather than the editor):

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_4_01_51_pm.png)


### Table tool

For those that need it, TinyMCE also comes with a really nice Table tool:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_42_57_pm.png)


### Bulleted-list and numbered-list tools

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_43_29_pm.png)


### Editor with toolbar only (no menubar)

The above screenshots show both the menubar and the toolbar, but either (or both) are optional. Here's what it looks like with just the toolbar, which is more what you may be used to from CKEditor:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_44_40_pm.png)


### Editor with menubar only (no toolbar)

You can also go with just the menubar (and no toolbar):

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_45_37_pm.png)


### Distraction free mode

If you want, you can also configure it completely naked with no menubar or toolbar! This is what's called the [distraction free editing mode](https://www.tiny.cloud/docs/tinymce/6/distraction-free-demo/) where the RTE features are all in context menus and only revealed when applicable.


### Drag-drop image uploading and resizing

You can drag and drop images directly into the editor and it'll take care of uploading them to an Images field on the page automatically, just like in CKEditor. But unlike CKEditor, you can drag to resize the images directly in the editor and new image size variations will be created automatically from the source file. Granted, it's mostly ProcessWire doing this rather than TinyMCE (or CKEditor) but TinyMCE provides the API that makes it possible to connect it with ProcessWire in ways that make it all seamless.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_48_59_pm.png)


### Oxide-dark UI

Here's what it looks like with the Oxide-dark UI skin (selected from the module settings):

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_50_53_pm.png)

And here's what it looks like if we also add in the Wire-dark content style (also selected in the module settings);

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_51_41_pm.png)


### Document content style

Also available is the Document content style, which makes your editor look like you are editing a document in a word processor:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_52_25_pm.png)


### Five UI

This is an alternative to the default Oxide UI:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_53_16_pm.png)

Five also comes with its own dark mode as well:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_53_51_pm.png)


### Inline editing mode

The inline editor behaves pretty much exactly like the CKEditor version you are already used to. Here's the TinyMCE version at the bottom of this screenshot:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_55_59_pm.png)

The inline editor after we click in it (using the Oxide-dark skin):

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_2_56_41_pm.png)


### Multi-language

If you are using ProcessWire in some language other than English you'll be glad to know that InputfieldTinyMCE comes ready-to-use with translations for 60 different languages. And it should pick up the correct language automatically (if it doesn't, you can map language packs to languages in the module settings).

[](//d1juguve2xwkcy.cloudfront.net/assets/files/3100/screen_shot_2022-10-21_at_3_35_18_pm.png)
