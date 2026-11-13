# FD-BL · The Bright Line

<p class="lede">The placement criterion: a threshold on the consequence of each individual action. Version 0.6 in the November 2026 Edition.</p>

<div class="flagbar"><span class="flag">Posted for Comment</span> &nbsp;The formal statements on this page have not yet been checked by a mathematician. The definition text quoted below is the issued instrument and governs.</div>

## What it is

The Bright Line is a threshold on actions. It is not a property of components, not a boundary between architectural layers, and not a classification of technologies (<em>The Bright Line</em> §4.1). What it partitions is the set of actions a system can take. An action falls above the line when its incorrect performance could produce a consequence at or above the severity threshold established for the facility, and below it when it could not.

## Why it matters

Almost every error the corpus has had to correct came from drawing the line somewhere else: on the technology ("generative AI is above the line"), on the layer ("the advisory-to-command seam is the line"), on the product, or on the criticality band of the application. Each of those shortcuts fails in both directions. It forces a human onto trivial actions, which breeds workarounds, and it waves through consequential ones. Drawing the line on the consequence of each action is harder to apply and is the only form that does not fail that way. It is also what makes the rule sector-neutral: every sector has actions, and every facility has a threshold.

## The formal statements

<div class="stmt"><div class="s-head"><span>Statement 1 · Placement is a threshold</span><span><span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">An action is above the line exactly when the worst its incorrect performance could cause reaches the facility’s threshold.</p>
<div class="lbl">Word notation</div><p class="words">FOR EVERY action a:<br>Above the line (a)&nbsp; IF AND ONLY IF &nbsp;Severity (a) is at least Threshold (facility)</p>
<div class="lbl">Read aloud</div><p class="aloud">An action is above the line when, and only when, the worst its incorrect performance could cause reaches the facility’s threshold.</p>
<div class="lbl">In symbols</div>

$$\forall a\;\big(\,\mathrm{Above}(a)\;\leftrightarrow\;\mathrm{sev}(a)\,\geq\,\theta_f\,\big)$$

</div></div>

<dl class="terms">
<dt>Severity (a), written sev(a)</dt>
<dd>The worst consequence the incorrect performance of the action could produce, assessed over its whole trajectory and rate (§4.2, §4.3). It is the consequence of the change the action itself would make, not of an authorization someone else grants on the strength of its output, which <a href="#/fd-bl-d2">Indication Integrity</a> governs.</dd>
<dt>Threshold (facility), written θ<sub>f</sub></dt>
<dd>The severity threshold established for the facility. The threshold belongs to the facility. The instrument does not set it, and this edition does not settle who does (front matter §5).</dd>
<dt>is at least</dt>
<dd>Severity must be comparable with the threshold, which presupposes that harms can be placed on one ordered scale. That is a real premise and is recorded as a candidate axiom.</dd>
</dl>

<div class="stmt"><div class="s-head"><span>Statement 2 · An action may not be split to lower its placement</span><span><span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">A whole change is placed at least as high as the highest of its parts.</p>
<div class="lbl">Word notation</div><p class="words">FOR EVERY action a, FOR EVERY part p of a:<br>Placement (p) is at most Placement (a)</p>
<div class="lbl">Read aloud</div><p class="aloud">Combining parts into the change they make never lowers the placement.</p>
<div class="lbl">In symbols</div>

$$\forall a\;\forall p\;\big(\,p \sqsubseteq a \;\rightarrow\; \mathrm{place}(p) \leq \mathrm{place}(a)\,\big)$$

</div></div>

<dl class="terms">
<dt>part p of a, written p ⊑ a</dt>
<dd>A piece of the change a makes. §4.3 forbids individuating an action more finely than the change it makes in order to lower its placement: where the parts would place lower than the whole, the whole is placed. A recommendation and its acceptance are one action, and a change commanded as one profile is one action.</dd>
<dt>Placement</dt>
<dd>Above or below the line, ordered so that above is higher. This is a monotonicity condition.</dd>
</dl>

<div class="stmt"><div class="s-head"><span>Statement 3 · The Gate is an invariant</span><span><span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">In every state the system can ever be in, no action that carries the obligation executes without authorization.</p>
<div class="lbl">Word notation</div><p class="words">ALWAYS: IF action a executes AND a carries the obligation, THEN a was authorized</p>
<div class="lbl">Read aloud</div><p class="aloud">However the system got here, an action that needs a Broker has not run without one.</p>
<div class="lbl">In symbols</div>

$$\square\;\forall a\;\big(\,\mathrm{Exec}(a)\,\wedge\,\mathrm{Obl}(a)\;\rightarrow\;\mathrm{Auth}(a)\,\big)$$

</div></div>

