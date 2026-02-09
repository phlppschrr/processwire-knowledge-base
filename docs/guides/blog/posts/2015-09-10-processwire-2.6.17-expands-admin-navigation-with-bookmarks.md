# ProcessWire 2.6.17 expands admin navigation with bookmarks

Source: https://processwire.com/blog/posts/processwire-2.6.17-expands-admin-navigation-with-bookmarks/

## Sections


## ProcessWire 2.6.17 expands admin navigation with bookmarks

10 September 2015 by Ryan Cramer [ 1 Comment](/blog/posts/processwire-2.6.17-expands-admin-navigation-with-bookmarks/#comments)


## ProcessWire 2.6.17

As we begin to wrap up our set of core features for ProcessWire 2.7, this week we added something that we think you'll find very handy, especially on large sites. You can now create bookmarks to edit, list, add or find any page(s) in the admin. We'll selectively cover each of them in the sections below.


### Page tree bookmarks

If there is a place in your page tree that you'd like to quickly get to, now you can create a bookmark for it. This can save time versus always having to drill down to it from the root of the tree. When you click a bookmark, it takes you right to that place in the tree and opens the children of the page you bookmarked. The page tree starts with the bookmarked page, rather than the root page.


### Page edit bookmarks

These are very much like the page tree bookmarks, except that clicking the bookmark takes you directly to the editor for the bookmarked page. So if you've got a page or group of pages that commonly need edits, now you can bookmark them, making them directly accessible from the top navigation.


### Page add bookmarks

We've already had page add "shortcuts" for quite some time, and they are configured with template family settings. While this works great for many instances, it takes template configuration, and requires specifically purposed templates. We still recommend you take the time to use those, but there are definitely instances where you may want to use more general purpose templates. Or maybe you just want to have an "add new page" shortcut without further configuration. To answer this, now we've got page add bookmarks.

Page add bookmarks are different from the existing "shortcuts" in that they are configured simply by specifying a parent page. Whereas shortcuts instead focus on template/family relationships. Shortcuts ask you "what type of page do you want to add?", whereas bookmarks ask you "where do you want to add a page?"

When you click a page add bookmark, you are adding a new child of the bookmarked page. If the bookmarked page allows multiple templates to be used for children, you'll be asked to select what template you want to use, as part of adding the new page.

From the navigation perspective, page add bookmarks are shown distinct from the existing shortcuts. This is because they really do have different meanings, given that shortcuts are templates, and bookmarks are parent pages.

In the screenshot below, Categories and Tools are bookmarks, whereas the items above it are shortcuts defined with template family settings.


### Page find (Lister) bookmarks

Of all the bookmark types added this week, this is the one that I think people may enjoy the most. The Lister bookmarks let you take any combination of search filters and columns, and save them as a bookmark that you (or other users in the system) can click to directly from the top navigation. They are essentially saved searches.

In addition, Lister (and ListerPro) gain a new "Bookmarks" tab at the top. From here you can review and click on existing bookmarks, or you (superuser) can add new bookmarks or edit existing bookmarks.

Below is the bookmarks tab in Lister/ListerPro. Note that non-superusers only see the clickable "Bookmark" column, whereas superusers see all the columns in the screenshot below to aid with configuration.


### How bookmarks are defined

Currently bookmarks can be defined only by the superuser, as they essentially become part of your administrative navigation. Though I do think that having user-definable bookmarks (that only they see) will be the next step, and we'll revisit soon if there is interest in it. For now the bookmarks are controlled by superuser accounts.

When logged in as a superuser, every part of your navigation where bookmarks are possible will have a "Bookmarks" item that you can click on. When you click on it, you are taken to a screen asking you to select which pages will be in the given type of bookmarks. You can drag-and-drop the order in which they appear, or you can configure them on a user role-by-role basis, so that only users in a specific role see specific bookmarks.

When it comes to definition of bookmarks in Lister, that's a little different. They are instead configured from your filters and columns. When you've got a search you want to bookmark, just click to the "Bookmarks" tab and "Add Bookmark". Unlike the other types of bookmarks, you will be asked to give your bookmark a title to describe what you are bookmarking. This title becomes the navigation label to the bookmark.

Regardless of bookmark type, they can all be edited after creation, sorted among other bookmarks, or deleted when you no longer want them.

Bookmarks in Lister have more configuration options for when you need to make edits to an existing bookmark:


### Access to bookmarks

All bookmark types support access control by user role. You can selectively configure what role is allowed to see a given bookmark, or you can specify that all roles are allowed to see the bookmark.

In order for a bookmark to be shown to a user, they must also have the relevant permission to access the Page (or Lister) the bookmark points to. For instance, if you create a "page add" bookmark for an editor role, but that role doesn't have access to add children to the page you bookmarked, then they will not see the bookmark.


### For next week…

We hope that you enjoy these new bookmark features in ProcessWire 2.6.17, and please let us know how they work for you. In the end, bookmarks are really simple and pretty much self explanatory once you try using them. And of course they work equally well whether using the default admin or the Reno admin (I've tried to include screenshots from both).

The next ProcessWire dev version (after 2.6.17) is scheduled for two weeks from now, rather than next week. However, we've still got some good stuff on the way next week, so stay tuned! Hope to see you at the [ProcessWire weekly](http://weekly.pw) on Saturday, and have a great weekend and week ahead!
