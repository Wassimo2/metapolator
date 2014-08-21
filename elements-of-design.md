## _note:_ this is not a specification
This page lists the **first, rough** building blocks of the design. With that the Metapolator project is **out of the dark** and the [interaction design goals](https://github.com/metapolator/metapolator/wiki/interaction-design-goals) **start to be realised**. But this is not a complete solution; details are lacking; drawings are illustrations, not building plans; and the interaction is not _exactly_ specified. That is for a later phase in the project.

So enjoy the fact that you can watch interaction being created ‘out of nothing’ and that you can plan with what you see here. Thanks for your patience where it comes to the last detail. _—ps_

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

![](http://mmiworks.net/metapolator/refined7.png)

**notes**, from left to right:

* **parameters** is where the cascading parameter system is displayed and edited (driven by context of the next section); here also the global, project parameters can be found (always, heh);
* **character range or specimens** are set up here and form the working context for editing a whole master, a glyph (range), point(s), lines(s), or vector shape(s)—all via the parameter section or via direct manipulation here.
* **masters and adjustment masters** are managed here and drive either the character range or specimens section or are input to the next two sections.
* **(adjustment) master sequences**, are managed here.
* **design spaces** set up here from the master side; worked in from the instance side; in the lower half **character range or specimens** can be evaluated, deeding on the master(s) or instance(s) highlighted.
* **metapolation sliders** supplement the more visual and explorative design spaces with precise input.
* **(strings of) instances** are managed here.
* **font (family) mapping** is managed here, large-scale font export takes place from here.
* **metadata** is maintained and assigned here to the font (families).
* beyond this, in the future kerning and hinting will also find a home at this side of this tableau.

Driven by the choice of department (Parameters, Design Spaces, Metapolation, Fonts) the viewport slides left or right, showing the continuity between these departments:

![](http://mmiworks.net/metapolator/slide6.png)

_(yes, for R-to-L language UI localisation, the whole order of these sections needs to be reversed, because its sequence is a forward/backward order in reading direction)_

The individual department views, Parameters:

![](http://mmiworks.net/metapolator/paraview.png)

_On the right, manage (adjustment) masters and select which ones to work on; review in the middle, directly manipulate and possibly refine the selection to glyph(s) or sub-glyph(s); review and work on the parameters of this selection on the left._

Design Spaces:

![](http://mmiworks.net/metapolator/designview3.png)

_Place (adjustment) masters on one or more design spaces and arrange them; manage master sequences; review the (adjustment) masters on the bottom of this department._

Metapolation:

![](http://mmiworks.net/metapolator/metapolview3.png)

_Explore the design spaces; create and manage (strings of) instances and adjust them both in the design spaces and the metapolation sliders; review the instances on the bottom of this department._

Fonts:

![](http://mmiworks.net/metapolator/fontsview.png)

_Map the (strings of) instances to font (families); manage metadata and assign to font (families)._

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
These interactions are for the character range view:

* when multiple (adjustment) masters are to be shown, mix masters per glyph, or pivot per master;
* a long display size slider, offering a wide range of sizes.

These interactions are for the general sentences view:

* a text field allows to enter characters which users want to focus on; a slider sets how strict this focus is: from ‘at least one entered char must appear in words’ to be shown, to ‘only combinations of the entered letters’ are shown.
* when multiple (adjustment) masters are to be shown, mix masters by: the paragraph / word / character;
* when multiple scripts are to be shown, mix scripts by: the paragraph / word / character;
* a long display size slider, offering a wide range of sizes.

These are for the other views:

* ability to mix multiple (adjustment) masters;
* ability to mix multiple scripts;
* a long display size slider, offering a wide range of sizes.

### 3. the highlight
What is highlighted (aka selected) in this section steers the level work is done:

* if nothing is highlighted, the work is done on the (adjustment) master(s) that are highlighted in the masters and adjustment masters panel;
* if one or more glyphs in the current view are highlighted, the work is done on these glyphs;
  * although all specimens (including character range) are very typographical (for lack of a better word), i.e. well-set text, the highlighting behaviour is that of a grid of glyphs (completely analogue to making (complex) selections in an icon grid in a file browser, including the use of rubber-banding to make selections, and shift and cmd/ctrl to grow and shrink these).
  * how to highlight? it is very important that the ‘black’-on-white view of these glyphs being worked on is preserved, but also that it is clear that they are the ones being worked on; even the visual interaction with their nearest neighbours should not be interrupted. A coloured rule under the glyph seems to be the most promising.
  * note that multiple glyphs can be highlighted across multiple (adjustment) masters (since these can be displayed at the same time).
* if one or more sub-glyph points are highlighted, the work is done on these points. note that multiple points can be highlighted across multiple glyphs, across multiple (adjustment) masters (since these can be displayed at the same time).
* if one or more sub-glyph lines are highlighted, the work is done on these lines. note that multiple lines can be highlighted across multiple glyphs, across multiple (adjustment) masters (since these can be displayed at the same time).
* if one or more sub-glyph vector shapes are highlighted, the work is done on these vector shapes. note that multiple vector shapes can be highlighted across multiple glyphs, across multiple (adjustment) masters (since these can be displayed at the same time).

**example**: with the components we got up to now it is very easy to set up a view that is filtered to show only the glyphs ‘a’ and ‘g’, for 3 master fonts (i.e. 6 glyphs are on the screen). Now the 3 ‘a’s can be multi-selected and a parameter change at glyph level can be done. Next, for all 6 glyphs one point is selected (6 points in total multi-selected) and the point parameter tension-in is lowered a bit (to 90% of its previous value). Finally, nothing is highlighted and for the 3 masters a parameter change is made at master level.

### 4. down to the bone
From a certain display size (say, 144pt) and up, it becomes feasible to directly manipulate (i.e. edit using the mouse) the skeletons. These can then be shown for a glyph on mouse-over. Approaching points or lines enlarges them to be able to grab them faster, shaving fractions of a second of the time for each action.

**however**, paradoxically some restraint has to be practiced when planning for what parameters (this is what it essentially is) direct manipulation is to be provided. This is for the following reasons:

* implementation effort for v1.0;
* we have to wean users off their old habits of working glyph-by-glyph, and of getting results directly pushing around the outline (i.e. the edge) of a glyph shape; we have to put the brakes on what facilitates this.

Our guiding credo should be: we provide direct manipulation there, where it would be completely silly not to.

### 5. it’s alive
Immediate, live update of parameters & skeleton changes means in practice within 500ms. The bad news is that _every_ instance of what is being worked on must update simultaneously; the good news is that only what is visible needs to update.

### 6. managing
Ah yeah, what is special about the character range view? It is the only one where it makes sense to offer glyph management (add, sort and delete).

## parameter review and editing
Let us develop the section called ‘parameters’, the one at the very start (in reading direction) of the overall UI layout. It is used to review and edit parameters of (adjustment) masters, up and down this hierarchy:

* project
  * master
    * script
      * glyph
        * (skeleton) segment
          * line
          * point
        * vector shape

Some interesting dynamics are at play:

1. parameters really _belong_ to the lower levels of the hierarchy, i.e. parameters are **_native_** to either—
  * glyph;
  * line;
  * point;
  * vector.
* parameters set at any level in the hierarchy (except for project) can be modified at a higher level (e.g. the width set for a glyph can be scaled (* 0.9) at master level);
* parameters set at any level in the hierarchy can be modified, or even overwritten, at a lower level—down to the level where these parameters are native (e.g. the weight set for a script can be capped by a maximum (<= X) value at glyph level; the slant set at a project level can be overwritten (= 0) at glyph level);
* a number of parameters are mandatory—if one is missing, glyphs cannot be drawn. thus for a master—for each and every glyph, line, point, vector shape they native to to—they need to be be defined (= XYZ) at that, or a higher level; for an adjustment master no such requirement exists (thus is the nature of an adjustment master: it is a delta);

### challenges

1. why does this master / glyph / segment / line look like this?
  * on which hierarchy level(s) is the parameter set?
* for a given context (global, master, script, glyph, segment, line, point, vector shape), what parameters are set?
  * is there interaction with settings at higher hierarchy levels—if so, where?
  * are there settings on lower levels that make this one ineffective?
* for a given _leaf_ context (glyph, line, point, vector shape) what are the effective values of the native parameters of that level?
* when a multi-selection is the context (e.g. a couple of masters, or a handful of glyphs), how not to get thoroughly confused by a plethora of different set/effective values for the same parameter?

### the rules

From a user interaction perspective, this is a simple but effective system for how the parameter operators cascade along the hierarchy:

1. only parameters who have their value set (=) anywhere in the hierarchy are defined;<br/>
_(e.g. any scaling (*), offset (+), etc operators may be defined for width along the hierarchy, but is width is not set to value anywhere, it is undefined)_
* the lowest hierarchy level that sets the value (=) wins;<br/>
_(e.g. script level sets a parameter and glyph level too, then the glyph one wins—for this glyph)_
* all scaling (*) that is performed at any hierarchy level is applied;<br/>
_(e.g. if at project, master and glyph level a parameter is scaled, all 3 are multiplied and then applied to the set value)_
* all offsets (+) that are defined at any hierarchy level are applied; **TBD:** does scaling affect offsets?<br/>
_(e.g. if at project, master and glyph level a parameter is offset, all 3 are added up and then applied to the set value)_
* the lowest hierarchy level that sets a maximum (<=) wins;<br/>
_(e.g. master level sets a maximum and point level too, then the point one wins—for that point)_
* the lowest hierarchy level that sets a minimum (>=) wins.<br/>
_(analogue to maximum)_

### a rough design
For how to set the working context, see the [highlighting section](https://github.com/metapolator/metapolator/wiki/elements-of-design#3-the-highlight).

![](http://mmiworks.net/metapolator/masterpar.png)

Above we see the parameters panel when a master is the working context. From the top—

* project-level parameters are also displayed, in this case slant is scaled (* 2) for all masters;
* for the mast fit self the point parameter ‘Direction in’ is set; it is shown next to it that 38% of all points in glyphs in this masters have this value overwritten somewhere along the hierarchy (it is also shown for the minimum and maximum operators, where applicable);
* the ‘+’ buttons allow to add a parameter entries to the different levels;
* when master is the working context, the script level is also shown, if more than one is configured for this master; in this case both latin and cyrillic script have no parameters defined, hence they are closed by default.

![](http://mmiworks.net/metapolator/moverpar.png)

Above we see the different **mouse-over** interaction. From the top—

* close box to remove the parameter entry;
* highlight over the operator (=); click to show a popup to change it:<br/>![](http://mmiworks.net/metapolator/opspop.png)
* override percentage to highlight in the ‘character range or specimens’ panel the points that did receive an override;
* value: click to activate an edit box.

#### leaf nodes

![](http://mmiworks.net/metapolator/pointpar.png)

Above we see the parameters panel when a leaf node, a point, is the working context. From the top—

* all the hierarchy levels, from project downwards, are shown—collapsed by default—above the leaf level, but scrolled out of view (except for the direct parent) to save space;
* an offset (+) parameter is set for Tension in; its value is negative; the ‘×+’ sign shows that at higher levels scale (*) and/or offset operators have also been applied to this parameter for this point; clicking the symbol pops up a panel that shows the trail of what is applied where (it is also shown for the scale  operator, where applicable);
* the whole light-grey section is _all_ point parameters, with the current values for this point; it is split in Skeleton and Pen sections for clarity (and shorter parameter names on each line);
* parameters that have a ‘=’ before their value have been set (operator =) directly at point level, with no scaling or offsets applied;
* parameters that have a ‘:’ before their value have **not** been set (operator =) directly at point level, either operators are at play at other levels and/or at this point level also other operators than set (=) are active; clicking the ‘:’ allows to change the operator to ‘=’; clicking the value pops up a panel that shows the trail of what is applied where to reach this value.

#### copy & paste
![](http://mmiworks.net/metapolator/hipara.png)

By clicking the parameter name, any parameter-configuring item can be highlighted. It can then be cut—deleting the item—or copied to the clipboard. What is copied is the triplet of parameter name, operator and value. It can then be pasted—

* it is always pasted in the current working context, as set by the highlights in the ‘masters and adjustment masters’ and ‘character range or specimens’ panels (these can be quite complex, e.g. points across several glyphs, across several masters); there is no need to click in the parameter panel ageing to steer ‘where it needs to be pasted’;
* for each individual destination of the working context (e.g. each point of a multi-select of points), if a parameter-configuring item with the same parameter name and operator already exists, then overwrite its value with the pasted one;
  * for any other destination, add the pasted triplet as a new parameter configuration.

#### drag & drop
![](http://mmiworks.net/metapolator/moveonup.png)

Any parameter-configuring item can be grabbed by the parameter name and dragged to a **higher** level in the hierarchy. This has the same effect as Cutting the item from its original location and pasting it at its destination—but then _without_ altering the contents of the clipboard.

#### multi-select contexts
On every level of the hierarchy (below project) it is possible to make several objects _of the same type_ the working context, i.e. several masters, scripts, glyphs, lines, points, or vector shapes. The challenge is that different values may be set for the same parameter, or that for one or more selected items it is not set at all.

![](http://mmiworks.net/metapolator/multipara.png)

Above we see the display of a multi-select of four points. From the top—

* the Tension in parameter is set for 50% of the items (i.e. 2 points) that form the context; clicking this percentage number highlights in the ‘character range or specimens’ panel the points that did;
  * the range that the Tension in parameter is set to is shown to be -0.5 to 0.4;
  * no ‘×+’ sign, nor the override percentage is shown in a multi-select context, because the baths up and down the hierarchy have become so much more complex for a set;
* Angle is only set for one of the points, for multi-select contexts these part-set values are lifted out of the current-values section, where the resulting values for all items are shown;
* in the current-values section we see a mix of single and multiple values, set at point level or above.

For multi-select contexts the functionality of the parameters panel is more limited, but users can still do the following useful things:

* see what parameters are set, how often and where, for the context
* inspect the range of values, effective and/or set;
* remove any parameter entry;
* overwrite a range of values with a single one—an empty edit box is shown when clicking on the value range.

## metapolation sliders
This describes the section called Metapolation sliders, which supplement the more visual and explorative design spaces with precise input.

![](http://mmiworks.net/metapolator/slidersdefault.png)

Above a see the default slider setup for a 6-master design space. The masters are called: Regular, Black, Thin, Small caps, Serifs, ‘+ x-height’. For an N-master setup, the number of sliders is always N-1. This gives exactly enough input, together with the 100% rule, for a complete metapolation definition.

* the popups on the right and left of the sliders contain all the master labels that—
  * do not appear at the opposite side of this slider;
  * do not appear on any other slider together with the one at the opposite side of this slider.
* the popups on the left of the sliders also contain, the item ‘From zero’ it sets the slider to absolute mode:<br/>
![](http://mmiworks.net/metapolator/sliderszero2.png)
* when a popup on a slider is changed, the slider value gets recalculated and set;
* text boxes with up/down arrows allow to set the slider value precisely;
* the extra popup on the bottom-lefthand side has the label ‘All’ and contains as values all the master labels plus ‘From zero’; it sets all the popups on the left of the sliders to whatever is picked:<br/>
![](http://mmiworks.net/metapolator/slidersall.png)<br/>
…while the right side is set to all the other masters (in case of All from zero, the right side is set to the first N-1 masters as defined in the masters panel).