<dl class="terms">
<dt>ALWAYS</dt>
<dd>In every reachable state, including after a configuration change, a software update or a system integration (§4.5). "Architectural, not procedural" means exactly this: a procedure makes the statement true on the runs where people comply, and architecture makes it true on every run.</dd>
<dt>carries the obligation</dt>
<dd>The action is above the line and comes from a component within scope. That conjunction is <a href="#/fd-ld">Layer Decomposition and Determinism</a>’s Statement 1.</dd>
<dt>authorized</dt>
<dd>Substantively and attributably, by the Command Broker in the moment or in advance (§4.5; <em>The Broker</em> §4.5).</dd>
</dl>

<div class="stmt"><div class="s-head"><span>Statement 4 · A staged release is placed on its whole planned reach</span><span><span class="new">NEW · draft for review</span> <span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">Where a component within scope releases a change in stages, each widening is its own action, and the first release is placed on the consequence of everything it is planned to reach.</p>
<div class="lbl">Word notation</div><p class="words">FOR EVERY staged release with stages s<sub>1</sub>, s<sub>2</sub>, …, s<sub>n</sub>:<br>Placement (s<sub>1</sub>) = Placement (the whole planned reach)<br>AND FOR EVERY later stage s<sub>i</sub>: s<sub>i</sub> is its own action</p>
<div class="lbl">Read aloud</div><p class="aloud">The first ring is judged as if it were the whole rollout, and every widening after it is judged again.</p>
<div class="lbl">In symbols</div>

$$\mathrm{place}(s_1) = \mathrm{place}\Big(\textstyle\bigcup_{i=1}^{n}\mathrm{reach}(s_i)\Big) \;\;\wedge\;\; \forall i>1\;\; \mathrm{Action}(s_i)$$

<p style="font-size:16px;color:var(--muted)">Drafted for this site from <em>The Bright Line</em> §4.3 as amended in the November 2026 Edition. The same paragraph says that a vendor’s release to hosts outside any one facility is not by itself an action, and that taking it in at the facility is an action placed on its consequence that enters only through a governed act; and that a change a component within scope makes to an enterprise network is an action.</p>

</div></div>

## The definition, as issued

> **The placement criterion is consequence.** The Bright Line is drawn on the consequence of the action. It is not drawn on the technology that produced the action, on the sophistication of that technology, on whether the action is characterized as advisory or as control, or on the architectural layer in which the producing component resides.
>
> An action falls above the Bright Line when its incorrect performance could produce a consequence at or above the severity threshold established for the facility. It falls below when it could not. The consequence is that of the change the action itself would make, assessed over its whole trajectory and rate.
>
> **What one action is.** An action is one change that a component’s output would make, if executed or acted upon, to a process parameter; to a protective function’s settings, trip logic, bypass state or actuation criteria; or to the pre-authorized envelope or the gatekeeper.
>
> **The obligation is architectural, not procedural.** The control system shall be incapable of executing an above-line action originating from a component within scope of §4.4 without the required authorization.
>
> — <em>The Bright Line</em> §4.2, §4.3 and §4.5, v0.6

Three corollaries in §4.2 correct errors still in circulation. A supplier’s characterization of a product does not determine placement. Placement does not follow architectural layer: the advisory-to-command seam is a good place to build enforcement and is not the definition of the boundary. And placement does not follow determinism. §4.3 adds that placement is distinct from criticality band assignment. Band is a property of the application and sets the rigor of assessment, qualification and audit. Placement is a property of each action. A high-band application contains below-line actions, and a low-band application may contain above-line ones.

## Relations to the other instruments

**<a href="#/fd-ld">Layer Decomposition and Determinism</a>** owns scope, which decides whose actions are placed at all. FD-BL §4.4 cites it rather than restating it. The carve-out is not the line: a reactor trip is outside the obligation and above the line. **<a href="#/fd-br">The Broker</a>** is the role that discharges the obligation this Line places, and the pairing is one to one. **<a href="#/fd-bl-d1">Mode of Discharge</a>** says when the authorization may be given in advance, and **<a href="#/fd-bl-d2">Indication Integrity</a>** says what an authorization may rest on. Both are determinations under this instrument. **<a href="#/fd-ls">Local Sovereignty</a>** does not decide placement, and the boundary is stated at <em>Local Sovereignty</em> §4. **<a href="#/fd-dbl">Design Basis Layers</a>** supplies the facility’s function and its layers, against which a consequence is measured.

## What changed in the November 2026 Edition

Version 0.5 to 0.6. §4.3 gains three paragraphs after its closing rules: on a vendor’s release, on staged releases, and on changes to an enterprise network. The placement criterion, the scope rule and the obligation do not change.
