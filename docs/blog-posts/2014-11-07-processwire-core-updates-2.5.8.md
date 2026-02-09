# ProcessWire core updates (2.5.8)

Source: https://processwire.com/blog/posts/processwire-core-updates-2.5.8/

## Sections


## ProcessWire core updates (2.5.8)

7 November 2014 by Ryan Cramer [ 1 Comment](/blog/posts/processwire-core-updates-2.5.8/#comments)


### Modal Tabs in the Page Editor

This week we added modal tab support to the page editor. Special thanks to Beat Beer of [Stardesign](http://www.stardesign.ch/) for sponsoring this update. He came to me with a site that had 180 multi-language fields, multiplied by several languages, on one template. Saving a page with that many fields was slow, somewhere around 10 seconds (it's nearly a thousand inputs after all). We found server side it was only taking 2 seconds, but once you added in the bandwidth and browser rendering time, it was a solid 10 seconds, which was just too long.

We strategized on ways to solve it without having to make changes to the site. We came up with the idea of splitting the tabs off into their own page editors rather than having one request manage them all. The result is what you see on this week's dev branch updates in ProcessWire 2.5.8. Now you can edit any Tab field (InputfieldFieldsetTab) and click on the Details tab and check the box to make the tab modal.

Once a tab in the page editor is modal, that means that clicking it will open up a modal window with the editable content. The benefit here is that you don't need to render and save content that you aren't editing. Your page edits can focus in on specific parts without the overhead of loading/saving everything at once.

For sites with a lot of fields, the performance improvements are massive. That 10 second save time we mentioned earlier got reduced to somewhere near half a second for most page edits. That equates to much happier editors. It also means that your page editor can now scale further than before, or at least scale further without making you wait. Thanks again to Beat Beer and Stardesign for finding this need and making it possible to implement a solution.
