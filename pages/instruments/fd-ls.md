# FD-LS · Local Sovereignty

<p class="lede">A protective function that executes on physical law, colocated with the asset, needing no authority from any reachable system. Originated by Project 5 of the portfolio. Version 0.6 in the November 2026 Edition.</p>

<div class="flagbar"><span class="flag">Posted for Comment</span> &nbsp;The formal statements on this page have not yet been checked by a mathematician. The definition text quoted below is the issued instrument and governs.</div>

## What it is

Local sovereignty is a property of a protective function, not of a device, a layer, an architecture or a vendor (<em>Local Sovereignty</em> §3.1). A function is locally sovereign when three conditions all hold. **Physical law:** the decision is a fixed function of measured quantities and setpoints, with no learned or stochastic element, and the measurements are sensed at the function or reach it over a path nothing on the reachable side can reach. **Colocation:** it is sited with the asset it protects. **No reachable authority**, in two limbs. At the time of acting, nothing on the reachable side can withhold, delay or induce the action; this limb is absolute. Ahead of acting, nothing there can alter its setpoints, logic or bypass state except through a governed act; this limb is conditional.

## Why it matters

Everything else on this site governs what an AI may do. Local sovereignty describes what still protects the asset when the governed architecture has failed, been compromised, or become unavailable. The burden of proof sits on the intermediation, not on the independence (§3.3): a proposal to put digital intermediation into a protective decision path carries the argument for it. The ground is consequence asymmetry. A relay costs thousands and is replaced in hours; the large power transformer it saves costs millions and takes years to replace.

## The formal statements

<div class="stmt"><div class="s-head"><span>Statement 1 · At the time of acting: noninterference</span><span><span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">Nothing the adversary can reach can change what the function does.</p>
<div class="lbl">Word notation</div><p class="words">FOR EVERY two situations that differ only in things the adversary can reach:<br>the protective function’s action is the same</p>
<div class="lbl">Read aloud</div><p class="aloud">Whatever the adversary does with what it can reach, the function acts exactly as it would have acted otherwise.</p>
<div class="lbl">In symbols</div>

$$\forall r_1\;\forall r_2\;\big(\,r_1\approx_{R} r_2\;\rightarrow\;\mathrm{act}_{\varphi}(r_1)=\mathrm{act}_{\varphi}(r_2)\,\big)$$

<p style="font-size:16px;color:var(--muted)">This is information-flow noninterference, defined by Goguen and Meseguer in 1982. It compares two runs at once, so it is a hyperproperty rather than a property of any single run. It is sharper than saying the function is unreachable, because it catches corrupted measurement by definition.</p>

</div></div>

<dl class="terms">
<dt>R, the reachable set</dt>
<dd>Everything an adversary could reach. The property is relative to it: when connectivity grows, R grows and the property must be re-established.</dd>
<dt>r<sub>1</sub> ≈<sub>R</sub> r<sub>2</sub></dt>
<dd>Two runs that agree on everything outside R and may differ in anything inside it.</dd>
<dt>act<sub>φ</sub></dt>
<dd>What the protective function φ does. "The same" covers withholding, delaying and inducing alike.</dd>
</dl>

<div class="stmt"><div class="s-head"><span>Statement 2 · Ahead of acting: the governed act is a cut</span><span><span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">Every route by which the reachable side could alter the function’s setpoints, logic or bypass state passes through a governed act.</p>
<div class="lbl">Word notation</div><p class="words">FOR EVERY path by which the reachable side could alter the function’s setpoints, logic or bypass state:<br>that path passes through a governed act</p>
<div class="lbl">Read aloud</div><p class="aloud">There is no way to change what the function acts on that does not go through a deliberate, recorded act by a qualified human.</p>
<div class="lbl">In symbols</div>

$$\forall\,\pi : R \rightsquigarrow \mathrm{Params}(\varphi)\;\;\exists g\in\pi\;\;\mathrm{Governed}(g)$$

</div></div>

<dl class="terms">
<dt>a governed act</dt>
<dd>A deliberate, authenticated act by a qualified human, recorded, which no automated element on the reachable side can perform or complete alone (§3.2).</dd>
<dt>a cut</dt>
<dd>In graph terms, remove the governed acts and the reachable side is disconnected from the function’s setpoints, logic and bypass state.</dd>
</dl>

<div class="stmt"><div class="s-head"><span>Statement 3 · The property is all three conditions together</span><span><span class="new">NEW · draft for review</span> <span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">A protective function is locally sovereign exactly when it executes on physical law, is colocated with its asset, and meets both limbs of no reachable authority.</p>
<div class="lbl">Word notation</div><p class="words">FOR EVERY protective function φ:<br>Locally sovereign (φ)&nbsp; IF AND ONLY IF<br>&nbsp;&nbsp;Physical law (φ) AND Colocated (φ)<br>&nbsp;&nbsp;AND Noninterfering at the time of acting (φ) AND Governed cut ahead of acting (φ)</p>
<div class="lbl">Read aloud</div><p class="aloud">Fail any one condition, or either limb, and the property is gone.</p>
<div class="lbl">In symbols</div>

$$\begin{gathered}\forall\varphi\;\big(\,\mathrm{LS}(\varphi)\;\leftrightarrow\\ \mathrm{Phys}(\varphi)\wedge\mathrm{Coloc}(\varphi)\wedge\mathrm{NI}_R(\varphi)\wedge\mathrm{Cut}_R(\varphi)\,\big)\end{gathered}$$

<p style="font-size:16px;color:var(--muted)">Drafted for this site. The working paper formalizes the two limbs; this statement makes the physical-law and colocation conditions explicit conjuncts. Physical law is the carve-out of <em>Layer Decomposition and Determinism</em> §4.3 with learned and stochastic elements excluded, so every locally sovereign function is a carved-out component, and the converse does not hold.</p>

</div></div>

## The definition, as issued

> **Local sovereignty is a property of a protective function: that the function executes on physical law, colocated with the asset it protects, and requires no authority from any reachable system to act.**
>
> *At the time of acting, the limb is absolute.* Nothing on the reachable side can withhold, delay or induce the function’s action, whether by command or by corrupting what the function measures.
>
> *Ahead of acting, the limb is conditional.* Nothing on the reachable side can alter what the function acts on — its setpoints, its logic or its bypass state — except through a governed act.
>
> **The burden of proof is on the intermediation, not on the independence.**
>
> — <em>Local Sovereignty</em> §3.1 to §3.3, v0.6

## Relations to the other instruments

**Local sovereignty does not decide placement** (§4). A locally sovereign function is not thereby below the line, and a function lacking the property is not thereby above it. An instrument shall not cite FD-LS to establish that an action needs no Broker; the correct citation is <a href="#/fd-bl"><em>The Bright Line</em></a>, on the consequence of that action. The governed act defined here is the one <a href="#/fd-ev"><em>The Envelope</em></a> requires for an envelope change and <a href="#/fd-ld"><em>Layer Decomposition and Determinism</em></a> names for a configuration change. <a href="#/fd-dbl"><em>Design Basis Layers</em></a> asks which functions can hold a protected state once denial has removed external support, and points here for one class of them.

## What changed in the November 2026 Edition

Nothing. Local Sovereignty is carried unchanged at v0.6. It is Project 5’s construct; the instrument is its definition of record, mastered with the rest of the family.
