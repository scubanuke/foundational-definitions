# FD-EV · The Envelope

<p class="lede">Reserves “envelope” for the thing that is authorized in advance, and names the operational sense the operating band. Version 0.2 in the November 2026 Edition.</p>

<div class="flagbar"><span class="flag">Posted for Comment</span> &nbsp;The formal statements on this page have not yet been checked by a mathematician. The definition text quoted below is the issued instrument and governs.</div>

## What it is

An **envelope** is a pre-authorized region of action (<em>The Envelope</em> §4.1). It is an object of authorization, not of monitoring. A region is an envelope when an above-line action inside it has been authorized in advance by a qualified human on an accepted proof, and when a change to the region is itself a governed act. The other, everyday engineering sense, the region of normal operation whose violation is a runtime event to detect and report, is renamed the **operating band**. Its boundary is an operating limit, the approach to it is encroachment, and a crossing is an operating-limit excursion.

## Why it matters

The sector series used "envelope" in both senses, often in the same paragraph. The two senses carry opposite obligations. An envelope is something a Broker accepted and only a governed act may change. An operating band is something an operator watches. A reader who meets "the AI operates within its envelope" cannot tell whether that is an authorization claim or a monitoring claim. Reserving the word makes the claim visible.

## The formal statements

<div class="stmt"><div class="s-head"><span>Statement 1 · What makes a region an envelope</span><span><span class="new">NEW · draft for review</span> <span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">A region is an envelope exactly when it was authorized in advance by a qualified human, its bounding proof was accepted, and any change to it is a governed act. Otherwise it is an operating band.</p>
<div class="lbl">Word notation</div><p class="words">FOR EVERY region R:<br>Envelope (R)&nbsp; IF AND ONLY IF &nbsp;Authorized in advance (R)&nbsp; AND &nbsp;Proof accepted (R)&nbsp; AND &nbsp;Change only by governed act (R)</p>
<div class="lbl">Read aloud</div><p class="aloud">A region earns the name envelope only by carrying an authorization, an accepted proof and a governed change.</p>
<div class="lbl">In symbols</div>

$$\forall R\;\big(\,\mathrm{Env}(R)\;\leftrightarrow\;\mathrm{PreAuth}(R)\,\wedge\,\mathrm{ProofAcc}(R)\,\wedge\,\mathrm{GovChange}(R)\,\big)$$

<p style="font-size:16px;color:var(--muted)">Drafted for this site from <em>The Envelope</em> §4.1. The working paper discusses FD-EV in prose only and gives it no statement of its own.</p>

</div></div>

<dl class="terms">
<dt>Authorized in advance</dt>
<dd>A Broker, discharging in advance, authorized above-line actions inside the region (<a href="#/fd-br"><em>The Broker</em> §4.2</a>).</dd>
<dt>Proof accepted</dt>
<dd>The completeness proof of <a href="#/fd-bl-d1"><em>Mode of Discharge</em></a> R2 was accepted for it.</dd>
<dt>Change only by governed act</dt>
<dd>A deliberate, authenticated act by a qualified human, recorded, which no automated element can perform or complete alone (<a href="#/fd-ls"><em>Local Sovereignty</em> §3.2</a>). A change to the envelope can never be discharged in advance (R3).</dd>
</dl>

One set can carry two structures, and mathematicians say so routinely. The operating band and the pre-authorized envelope may be the same physical region of states. What differs is what is attached. The envelope carries an authorization, an accepted proof and a governed change. The operating band carries monitoring and reporting. The test at §4.4 is the instruction to name the structure, not merely the set: ask which obligation the sentence is about.

## The definition, as issued

> An **envelope** is a pre-authorized region of action. It is an object of authorization, not of monitoring.
>
> The term “envelope,” and the compound “pre-authorized envelope,” are reserved for Sense G throughout the corpus.
>
> The operational sense — the region of normal operation whose violation is a runtime event to detect and report — is renamed the **operating band**. A sector term may stand in for “operating band” where a sector already carries an established term for the designed operating region, provided it is stated once, used consistently, and is not “envelope.”
>
> — <em>The Envelope</em> §4.1 to §4.3, v0.2

## Relations to the other instruments

**<a href="#/fd-bl-d1">Mode of Discharge</a>** permits advance discharge within an envelope and forbids advance discharge of a change to one. **<a href="#/fd-br">The Broker</a>** names the human who accepts the envelope. **<a href="#/fd-ls">Local Sovereignty</a>** supplies the definition of a governed act. **<a href="#/fd-dbl">Design Basis Layers</a>** uses operating limits, not envelopes, for the bounds within which the function is performed.

## What changed in the November 2026 Edition

Nothing. The Envelope is carried unchanged at v0.2.
