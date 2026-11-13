# FD-LD · Layer Decomposition and Determinism

<p class="lede">The companion root that owns scope: which components are analyzed under the Bright Line at all. Version 0.5 in the November 2026 Edition.</p>

<div class="flagbar"><span class="flag">Posted for Comment</span> &nbsp;The formal statements on this page have not yet been checked by a mathematician. The definition text quoted below is the issued instrument and governs.</div>

## What it is

The determinism boundary is a scope gate (<em>Layer Decomposition and Determinism</em> §4.1). It sorts components by whether their behavior has been shown to be bounded by proof. A component that is deterministic within a stated input bound and formally testable as deployed sits on the infrastructure side and is outside Bright Line analysis. Every other component is on the cognitive side and within it. That includes a component whose determinism has never been established over a stated bound, or which has never been formally tested.

## Why it matters

The corpus once fused this boundary with the Bright Line itself: "deterministic machine learning below the line, generative AI above it." That one sentence produced two errors at once. It made every generative action an above-line action, including actions of no consequence. And it made a deterministic component incapable of an above-line action, which is false and which removes from analysis the automated systems most capable of causing harm. FD-LD withdraws the fusion. Determinism decides **scope**. Consequence decides **placement**. Who authorizes is the **obligation**. No one of the three answers another (§4.4).

The carve-out also protects something. A great deal of machine learning already serving critical infrastructure, such as anomaly detection, predictive maintenance and condition monitoring, is deterministic within bounded inputs and adequately governed by the existing standards. The carve-out keeps cognitive-layer assessment off it (§4.3).

## The formal statements

<div class="stmt"><div class="s-head"><span>Statement 1 · The obligation is scope AND placement</span><span><span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">An action carries the obligation exactly when it comes from a component within scope and it is above the line.</p>
<div class="lbl">Word notation</div><p class="words">FOR EVERY action a:<br>Obligation (a)&nbsp; IF AND ONLY IF &nbsp;In scope (the component that produced a)&nbsp; AND &nbsp;Above the line (a)</p>
<div class="lbl">Read aloud</div><p class="aloud">An action needs a Broker when, and only when, it comes from an in-scope component and it is above the line.</p>
<div class="lbl">In symbols</div>

$$\forall a\;\big(\,\mathrm{Obl}(a)\;\leftrightarrow\;\mathrm{InScope}(\mathrm{src}(a),\,\mathrm{in}(a))\,\wedge\,\mathrm{Above}(a)\,\big)$$

</div></div>

<dl class="terms">
<dt>In scope</dt>
<dd>The producing component does not meet the carve-out (Statement 2). Generative and other non-deterministic components are the principal cases, not the definition.</dd>
<dt>AND</dt>
<dd>Scope and placement are independent questions joined here, not one question asked twice. One counterexample shows the independence: a reactor trip is out of scope and above the line.</dd>
<dt>src(a), in(a)</dt>
<dd>The component that produced the action and the input it was working from. Scope depends on both (Statement 2).</dd>
</dl>

<div class="stmt"><div class="s-head"><span>Statement 2 · Scope is the complement of the carve-out</span><span><span class="new">NEW · draft for review</span> <span class="flag">Posted for Comment</span></span></div><div class="s-body">
<div class="lbl">Plain English</div><p class="plain">A component is within scope for a given input and configuration unless it is deterministic within a stated bound, formally tested in the configuration it is running, and the input actually lies within that bound.</p>
<div class="lbl">Word notation</div><p class="words">FOR EVERY component c, input x and configuration k:<br>In scope (c, x, k)&nbsp; IF AND ONLY IF &nbsp;NOT (<br>&nbsp;&nbsp;Deterministic (c) within bound B<br>&nbsp;&nbsp;AND Formally tested (c) in configuration k<sub>T</sub><br>&nbsp;&nbsp;AND x lies within B<br>&nbsp;&nbsp;AND k is k<sub>T</sub> )</p>
<div class="lbl">Read aloud</div><p class="aloud">A component escapes the analysis only while it is proven deterministic over a stated range, was tested exactly as it is now running, and is being fed inputs inside that range.</p>
<div class="lbl">In symbols</div>

$$\begin{gathered}\forall c\;\forall x\;\forall k\;\Big(\,\mathrm{InScope}(c,x,k)\;\leftrightarrow\\ \neg\big(\,\mathrm{Det}(c,B_c)\wedge\mathrm{Tested}(c,k_T)\wedge x\in B_c\wedge k=k_T\,\big)\Big)\end{gathered}$$

<p style="font-size:16px;color:var(--muted)">The working paper states this without the configuration term. The term k = k<sub>T</sub> is new for the November 2026 Edition, which adds to §4.3 that the carve-out does not cover a component running a configuration other than the one formally tested, including one altered outside a governed act. How either out-of-bound condition is detected and the action routed is open at this version, and the formal reading shows that the gap is in the definition of scope itself, not in implementation.</p>

</div></div>

<dl class="terms">
<dt>Deterministic within bound B<sub>c</sub></dt>
<dd>Reproducible outputs for identical inputs over a stated input range. The qualifier is not severable: "merely deterministic" is not a valid carve-out.</dd>
<dt>Formally tested</dt>
<dd>Testable, and tested, in the deployed configuration.</dd>
<dt>x lies within B<sub>c</sub></dt>
<dd>An action produced while the inputs lie outside the stated bound is not covered by the carve-out.</dd>
<dt>NOT ( … )</dt>
<dd>Scope is everything the carve-out does not reach. The carve-out may not be narrowed to a list of named roles; it is a property test.</dd>
</dl>

## The definition, as issued

> Bright Line analysis and the Command Broker obligation apply to every component that does not meet the carve-out.
>
> A component meets the carve-out only if it is deterministic within a stated input bound and formally testable in the deployed configuration. Both conditions must hold, and the first is not severable from its bound.
>
> Generative and other non-deterministic components are the principal cases within scope. They are not its definition: a deterministic component never formally tested, or a generative model run at a fixed seed, is within scope because it does not meet the carve-out.
>
> The carve-out removes a component from this obligation only. It is not a grant of ungoverned autonomy, and it is not a finding that the component’s actions are below the line.
>
> — <em>Layer Decomposition and Determinism</em> §4.3, v0.5

Deterministic protective functions such as reactor trip, engineered safety-feature actuation and protective-relay operation are outside the Command Broker obligation **by the carve-out, not by being below the line**. They are among the highest-consequence actions in any facility. They are outside the obligation because their behavior is bounded by proof (§4.3; <em>The Bright Line</em> §4.5).

## Relations to the other instruments

**<a href="#/fd-bl">The Bright Line</a>** cites §4.3 for scope at its own §4.4, and adds that the carve-out does not extend to actions taken upon a carved-out component: an in-scope component that changes a protective function’s settings is placed on that change. **<a href="#/fd-bl-d1">Mode of Discharge</a>** calls the proposer an in-scope component under §4.3. **<a href="#/fd-ls">Local Sovereignty</a>** takes the carve-out test as its physical-law condition, with learned and stochastic elements excluded, so every locally sovereign function is a carved-out component, and not the reverse. **<a href="#/fd-bl-d2">Indication Integrity</a>** attaches to the output of any in-scope component. The surveillance Line does not inherit the carve-out: a deterministic statistical model’s societal effect is not bounded by proof.

## What changed in the November 2026 Edition

Version 0.4 to 0.5. §4.3 states that the carve-out does not cover a component running a configuration other than the one formally tested, and the open item at §7 widens to take that condition in. The Record gains R.7, which traces the layer split to the author’s formal-methods papers of 2025.
