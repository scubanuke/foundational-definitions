# FD-BL-D1 · Mode of Discharge

<p class="lede">When the Command Broker may discharge the authorization in advance, with a verified gatekeeper admitting each action. A determination under the Bright Line. Version 0.5 in the November 2026 Edition.</p>

<div class="flagbar"><span class="flag">Posted for Comment</span> &nbsp;The formal statements on this page have not yet been checked by a mathematician. The definition text quoted below is the issued instrument and governs.</div>

## What it is

An authorization decision has two parts: **admissibility** (is the action inside a pre-authorized, verified region?) and **selection** (which action, at what magnitude, in what order, at what rate?) (<em>Mode of Discharge</em> §3). Advance discharge is permitted for an action in the eligible class **if and only if** the construction satisfies R1, R2 and R3 together. Under them the human authorization is "not skipped; it is relocated in time" (§4.4). The Command Broker, discharging in advance, defines and authorizes the envelope, accepts the completeness proof, and keeps sole authority over any change to it.

## Why it matters

Without this determination there are only two choices: a human at every above-line action, which is impossible at machine speed, or no human at all. R1 to R3 describe the narrow third case, in which a proof a qualified human accepted does the work the human would have done, exactly as a protective function’s actions are authorized in advance by its qualification. They also say plainly where the third case ends.

## The formal statements

<div class="stmt"><div class="s-head"><span>Statement 1 · The determination</span><span><span class="new">NEW · draft for review</span> <span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">Advance discharge is available for an action exactly when the action is in the eligible class and all three requirements hold.</p>
<div class="lbl">Word notation</div><p class="words">FOR EVERY above-line action a:<br>Advance discharge permitted (a)&nbsp; IF AND ONLY IF &nbsp;Eligible (a) AND R1 AND R2 AND R3</p>
<div class="lbl">Read aloud</div><p class="aloud">Advance discharge needs all three requirements at once, and an action in the eligible class.</p>
<div class="lbl">In symbols</div>

$$\forall a\;\big(\,\mathrm{Adv}(a)\;\leftrightarrow\;\mathrm{Elig}(a)\wedge R_1\wedge R_2\wedge R_3\,\big)$$

<p style="font-size:16px;color:var(--muted)">The working paper states R1 and R2 separately (Statements 2 and 3) and treats R3 by analogy. This conjunction restates the operative sentence of §4.</p>

</div></div>

<div class="stmt"><div class="s-head"><span>Statement 2 · R1, the whole safety case lives in the gatekeeper</span><span><span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">Safety must hold whatever the proposer proposes, including the worst thing it could propose.</p>
<div class="lbl">Word notation</div><p class="words">FOR EVERY way the proposer might choose its actions, including the worst:<br>the plant ALWAYS stays inside the safe set</p>
<div class="lbl">Read aloud</div><p class="aloud">No choice the proposer could make, however bad, can take the plant outside the safe set.</p>
<div class="lbl">In symbols</div>

$$\forall \pi\;\;\square\,\big(\,x_{G\circ\pi}(t)\in \mathrm{Safe}\,\big)$$

</div></div>

<dl class="terms">
<dt>π, the proposer’s policy</dt>
<dd>Every way the in-scope proposer could choose its actions. The proposer holds proposal authority only.</dd>
<dt>G ∘ π</dt>
<dd>That policy filtered through the gatekeeper G, which holds veto authority and is the sole path to the process. This is the Simplex architecture of Sha and colleagues: an unverified controller behind a simple verified one.</dd>
</dl>

<div class="stmt"><div class="s-head"><span>Statement 3 · R2, completeness over state, trajectory and rate</span><span><span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">Starting from where the plant is, no sequence of admitted actions, in any order and at any speed, can carry it out of the safe set.</p>
<div class="lbl">Word notation</div><p class="words">FOR EVERY sequence of actions the gatekeeper admits, in any order and at any rate:<br>the plant ALWAYS stays inside the safe set</p>
<div class="lbl">Read aloud</div><p class="aloud">However the admitted actions are strung together, the plant never leaves the safe set.</p>
<div class="lbl">In symbols</div>

