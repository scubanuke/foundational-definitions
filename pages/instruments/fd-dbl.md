# FD-DBL · Design Basis Layers

<p class="lede">The three layers of design basis analysis, the function that holds them together, and the change in what success means once an adversary is in the analysis. New in the November 2026 Edition at version 0.15.</p>

<div class="flagbar"><span class="flag">Posted for Comment</span> &nbsp;The formal statements on this page have not yet been checked by a mathematician. The definition text quoted below is the issued instrument and governs.</div>

## What it is

A design basis layer has five parts: the function the facility must perform; the conditions under which the design is analyzed; the assumptions under which those conditions are postulated; the success criterion; and the operating limits (<em>Design Basis Layers</em> §4.1). The **Design Basis layer** establishes the function, the service the facility is built to deliver. The **accident layer** adds disruptive events drawn from experience under three assumptions: A1, independence; A2, bounded progression; A3, available support. The **adversary layer** adds an actor who sets out to stop the function. It is reached only when the actor shows all four canonical characteristics: **intentionality**, **persistence**, **precision** and **denial**. Each characteristic removes one of the accident layer’s assumptions.

## Why it matters

The whole corpus rests on this progression, and until this edition it had been enacted without ever being defined. It is where the consequence the Bright Line measures comes from: the function, and the facility’s must-not-happen outcomes. It also says why AI governance cannot stop at the accident layer. An adversary chooses which failures occur, keeps them going, aims them at the elements whose loss is hardest to recover from, and takes away the help recovery depends on. At that layer success is no longer recovery. It is reaching and holding a protected state with what is on site.

## The formal statements

<div class="stmt"><div class="s-head"><span>Statement 1 · Conditions widen, designs narrow</span><span><span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">Adding conditions can only remove designs from the acceptable set, never add them.</p>
<div class="lbl">Word notation</div><p class="words">IF one set of conditions contains another,<br>THEN every design that succeeds under the larger set also succeeds under the smaller</p>
<div class="lbl">Read aloud</div><p class="aloud">Each layer analyzes more conditions than the one before, so fewer designs pass.</p>
<div class="lbl">In symbols</div>

$$\begin{gathered}\forall C_1\;\forall C_2\;\big(\,C_1\subseteq C_2\;\rightarrow\;D(C_2)\subseteq D(C_1)\,\big)\\ \text{where }D(C)=\{\,d : \forall c\in C,\;\mathrm{Succeeds}(d,c)\,\}\end{gathered}$$

<p style="font-size:16px;color:var(--muted)">An order-reversing correspondence of the kind called a Galois connection. The arrow DB → DBA → DBA-MA walks along a nested chain of condition sets (§4.6).</p>

</div></div>

<div class="stmt"><div class="s-head"><span>Statement 2 · The accident layer is a list; the adversary layer is a game</span><span><span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">At the accident layer the design must survive each listed event. At the adversary layer it must survive the worst an intelligent opponent could choose.</p>
<div class="lbl">Word notation</div><p class="words">Accident layer: FOR EVERY event on the list, the design succeeds<br>Adversary layer: THERE IS a response, such that FOR EVERY strategy an adversary within the threat assessment could choose, the design succeeds</p>
<div class="lbl">Read aloud</div><p class="aloud">One asks about a list of events; the other asks about an opponent who watches and adapts.</p>
<div class="lbl">In symbols</div>

$$\begin{gathered}\text{Accident: }\forall e\in E\;\;\mathrm{Succeeds}(d,e)\\ \text{Adversary: }\exists\rho\;\forall\sigma\in\Sigma_{TA}\;\;\mathrm{Succeeds}(d,\rho,\sigma)\end{gathered}$$

<p style="font-size:16px;color:var(--muted)">The order of ∃ρ and ∀σ matters: reversed, it would let the response be chosen after the adversary’s whole plan is known. This is the formal reason the adversary layer cannot be reached by adding events to the accident list.</p>

</div></div>

<dl class="terms">
<dt>E</dt>
<dd>The listed set of disruptive events, drawn from operating experience and bounded because experience is bounded.</dd>
<dt>Σ<sub>TA</sub></dt>
<dd>Every strategy within the facility’s threat assessment. The adversary envelope is the threat assessment’s, not this instrument’s (§6.2).</dd>
<dt>ρ</dt>
<dd>The facility’s response strategy, which may react to what it observes.</dd>
</dl>

<div class="stmt"><div class="s-head"><span>Statement 3 · The adversary layer requires all four, each established on the record</span><span><span class="new">NEW · draft for review</span> <span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">An actor, or a recorded event, reaches the adversary layer exactly when intentionality, persistence, precision and denial are all present, and a characteristic the record cannot establish counts as absent.</p>
<div class="lbl">Word notation</div><p class="words">FOR EVERY actor or event x:<br>Adversary layer (x)&nbsp; IF AND ONLY IF<br>&nbsp;&nbsp;Established (intentionality, x) AND Established (persistence, x)<br>&nbsp;&nbsp;AND Established (precision, x) AND Established (denial, x)</p>
<div class="lbl">Read aloud</div><p class="aloud">Three out of four is not the adversary layer, and "not determined" means "not present".</p>
<div class="lbl">In symbols</div>

