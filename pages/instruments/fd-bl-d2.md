# FD-BL-D2 · Indication Integrity

<p class="lede">What an above-line authorization may rest on: output that is traceable, corroborated and sufficient. A determination under the Bright Line. Version 0.5 in the November 2026 Edition.</p>

<div class="flagbar"><span class="flag">Posted for Comment</span> &nbsp;The formal statements on this page have not yet been checked by a mathematician. The definition text quoted below is the issued instrument and governs.</div>

## What it is

An operator who confirms an above-line action against a corrupted or drifted synthesis is not blind. He is confident and wrong, and the human authorization the framework relies on has been hollowed out without anyone noticing. *Indication Integrity* attaches an obligation to any output of an in-scope component that can serve as the basis for an above-line authorization, or as an input on which placement or discharge depends. Such output must be **traceable** to independently verifiable values (I2) and must **not be the sole basis** for the authorization (I3). The output does not move above the line. It carries a precondition.

## Why it matters

A human authorization is only as good as the picture the human is shown. Every adversary who cannot command the plant directly will try to command it through the operator, by showing him a false state. The same is true of a verified gatekeeper checking measured state. Without this determination the Command Broker obligation could be met in form and defeated in substance.

## The formal statements

<div class="stmt"><div class="s-head"><span>Statement 1 · Independent corroboration</span><span><span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">An authorization may rest on a component’s output only if a separate path can confirm the state, and no single cause could corrupt both.</p>
<div class="lbl">Word notation</div><p class="words">An authorization resting on output o is valid&nbsp; ONLY IF &nbsp;THERE IS a confirming path p<br>&nbsp;&nbsp;such that p confirms the state<br>&nbsp;&nbsp;AND NOT ( some single cause can corrupt both o and p )</p>
<div class="lbl">Read aloud</div><p class="aloud">An authorization can lean on the output only when a second, independent path confirms the state and nothing that could corrupt the one could also corrupt the other.</p>
<div class="lbl">In symbols</div>

$$\begin{gathered}\mathrm{Valid}(\mathit{auth},o)\;\rightarrow\\ \exists p\,\big(\,\mathrm{Confirms}(p)\,\wedge\,\neg\,\exists k\,(\,\mathrm{Corrupts}(k,o)\wedge\mathrm{Corrupts}(k,p)\,)\big)\end{gathered}$$

</div></div>

<dl class="terms">
<dt>o, the output</dt>
<dd>A display, synthesis, summary or recommendation. The obligation attaches by function, not by the kind of artifact (I1).</dd>
<dt>p, the confirming path</dt>
<dd>A direct read of the measurement, a diverse or redundant instrument, or a deterministic sensor channel (I2). Its grade is set by the sector annex; corroboration itself cannot be waived (I3).</dd>
<dt>k, a cause</dt>
<dd>Chance or choice. At the adversary layer, precision turns common causes into targets, so the independence must hold against a cause an adversary chooses. This is the beta-factor model of common-cause failure carried over from hardware to information.</dd>
</dl>

<div class="stmt"><div class="s-head"><span>Statement 2 · Correct is not sufficient</span><span><span class="new">NEW · draft for review</span> <span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">Before an authorization relies on a basis, the basis must show what the authorization depends on. If it does not, what is missing is identified and sought, and a basis acted on while incomplete is recorded as incomplete.</p>
<div class="lbl">Word notation</div><p class="words">FOR EVERY authorization relying on output o:<br>Sufficient (o) for what the authorization depends on<br>&nbsp;&nbsp;OR Recorded as incomplete (the authorization)</p>
<div class="lbl">Read aloud</div><p class="aloud">A true picture that leaves out what matters is not enough to authorize on silently.</p>
<div class="lbl">In symbols</div>

$$\forall \mathit{auth}\;\big(\,\mathrm{Relies}(\mathit{auth},o)\;\rightarrow\;\mathrm{Suff}(o,\mathit{auth})\,\vee\,\mathrm{RecIncomplete}(\mathit{auth})\,\big)$$

<p style="font-size:16px;color:var(--muted)">Drafted for this site from the sufficiency paragraph added to §4.3 in the November 2026 Edition. How what is missing is identified, and what may be done while it is sought, is open at this version.</p>

</div></div>

## The definition, as issued

> Output described in I1 carries the indication-integrity obligation, whatever its own placement. The obligation is discharged only where I2 and I3 both hold. Where they do not, that output may not serve as the basis for an above-line authorization, nor as an input on which placement or discharge depends.
>
> **Classifier inputs.** Where output subject to I1 serves as an input on which placement depends and cannot be corroborated through an independent path, the action it bears on shall not proceed without in-the-moment Command Broker authorization. This rule governs discharge, not placement.
>
> **Sufficiency.** An indication can be correct and insufficient. Correctness is necessary and not sufficient: where the basis for an authorization is correct but does not show what the authorization depends on, what is missing is identified and sought before the authorization is relied on, and a basis acted on while incomplete is recorded as incomplete.
>
> — <em>Indication Integrity</em> §4 and §4.3, v0.5

## Relations to the other instruments

A determination under **<a href="#/fd-bl">The Bright Line</a>**, settling its §6.2 question. Output that makes no change of its own is placed below the line at <em>The Bright Line</em> §4.2 and attracts this obligation instead. It protects both kinds of authorizer: the human **<a href="#/fd-br">Broker</a>** in the moment and the verified gatekeeper of **<a href="#/fd-bl-d1">Mode of Discharge</a>**. Its independence test and the reachability test of **<a href="#/fd-ls">Local Sovereignty</a>** ask the same question: can anything the adversary reaches affect both paths? It applies to the output of any component within scope under **<a href="#/fd-ld">Layer Decomposition and Determinism</a>**.

## What changed in the November 2026 Edition

Version 0.4 to 0.5. §4.3 gains the sufficiency paragraph.
