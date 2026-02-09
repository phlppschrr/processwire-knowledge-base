# Extra action in your Page List (core updates 2.6.5)

Source: https://processwire.com/blog/posts/extra-action-in-your-page-list-processwire-core-updates-2.6.5/

## Sections


## Extra action in your Page List

19 June 2015 by Ryan Cramer [ 2 Comments](/blog/posts/extra-action-in-your-page-list-processwire-core-updates-2.6.5/#comments)


## ProcessWire core updates 2.6.5


### Get extra action from the Page List and Lister

When using ProcessWire's page list tree, or Lister (or ListerPro) you now have a lot more actions available to you for any given page. New actions include:

- Publish
- Unpublish
- Hide
- Unhide
- Lock
- Unlock
- Trash*
- Restore
- Copy*

The nice thing about these extra actions is that they are ajax driven and happen right within the PageList or Lister. So these actions happen on click, with the results visible immediately in your PageList or Lister.

*You previously did have Trash and Copy options, but both have been rewritten a bit and moved into the "extra action" list to accompany the others.

We've always been interested in keeping the page list pretty minimal, so that it always remains as easy as possible, whether a newcomer to ProcessWire or a long time user. So these new actions have a trigger you must click before you see them. These screenshots should describe it best:

In Lister/ListerPro, horizontal space is typically more limited, so it shows either the main (Edit, View, New) actions, or the extra actions, but not both at the same time:


### New inline page copy/clone option

ProcessWire has always had a copy/clone option, so long as you had the core ProcessPageClone module installed (which I almost always recommend). Previously when you clicked the "copy" button in the PageList, it took you to another page, which asked you some more questions (like new name, title, whether to copy children, etc.).

The copy/clone action has been updated so that if the page being cloned has no children, it'll create the new clone without you having to leave the page list or Lister. From there, you can just click "edit" on the clone and modify not just the name and title, but anything else on the page as you see fit. This is a particularly nice workflow improvement when using ListerPro and modal editing windows.


### New restore from trash feature

From this point forward, any pages you individually put in the trash can now be restored to their original parent and order, without you having to do anything, other than clicking a "restore" action in the Page List.

This is one of the new "extra actions", and it's also available from the API side as `$pages->restore($page);` where `$page` is any page in the trash. The restore function has always been part of the API, but you had to populate the parent (and sort, if used) to the $page you were restoring ahead of time. Now ProcessWire keeps track of this information for you whenever you trash a page. However, you can still populate your own parent to the $page from the API if you prefer (or by dragging a page out of the trash interactively). But if you don't, PW will now figure out where it's supposed to go for you.

Note that this feature only works on pages you trash from this point forward. Pages already in the trash don't have the parent and sort information recorded with them, since they would have been trashed in some version of PW before 2.6.5.


### New page list label format gives you a lot more control

When viewing the page tree in ProcessWire, you typically see pages with their "title" field shown (or "name" if they have no title). If you've hunted around a bit, you may have discovered that you can specify different fields to appear as your page list labels, or even multiple fields at once. You can do this by specifying them individually for each template (Setup > Templates > edit any template > Advanced tab > Page Labels), or specify the default(s) for all pages in the ProcessPageList module settings.

But the flexibility didn't go much beyond that, as it would simply display your field values separated by commas. As of ProcessWire 2.6.5, you now have a lot more flexibility with your page list labels, as you can specify a format string. The format string lets you use whatever punctuation and additional characters you'd like.

A format string is simply any string of text where the field names are surrounded in curly `{brackets}`. For field values that resolve to objects (like Page reference fields), you can also also specify a property, like `{categories.title}` to display the "title" of a "categories" field on the page.

As an example, lets say that we wanted our page list label to display the page ID, title, date and categories in a format like this:

```
1234: Page Title - 2015/10/10 (Some Category, Another Category)
```

Our format string would be:

```
{id}: {title} - {date} ({categories.title})
```


### What else is new?

Major portions of ProcessWire's hooks system were rewritten/refactored this week to resolve an issue relating to hook priority levels, and to optimize a few things while we were there. This particular update doesn't affect you unless you were a module developer trying to change the order in which your hooks get executed. Though this was probably the biggest update (in terms of time) this week. If we did everything right, you shouldn't notice anything different. Even if there isn't anything fun to see in refactoring the hooks system, we're always tinkering with the foundations of ProcessWire, always trying to make it better and better.

In other news, we've got a great new update coming for ListerPro in the next week or two, so stay tuned for that. We'll also soon be releasing a new module sponsored by Avoine that lets you define and execute if-then tasks that can execute predefined and custom actions from any hook in ProcessWire, all handled interactively in the admin. We think you'll like it!