$$\forall x\;\Big(\,\mathrm{Adv}(x)\;\leftrightarrow\;\textstyle\bigwedge_{k\in\{\mathrm{Int},\,\mathrm{Per},\,\mathrm{Pre},\,\mathrm{Den}\}}\mathrm{Est}(k,x)\,\Big)$$

<p style="font-size:16px;color:var(--muted)">Drafted for this site from §4.4 and §6.4, including the author’s determinations of 10 and 13 October 2026, which postdate the working paper. An event without denial is recorded as military action that realizes the scenario it realizes, and does not carry the military-action tier.</p>

</div></div>

<div class="stmt"><div class="s-head"><span>Statement 4 · The protected state is a viability kernel</span><span><span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">However long the adversary keeps it up, the facility can stay protected using only what it has on site.</p>
<div class="lbl">Word notation</div><p class="words">The protected state holds&nbsp; IF &nbsp;FOR EVERY adversary action, lasting any length of time,<br>local resources alone ALWAYS keep the facility inside the protected set</p>
<div class="lbl">Read aloud</div><p class="aloud">Success at the adversary layer is holding a safe condition indefinitely, with no path back assumed and no outside help counted.</p>
<div class="lbl">In symbols</div>

$$x_0\in\mathrm{Viab}(K)\;\leftrightarrow\;\exists\rho_{\mathrm{local}}\;\forall\sigma\in\Sigma_{TA}\;:\;\square\,\big(\,x(t)\in K\,\big)$$

<p style="font-size:16px;color:var(--muted)">The viability kernel of Aubin’s viability theory. K is the protected set; ρ<sub>local</sub> uses only resources present at the facility.</p>

</div></div>

<div class="stmt"><div class="s-head"><span>Statement 5 · The tier moves the duty to defend, not the duty to survive</span><span><span class="new">NEW · draft for review</span> <span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">Where the law places defense against a state’s armed forces with the state, reaching the military-action tier moves that duty to the state. It never moves the facility’s duty to reach and hold its protected state, and no design takes credit for a state response it cannot show will arrive.</p>
<div class="lbl">Word notation</div><p class="words">IF the military-action tier is reached AND the jurisdiction’s law places defense with the state<br>THEN the duty to defend moves to the state<br>AND the protected-state criterion is unchanged<br>AND FOR EVERY design d: NOT Credit (d, the state’s response) UNLESS that response is shown to arrive</p>
<div class="lbl">Read aloud</div><p class="aloud">Handing off the defense is an allocation of responsibility, never a credit in the design.</p>
<div class="lbl">In symbols</div>

$$\begin{gathered}\mathrm{Tier}\wedge\mathrm{LawToState}\;\rightarrow\;\mathrm{DutyToDefend}=\mathrm{State}\;\wedge\;x_0\in\mathrm{Viab}(K)\text{ still required}\\ \forall d\;\big(\,\mathrm{Credit}(d,\mathrm{StateResp})\;\rightarrow\;\mathrm{ShownToArrive}(\mathrm{StateResp})\,\big)\end{gathered}$$

<p style="font-size:16px;color:var(--muted)">Drafted for this site from the paragraph added to §4.5 at v0.15, approved by the author on 15 October 2026. The United States nuclear instance is 10 CFR 50.13. The state’s defense is itself external support, which is the assumption (A3) that denial removes.</p>

</div></div>

## The definition, as issued

> The adversary layer adds an adversary: an actor who sets out to stop the facility from performing its function. The adversary is defined by capability, not by identity. Any actor that exhibits all four of the characteristics below, at the level characterized in the facility’s threat assessment, is within this layer.
>
> **At the adversary layer,** recovery is no longer a success outcome, because the adversary can defeat it and persistence and denial remove the support it relies on. Success is the transition to, and the holding of, a protected state in which consequences remain bounded, using only resources present at the facility, for as long as the adversary’s action lasts.
>
> At the adversary layer the facility may give up its function. It never gives up the requirement that whatever it does, including ceasing to perform its function, is done safely. The safety requirement is the one obligation that survives every layer unchanged.
>
> — <em>Design Basis Layers</em> §4.4 and §4.5, v0.15

## Relations to the other instruments

**<a href="#/fd-bl">The Bright Line</a>** measures consequence against the facility’s function and threshold, which the Design Basis layer establishes; FD-DBL leaves the placement of any action to the Bright Line. **<a href="#/fd-bl-d2">Indication Integrity</a>** carries the accident layer’s common-cause analysis over to information, and precision is why its independence must hold against a chosen cause. **<a href="#/fd-ls">Local Sovereignty</a>** defines one class of function that can hold a protected state once denial has removed external support and authority. The layer is an input to AI governance (§4.8), and cyber runs through every layer rather than forming a layer of its own (§4.9).

## What changed in the November 2026 Edition

FD-DBL enters the family for the first time, as its eighth member, at v0.15. Earlier working versions were not published.
