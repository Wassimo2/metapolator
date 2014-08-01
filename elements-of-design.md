## overall structure
Let’s develop an overall structure for the user interaction; a global plan for where everything in Metapolator ‘lives’. All the functionality we have to pack, even for v1.0, does not fit on one screen; different departments need to be created. But we also want to create a sense of continuity for users, not just a collection of screens and panels.

We can observe the following:

* the **masters** form the connection between the world of skeletons & parameters, and the design spaces.
* the **instances** form the connection between the design spaces and real font (families).
* the two statements above have in common the **design spaces**, they connect masters to instances.

With these three connecting elements, we can chain four departments together, their working titles are:

1. Parameters
* Design Spaces
* Metapolation
* Fonts

![](http://mmiworks.net/metapolator/trainof4.png)

Giving everything its place it looks like this:

![](http://mmiworks.net/metapolator/refined6.png)

**notes**, from left to right:

* **parameters** is where the cascading parameter system is displayed and edited (driven by context of the next section); here also the global, project parameters can be found (always, heh);
* **character range or specimens** are set up here and form the working context for editing a whole master, a glyph (range), point(s), lines(s), or vector shape(s)—all via the parameter section or via direct manipulation here.
* **masters and adjustment masters** are managed here and drive either the character range or specimens section or are input to the next two sections.
* **(adjustment) master sequences**, are managed here.
* **design spaces** set up here from the master side; worked in from the instance side; in the lower half **character range or specimens** can be evaluated, deeding on the master(s) or instance(s) highlighted.
* **metapolation sliders** supplement the more visual and explorative design spaces with precise input (see [minimum ratio](https://github.com/metapolator/metapolator/wiki/metapolation#minimum-ratio)).
* **(strings of) instances** are managed here.
* **font (family) mapping** is managed here, large-scale font export takes place from here.
* **metadata** is maintained and assigned here to the font (families).
* beyond this, in the future kerning and hinting will also find a home at this side of this tableau.

Driven by the choice of department (Parameters, Design Spaces, Metapolation, Fonts) the viewport slides left or right, showing the continuity between these departments:

![](http://mmiworks.net/metapolator/slide5.png)

_(yes, for R-to-L language UI localisation, the whole order of these sections needs to be reversed, because its sequence is a forward/backward order in reading direction)_

The individual department views, Parameters:

![](http://mmiworks.net/metapolator/paraview.png)

Design Spaces:

![](http://mmiworks.net/metapolator/designview2.png)

Metapolation:

![](http://mmiworks.net/metapolator/metapolview2.png)

Fonts:

![](http://mmiworks.net/metapolator/fontsview.png)

**quick note**: it will not be required to set up and navigate to the Fonts section to get a font out of Metapolator—for a quick try-out there will be quicky font export available for individual masters and instances (& co).

## working with masters and glyphs in context
Let us develop the section called ‘character range or specimens’, the one visible in the Parameters department. It has got a range of important jobs to do:

1. show the character range or specimen for any number of masters and adjustment masters—the ones that are highlighted in the masters and adjustment masters panel;
* let users control how much, how big and how mixed it is what they _see_;
* let users control if they are working with parameters & skeletons on a master, glyph, or sub-glyph level—on one or more items;
* offer, where appropriate, direct-manipulation of skeletons and parameters;
* show the _immediate_ effect (live update) of parameters & skeleton changes;
* let users add, sort and delete glyphs from masters.

### 1. character range is a specimen
The first thing we will do is to put the character range view and specimens on equal footing—_well almost, see later_. That means: the character range view is just another specimen, where glyphs appear only once, by default sorted according to character code.

Thus character range appears on a popup list of possible views, as does a general sentences view (sourced from a news feed, one for each script) and some specific ones for checking numbers, punctuation, etc. This list is extendible through html files.

### 2. character filtering and the big mix
These interactions are for the general sentences view:

* a text field allows to enter characters which users want to focus on; a slider sets how strict this focus is: from ‘at least one char must appear in words’ to be shown, to ‘only combinations of the entered letters’ are shown.
* when multiple (adjustment) masters are to be shown, mix masters by: the paragraph / word / character;
* when multiple scripts are to be shown, mix scripts by: the paragraph / word / character;
* a long display size slider, offering a wide range of sizes.

These are for the other views:

* when multiple (adjustment) masters are to be shown, mix masters by the glyph, or pivot per master;
* when multiple scripts are to be shown, mix scripts by: the paragraph / word / character
* a long display size slider, offering a wide range of sizes.

### 3. the highlight
What is highlighted (aka selected) in this section steers the level work is done:

* if nothing is highlighted, the work is done on the current master(s);
* if one or more glyphs in the current view are highlighted, the work is done on these glyphs;
  * although all specimens (including character range) are very typographical (for lack of a better word), i.e. well-set text, the highlighting behaviour is that of a grig of glyphs (completely analogue to making (complex) selections in an icon grid in a file browser).
  * how to highlight? it is very important that the ‘black’-on-white view of these glyphs of interest is preserved, but also that it is clear that they are the ones being worked on; even the visual interaction with their nearest neighbours should not be interrupted. A coloured rule under the glyph seems to be the most promising.
  * note that multiple glyphs can be highlighted across multiple (adjustment) masters (since these can be displayed at the same time).
* if one or more sub-glyph points are highlighted, the work is done on these points. note that multiple points can be highlighted across multiple glyphs, across multiple (adjustment) masters (since these can be displayed at the same time).
* if one or more sub-glyph lines are highlighted, the work is done on these lines. note that multiple lines can be highlighted across multiple glyphs, across multiple (adjustment) masters (since these can be displayed at the same time).
* if one or more sub-glyph vector shapes are highlighted, the work is done on these vector shapes. note that multiple vector shapes can be highlighted across multiple glyphs, across multiple (adjustment) masters (since these can be displayed at the same time).

**example**: with the components we got up to now it is very easy to set up a view that is filtered to show only the glyphs ‘a’ and ‘g’, for 3 master fonts (i.e. 6 glyphs are on the screen). Now the 3 ‘a’s can be multi-selected and a parameter change at glyph level can be done. Next, for all 6 glyphs one point is selected (6 points in total multi-selected) and the point parameter tension-in is lowered a bit (to 90% of its previous value). Finally, nothing is highlighted and for the 3 masters a parameter change is made at master level.

### 4. down to the bone
From a certain display size (say, 144pt) and up, it becomes feasible to directly manipulate (i.e. edit using the mouse) the skeletons. These can then be shown for a glyph on mouse-over. Approaching points or lines enlarges them to be able to grab them faster, shaving fractions of a second of the time for each action.

### 5. it’s alive
Immediate, live update of parameters & skeleton changes means in practice within 500ms. The bad news is that _every_ instance of what is being worked on must update simultaneously; the good news is that only what is visible needs to update.

### 6. managing
Ah yeah, what is special about the character range view? It is the only one where it makes sense to offer glyph management (add, sort and delete).