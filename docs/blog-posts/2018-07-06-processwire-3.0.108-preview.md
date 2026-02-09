# ProcessWire 3.0.108 preview

Source: https://processwire.com/blog/posts/processwire-3.0.108-preview/

## Sections


## ProcessWire 3.0.108 preview

6 July 2018 by Ryan Cramer [ 2 Comments](/blog/posts/processwire-3.0.108-preview/#comments)


## ProcessWire 3.0.108 preview

I've got a pretty major rewrite of ProcessWire’s admin live search in progress. It's nearly done, but needs another few days to wrap it up and make sure everything is perfect before committing to our dev branch. So I'm going to hold PW 3.0.108 till next week, and then next week's blog post will cover some more on this, as well as other updates. We'll get started covering 3.0.108 in this post, and then follow up with more next week.


### New live search updates in ProcessWire

**Now any module can be searchable** The updated live search function enables any PW module (whether core or 3rd party) to easily make its items searchable from that little search box in the top right corner of your admin. I've updated the core Process modules for fields and templates to implement this, which you might not notice initially since they were searchable before. But now they are searchable in a way that any other module can support in the same way. So I've gone ahead and made other things searchable in the live search, like Comments and Forms (FormBuilder) for example. Next week I'll also get into how any module can support it, along with an example of how to do it (it's really simple).

**How the searching works** The search works as before, in that you just start typing and it starts finding stuff for you. For most people, that's likely all they need to know. Only now the search is smarter, and also potentially searches a lot more. While you don't have to do anything other than start typing what you are looking for, for the power users among us, there's also a lot of new tricks. The rest of this post will cover some of them. For instance, you can tell it to limit results to a particular type of asset, limit results to pages using a specific template, or even tell it what properties/fields you want it to perform the search upon.

**Page searching tricks** While the new search function now enables you to search just about anything, pages are still likely to be the most common thing to search here, so this is where much of the power-user fun can be found. As before, you can simply type something like "hello" and it'll match all pages having that in the title. But now you can also do things like type "pages=hello" and it'll match just pages (excluding other types), or "pages.body=hello" and it'll match pages having the word "hello" somewhere in the body field, rather the title field. (Of course you can substitute any other field.) If you want to limit your search to just pages having a particular template, you'd type "blog-post=ProCache" to find all blog-post pages here that mention ProCache in the title. Or "blog-post.body=ProCache" would find all posts here that mention ProCache in the body.

**Searching other assets** A similar strategy can be applied to searching other module managed assets. If you wanted to limit your search to comments (like those that appear underneath these blog posts) you would type "comments=Tracy" and that would search only comments for the word "Tracy", rather than everything else (pages, fields, templates, modules, etc.). Or if you wanted to find comments by a particular person, you'd type "comments.cite=Adrian".

**Live search with a selector** This is basically an interactive search engine that optionally supports a selector statement, which, if you've spent much time with ProcessWire, likely looks pretty familiar. The difference is that you can specify just one "type=text", or "type.property=text" statement per search. If there's no "=" present in what you type, then it's assumed it is just "text" and it should search everything.

**Search operators** We are treating the "=" operator as a "contains phrase" (%=) operator, since that's what you'll want 99% of the time. But if your query "text" has more than one word, then it assumes the intention is instead a "contains words" (~=) operator; meaning the words do not have to appear next to each other. If you want a literal equals operator, you can use "==". Or if you want to literally specify some other operator (like ^=, %=, *=, !=, <=, >=, etc), go ahead—it supports them all.

**Configuring result type order** Notice in the screenshots here that the "Comments" matches are coming up first. What if you wanted them to come last instead? Or maybe you don't want comments to be searched unless you type "comments=..."? You are in luck. The ProcessPageSearch module lets you configure what resources should be searched by default, and in what order.

**View all and pagination** On a large site, there's always a good chance that it'll match more stuff than can reasonably be displayed in a live search result. When that's the case, it gives you a "View All" link. That link takes you to a paginated set of results where you can see everything. If it happens to be for pages, then ProcessWire uses Lister/ListerPro to handle that.


### Screenshots

If there are too many items to show in the dropdown, a “View all” link appears, which leads to a paginated page of results:

Regular pages are isolated from those in the trash (a feature request from Adrian in the requests repo). Plus, pages now identify their status in the same way that those in the PageList do.

This demonstrates focusing in on the "body" field of pages for the term "jQuery":

When matching fields, the search engine searches field name, label, description, notes and Fieldtype (as shown below):

Searching for all blog-related templates in this site:

Next week I'll have this feature ready to use and will tell you some more details, along with other updates going in 3.0.108. Btw, if you haven't already seen it, check out Joshuag’s [preview](/talk/topic/19557-designme-visually-layout-your-edit-screens-preview/) of his DesignMe module that he posted in the forums (video), it's quite amazing. I hope that you all have a great weekend. Thanks for reading, and stop by and enjoy the [ProcessWire Weekly](http://weekly.pw) this weekend.