$$\begin{gathered}\forall \sigma\in \mathrm{Adm}^{*}(x_0)\;:\;\square\,\big(\,x_\sigma(t)\in\mathrm{Safe}\,\big)\\ \text{equivalently}\quad \mathrm{Reach}(x_0,\mathrm{Adm})\subseteq\mathrm{Safe}\end{gathered}$$

</div></div>

<dl class="terms">
<dt>Adm*(x<sub>0</sub>)</dt>
<dd>Every sequence of admitted actions, in any order and timing, from the current state.</dd>
<dt>forward-invariant</dt>
<dd>A set with this property is forward-invariant, and control engineers prove it with reachability analysis or barrier certificates. R2 is the difference between testing each action alone, a range check, and testing every sequence of actions. Ratcheting and oscillation are two ways that a sequence of individually acceptable actions can leave the set.</dd>
<dt>a premise</dt>
<dd>The proof is about a model of the plant. A gatekeeper proven correct against an unfaithful model is proven correct about the wrong plant, so model fidelity within a stated bound is a premise of R2.</dd>
</dl>

<div class="stmt"><div class="s-head"><span>Statement 4 · R3, changes to the envelope or gatekeeper are never discharged in advance</span><span><span class="new">NEW · draft for review</span> <span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">An action that changes the envelope, or the gatekeeper’s configuration, limits or logic, is never eligible for advance discharge.</p>
<div class="lbl">Word notation</div><p class="words">FOR EVERY action a:<br>IF a changes the envelope OR a changes the gatekeeper<br>THEN NOT Advance discharge permitted (a)</p>
<div class="lbl">Read aloud</div><p class="aloud">No runtime gatekeeper can validate a change to its own safety basis.</p>
<div class="lbl">In symbols</div>

$$\forall a\;\big(\,\mathrm{ChEnv}(a)\vee\mathrm{ChGate}(a)\;\rightarrow\;\neg\,\mathrm{Adv}(a)\,\big)$$

<p style="font-size:16px;color:var(--muted)">Drafted for this site from §4.3. The working paper relates R3 to Tarski’s result that a language cannot define its own truth, as an analogy and not as a proof: the change is sent one level up, to the Broker in the moment or to an offline requalification.</p>

</div></div>

## The definition, as issued

> Advance discharge of the FD-BL §4.5 authorization is permitted for an action in the eligible class if and only if the construction satisfies all of R1, R2, and R3.
>
> **R1.** The admitting element is a deterministic, formally verified gatekeeper through which every above-line action in the class must pass, and which the proposer, an in-scope component under FD-LD §4.3, can neither modify nor bypass.
>
> **R2.** The gatekeeper’s acceptance set shall be proven to be a subset of the truly-safe set over state, trajectory, and timing/rate — not a setpoint range check. … Where the proof cannot be produced, advance discharge is not available and the action takes in-the-moment Command Broker authorization under FD-BL §4.5.
>
> **R3.** An action that changes the pre-authorized envelope itself — or the gatekeeper’s configuration, limits, or logic, or that moves the pre-authorized envelope toward a protective setpoint — is not eligible for advance discharge under any construction.
>
> — <em>Mode of Discharge</em> §4, v0.5

## Relations to the other instruments

A determination under **<a href="#/fd-bl">The Bright Line</a>**, settling its §6.1 question; the substitutability value it determines is stated at <em>The Bright Line</em> §4.5. **<a href="#/fd-br">The Broker</a>** names the Command Broker discharging in advance as the envelope’s author: one role in two modes. **<a href="#/fd-ev">The Envelope</a>** names what is accepted. **<a href="#/fd-bl-d2">Indication Integrity</a>** governs the measured state the gatekeeper checks. Actions are individuated under <em>The Bright Line</em> §4.3, and R2 governs how actions so individuated compose. Sector instantiation is left to sector annexes (§7).

## What changed in the November 2026 Edition

Nothing. Mode of Discharge is carried unchanged at v0.5.
