# ProcessWire 3.0.120 and continued site rewiring (part 4)

Source: https://processwire.com/blog/posts/processwire-3.0.120-and-more-new-site-updates/

## Sections


## ProcessWire 3.0.120 and continued site rewiring (part 4)

30 November 2018 by Ryan Cramer [ 7 Comments](/blog/posts/processwire-3.0.120-and-more-new-site-updates/#comments)

This week ProcessWire 3.0.120 is on the dev branch. This post takes a look at updates for this version and talks about our work towards the next master version. In addition, we take a look at some more updates and screenshots for the new ProcessWire.com website.


### ProcessWire 3.0.120

Relative to version 3.0.119 this update focuses primarily on resolving issue reports from GitHub as well as various other small improvements and optimizations.

Last week in a [forum post](/talk/topic/20385-weekly-update-nov-23-2018/?tab=comments#comment-176534) I mentioned that we’re now working towards our next master version. I tend to wait too long between master versions and end up with dev versions that are often more stable than the master. That’s because the dev versions have months worth of resolved issues and such. So my focus right now is on identifying and fixing any issues that are new to the dev branch (that aren’t on the current master). After spending a couple days in the issue reports this week, I feel like we may already be there.

I’m going to be working through issue reports next week and focusing especially on those that might be new to the dev branch. Following that, 3.0.121 will be the first release candidate for the next master. After we get the next master version out, I’m going to go back and resolve any remaining issue reports that aren’t necessarily specific to the dev version.


### Rewiring ProcessWire.com continued (part 4)

Progress continues on the new ProcessWire.com website. At this point, the main site is nearly fully built out. Just about everything but the homepage is there, though a lot of detail work remains to be done throughout. I’ve been trying to get the largest parts of the development work in place so that I can get it to the point where it’s useful for staging and collaboration.

Let’s take a look at a few screenshots of where it’s at right now. These are in addition to the [previous screenshots posted earlier](/blog/posts/processwire-3.0.119-and-new-site-updates/#new-processwire.com-site-update-part-3). Some of your suggestions in that post are already present in these screenshots. By the way, I'm cropping out the footer in most of these screenshots since it takes quite a bit of vertical space and you've already seen it in the previous round.

This first screenshot shows the About page, which is kind of typical of many index pages in the site. Since the site uses drop-down navigation, it’s likely many will never see these index pages, so I’m just keeping them relatively simple.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2459/about.png)

Next is an example of a general content page in the About section. The right sidebar of most pages in this section randomly feature selections from the Showcase. This page is actually about twice as long as what's shown, but I've cropped it half way just to avoid a massive screenshot.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2459/about-whats-unique.png)

Since we are showing a selection of showcase sites on various pages, clicking any of them leads to a details page for the showcase site that you clicked on. The next screenshot shows an example of that.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2459/showcase-site.png)

Here’s an example of a Showcase category page:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2459/showcase-category.png)

Here’s the downloads index page. This is shown with the dropdown selected as well.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2459/download.png)

If you click the ProcessWire link on the page above, you get to the core download page:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2459/download-core.png)

Next up is the blog index page. This continues the “everything wired together” theme used throughout the site, though in this case it’s also part of the masonry grid layout being used here:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2459/blog.png)

Here’s a look at a blog post. This is probably the shortest blog post ever, ideal for a screenshot:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2459/blog-post.png)

Here’s an example of a Blog Category page, something that we don’t have on the current site. In this case, the category dropdown is also hovered:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2459/blog-category.png)


### Rewired search engine

One thing that I gathered from your comments is that you’d like to see a better search engine on the site, that integrates everything. That’s what I’ve spent most of my time working on this week. I now think we’ve got a great search engine. The following screenshots preview some of the capabilities.

First off, the search engine is a live search, so the results appear as you are typing. Secondly, the results are categorized by section of the site. And as you can see, it searches the modules directory too, unlike the existing site search.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2459/search-live.png)

You can click on any category in the search to view more results and get more details about those results:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2459/search-results.png)

Some parts of the site also get their own focused search engine. For instance, even though the main site search engine also searches the API, the ProcessWire API section of the site also gets its own API-focused engine as well:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2459/api-search.png)

That’s all for this week. Thanks for reading and have a great weekend. Check in at the ProcessWire Weekly this weekend for the latest ProcessWire news and updates.
