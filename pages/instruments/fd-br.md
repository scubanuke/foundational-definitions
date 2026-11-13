# FD-BR · The Broker

<p class="lede">The qualified human role that discharges a Bright Line’s authorization obligation, in the moment or in advance. Version 0.11 in the November 2026 Edition.</p>

<div class="flagbar"><span class="flag">Posted for Comment</span> &nbsp;The formal statements on this page have not yet been checked by a mathematician. The definition text quoted below is the issued instrument and governs.</div>

## What it is

A Broker is a role: a qualified human who discharges the authorization obligation that a Bright Line places on above-line actions (<em>The Broker</em> §4.1). It is not an office, not a job title, not a software component, and not a procedure telling someone to confirm. It is the human-judgment node in a triad. The **Line** places the obligation. The **Gate** is the enforcement interlock, the architecture incapable of executing an above-line action without authorization. The **Broker** authorizes. The Gate never authorizes and never stands in for the Broker.

## Why it matters

The Broker exists for one reason: to supply judgment where proof is unavailable. It is compensation for unverifiability, not a general demand for a human in the loop. That reason sets everything else. It explains why a deterministic protective function needs no Broker, why competence is tied to the Line the Broker serves, and why a verified gatekeeper may stand in for the Broker’s presence but never for its judgment. Without the role defined once, every sector would invent its own "human in the loop", and each would mean something different.

## The formal statements

<div class="stmt"><div class="s-head"><span>Statement 1 · One Broker per Line</span><span><span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">Every Bright Line has exactly one Broker role, and every Broker role belongs to exactly one Line.</p>
<div class="lbl">Word notation</div><p class="words">FOR EVERY Line L, THERE IS exactly one Broker role that discharges L’s obligation,<br>AND FOR EVERY Broker role, THERE IS exactly one Line it discharges for</p>
<div class="lbl">Read aloud</div><p class="aloud">Lines and Broker roles pair off one to one.</p>
<div class="lbl">In symbols</div>

$$\forall L\;\exists!\,B\;\mathrm{Discharges}(B,L)\;\;\wedge\;\;\forall B\;\exists!\,L\;\mathrm{Discharges}(B,L)$$

</div></div>

<dl class="terms">
<dt>Line</dt>
<dd>A Foundational Bright Line. Today there are two: the industrial Line (FD-BL), paired with the Command Broker, and the surveillance Line (FD-SBL), paired with the Influence Broker.</dd>
<dt>exactly one</dt>
<dd>The pairing invariant of §4.2. A future Line generates its own Broker; it does not inherit one. The pairing holds across both modes of discharge: the human who accepts a pre-authorized envelope is the same Broker discharging in advance, not a second role.</dd>
<dt>consequence for competence</dt>
<dd>Competence is set by the paired Line’s placement criterion and does not transfer (§4.3). Holding two Broker roles means meeting both standards independently.</dd>
</dl>

<div class="stmt"><div class="s-head"><span>Statement 2 · The Gate never authorizes</span><span><span class="new">NEW · draft for review</span> <span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">Nothing in the enforcement architecture is ever the source of an authorization; a human Broker is, in the moment or in advance.</p>
<div class="lbl">Word notation</div><p class="words">ALWAYS, FOR EVERY action a:<br>IF a is authorized THEN THERE IS a qualified human Broker who authorized a,<br>&nbsp;&nbsp;in the moment OR in advance by accepting the envelope a lies in</p>
<div class="lbl">Read aloud</div><p class="aloud">Every authorization traces back to a named, qualified person, either at the moment or when the envelope was accepted.</p>
<div class="lbl">In symbols</div>

$$\begin{gathered}\square\;\forall a\;\Big(\,\mathrm{Auth}(a)\;\rightarrow\;\exists h\;\big(\,\mathrm{Broker}(h)\;\wedge\\ (\,\mathrm{AuthNow}(h,a)\,\vee\,\exists E\,(\,a\in E\,\wedge\,\mathrm{Accepted}(h,E)\,)\,)\big)\Big)\end{gathered}$$

<p style="font-size:16px;color:var(--muted)">Drafted for this site from <em>The Broker</em> §4.1, §4.2 and §4.4, which the working paper treats in prose. "The human discharges; the gatekeeper admits."</p>

</div></div>

<dl class="terms">
<dt>Broker (h)</dt>
<dd>A qualified individual holding the role for this Line. "Attributable" means the authorization resolves to that named individual and is reconstructable from the audit record (§4.5).</dd>
<dt>in advance, by accepting the envelope</dt>
<dd>Where the Line permits it, the Broker authorizes a pre-authorized envelope and accepts the proof that bounds it, and a verified gatekeeper then admits each action in the class. What the gatekeeper substitutes for is the Broker’s presence at the moment of action, not the Broker’s judgment (§4.4).</dd>
</dl>

Substitutability is a spectrum with one driving variable. As the availability of proof falls, the room for a verified gatekeeper to stand in for the Broker’s presence falls with it. The Command Broker is partially substitutable, for pre-proven action classes under <a href="#/fd-bl-d1">Mode of Discharge</a>. The Influence Broker is not substitutable, on present understanding.

## The definition, as issued

> A Broker is a role: a qualified human who discharges the authorization obligation that a Bright Line places on above-line actions.
>
> For every Foundational Bright Line there is exactly one Broker role that discharges its §4.5 obligation.
>
> What the verified gatekeeper substitutes for is the Broker’s presence at the moment of action, not the Broker’s judgment, which was exercised when the envelope and its proof were accepted.
>
> Authorization by a Broker shall be substantive and attributable. Substantive means the Broker has the information, competence, time, and authority to withhold authorization on the merits. Attributable means the authorization resolves to a named qualified individual and is reconstructable from the audit record.
>
> — <em>The Broker</em> §4.1, §4.2, §4.4 and §4.5, v0.11

## Relations to the other instruments

**<a href="#/fd-bl">The Bright Line</a>** places the obligation the Broker discharges and points here for the role, the pairing and the meaning of "substantive" and "attributable". **<a href="#/fd-bl-d1">Mode of Discharge</a>** sets the conditions for advance discharge on the industrial Line. **<a href="#/fd-ev">The Envelope</a>** names what the Broker accepts in advance. **<a href="#/fd-bl-d2">Indication Integrity</a>** protects the basis the Broker authorizes on. The consequence classifier sits upstream of the triad: an action reaches the Gate and the Broker only once it has been placed above the line.

## What changed in the November 2026 Edition

Nothing. The Broker is carried unchanged at v0.11 from the October 2026 Edition.
