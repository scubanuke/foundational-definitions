# The One Principle

<p class="lede">Eight short instruments hold the definitions that my body of work, the Design Basis for AI Governance in Critical Infrastructure, applies in every sector. This site walks through them one at a time. It follows the model of Maxwell's equations on a T-shirt: a short formal statement first, and then a discussion of each term in it.</p>

Read together, most of the family applies one rule at different levels. In plain English: **a qualified human's judgment is needed at the moment of action exactly when the action could cause serious harm and its behavior has not been bounded by proof.**

<div class="principle">
<div class="lbl" style="font-family:var(--mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-weight:600">The One Principle · <span class="flag">Posted for Comment</span></div>
<p class="words">FOR EVERY action a:<br>Human judgment needed at the moment of action (a)<br>&nbsp;&nbsp;IF AND ONLY IF Above the line (a) AND NOT Proven (a)</p>
<p><em>Read it as:</em> for any action <em>a</em>, a human must judge it as it happens when, and only when, <em>a</em> is above the line and <em>a</em> has not been proven safe.</p>
<p style="font-family:var(--mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-weight:600;margin-bottom:0">In symbols</p>

$$\forall a\;\big(\,\mathrm{HumanNow}(a)\;\leftrightarrow\;\mathrm{Above}(a)\,\wedge\,\neg\,\mathrm{Proven}(a)\,\big)$$

</div>

## Term by term

<dl class="terms">
<dt>FOR EVERY action a</dt>
<dd>The rule is stated about actions, not about systems, products or technologies. An action is one change that a component's output would make to a process, to a protective function, or to a pre-authorized envelope or its gatekeeper (<a href="#/fd-bl"><em>The Bright Line</em> §4.3</a>). A single product typically produces actions on both sides of the line.</dd>
<dt>Human judgment needed at the moment of action</dt>
<dd>A qualified human, the Broker, must authorize this action as it happens, substantively and attributably (<a href="#/fd-br"><em>The Broker</em> §4.5</a>). The control system must be architecturally incapable of executing it without that authorization.</dd>
<dt>IF AND ONLY IF</dt>
<dd>The rule runs both ways. Where the right-hand side holds, the human is required. Where it does not, the human is not required by this rule. The Broker is compensation for unverifiability, not a general demand that consequential actions involve a person.</dd>
<dt>Above the line (a)</dt>
<dd>The incorrect performance of the action could produce a consequence at or above the severity threshold established for the facility. Placement is consequence, action by action (<a href="#/fd-bl"><em>The Bright Line</em> §4.2</a>).</dd>
<dt>NOT Proven (a)</dt>
<dd>The action's behavior has not been bounded by proof. Each instrument supplies "proven" at its own level. <a href="#/fd-ld"><em>Layer Decomposition and Determinism</em></a> applies it to a component, through the determinism carve-out. <a href="#/fd-bl-d1"><em>Mode of Discharge</em></a> applies it to a region of action, a verified gatekeeper's acceptance set. <a href="#/fd-ls"><em>Local Sovereignty</em></a> applies it to a protective function and adds that nothing an adversary can reach can influence it.</dd>
</dl>

The statement simplifies one thing. The carve-out and the gatekeeper are different kinds of "proven". The carve-out removes a component from the obligation altogether. The gatekeeper removes nothing: it moves the Broker's judgment earlier in time, to the acceptance of the envelope and its proof. That is why *Mode of Discharge* §4.4 says the authorization is "not skipped; it is relocated in time." The principle is about the moment of action, and it is true of both.

The principle is also the strongest candidate for the corpus's first axiom. It is a value premise, not an empirical one. No experiment could show it false; a reader can only accept it or reject it. The formal statement of the axioms is planned for the December 2026 Edition.

## How the eight fit together

<div class="diagram" role="img" aria-label="The governing stack. The One Principle at the top. Below it the Bright Line, which places the obligation, with Layer Decomposition and Determinism setting scope on its left and the Broker discharging the obligation on its right. Under the Bright Line sit its two determinations, Mode of Discharge with the Envelope, and Indication Integrity. Local Sovereignty stands beside the stack as the protective layer that remains when the governed layer fails. Design Basis Layers lies beneath all of them as the analysis the rest is applied in.">
<svg viewBox="0 0 900 560" xmlns="http://www.w3.org/2000/svg" font-family="IBM Plex Mono, Menlo, monospace">
  <rect x="150" y="14" width="600" height="58" rx="6" fill="#FFF4E5" stroke="#B34700" stroke-width="3"/>
  <text x="450" y="40" text-anchor="middle" font-size="17" font-weight="600" fill="#111418">THE ONE PRINCIPLE</text>
  <text x="450" y="61" text-anchor="middle" font-size="13" fill="#111418">human now  IFF  above the line  AND  NOT proven</text>
  <line x1="450" y1="72" x2="450" y2="100" stroke="#111418" stroke-width="2"/>
  <rect x="20" y="100" width="250" height="96" rx="6" fill="#0B3D91"/>
  <text x="145" y="130" text-anchor="middle" font-size="16" font-weight="600" fill="#FFFFFF">FD-LD</text>
  <text x="145" y="153" text-anchor="middle" font-size="13" fill="#FFFFFF">Layer Decomposition</text>
  <text x="145" y="171" text-anchor="middle" font-size="13" fill="#FFFFFF">SCOPE: which components</text>
  <rect x="325" y="100" width="250" height="96" rx="6" fill="#B34700"/>
  <text x="450" y="130" text-anchor="middle" font-size="16" font-weight="600" fill="#FFFFFF">FD-BL</text>
  <text x="450" y="153" text-anchor="middle" font-size="13" fill="#FFFFFF">The Bright Line</text>
  <text x="450" y="171" text-anchor="middle" font-size="13" fill="#FFFFFF">PLACEMENT: which actions</text>
  <rect x="630" y="100" width="250" height="96" rx="6" fill="#0A6B3D"/>
  <text x="755" y="130" text-anchor="middle" font-size="16" font-weight="600" fill="#FFFFFF">FD-BR</text>
  <text x="755" y="153" text-anchor="middle" font-size="13" fill="#FFFFFF">The Broker</text>
  <text x="755" y="171" text-anchor="middle" font-size="13" fill="#FFFFFF">OBLIGATION: who authorizes</text>
  <line x1="270" y1="148" x2="325" y2="148" stroke="#111418" stroke-width="2"/>
  <line x1="575" y1="148" x2="630" y2="148" stroke="#111418" stroke-width="2"/>
  <line x1="390" y1="196" x2="300" y2="236" stroke="#111418" stroke-width="2"/>
  <line x1="510" y1="196" x2="600" y2="236" stroke="#111418" stroke-width="2"/>
  <rect x="150" y="236" width="270" height="86" rx="6" fill="#FFFFFF" stroke="#111418" stroke-width="2.5"/>
  <text x="285" y="264" text-anchor="middle" font-size="15" font-weight="600" fill="#111418">FD-BL-D1</text>
  <text x="285" y="285" text-anchor="middle" font-size="13" fill="#111418">Mode of Discharge</text>
  <text x="285" y="304" text-anchor="middle" font-size="12" fill="#3D4550">in the moment, or in advance</text>
  <rect x="480" y="236" width="270" height="86" rx="6" fill="#FFFFFF" stroke="#111418" stroke-width="2.5"/>
  <text x="615" y="264" text-anchor="middle" font-size="15" font-weight="600" fill="#111418">FD-BL-D2</text>
  <text x="615" y="285" text-anchor="middle" font-size="13" fill="#111418">Indication Integrity</text>
  <text x="615" y="304" text-anchor="middle" font-size="12" fill="#3D4550">a trustworthy basis to authorize on</text>
  <line x1="285" y1="322" x2="285" y2="350" stroke="#111418" stroke-width="2"/>
  <rect x="150" y="350" width="270" height="70" rx="6" fill="#FFFFFF" stroke="#0B3D91" stroke-width="2.5" stroke-dasharray="7 4"/>
  <text x="285" y="375" text-anchor="middle" font-size="15" font-weight="600" fill="#0B3D91">FD-EV</text>
  <text x="285" y="396" text-anchor="middle" font-size="13" fill="#111418">The Envelope</text>
  <text x="285" y="413" text-anchor="middle" font-size="12" fill="#3D4550">what is pre-authorized</text>
  <rect x="640" y="350" width="240" height="70" rx="6" fill="#4A1F6E"/>
  <text x="760" y="377" text-anchor="middle" font-size="15" font-weight="600" fill="#FFFFFF">FD-LS</text>
  <text x="760" y="399" text-anchor="middle" font-size="13" fill="#FFFFFF">Local Sovereignty</text>
  <text x="760" y="440" text-anchor="middle" font-size="12" fill="#3D4550">the protection that remains</text>
  <text x="760" y="456" text-anchor="middle" font-size="12" fill="#3D4550">when the governed layer fails</text>
  <rect x="20" y="474" width="860" height="72" rx="6" fill="#111418"/>
  <text x="450" y="502" text-anchor="middle" font-size="16" font-weight="600" fill="#FFD60A">FD-DBL · Design Basis Layers</text>
  <text x="450" y="526" text-anchor="middle" font-size="13" fill="#FFFFFF">the analysis everything above is applied in: Design Basis → accident → adversary</text>
</svg>
</div>

The three boxes across the middle answer three separate questions, and no one of them answers another (*Layer Decomposition and Determinism* §4.4). **Scope** asks which components are analyzed at all. **Placement** asks where the line falls for each of their actions. **The obligation** asks who authorizes an action above the line. The two determinations settle how the obligation may be discharged and what an authorization may rest on. The Envelope reserves the word for the thing that is authorized in advance. Local Sovereignty describes the protective functions that remain when everything governed fails, and it does not decide placement. Design Basis Layers lies underneath: it says what the facility is for, and what success means once an adversary is in the analysis.

## Where to go next

Start with [How to read the notation](#/how-to-read) if the symbols are unfamiliar. Each instrument page then gives what the instrument is, why it matters, its formal statement with each term explained, the definition as issued, and its relations to the others. [The sixteen sectors](#/sectors) shows the same definitions at work in each of the sixteen critical-infrastructure sectors. [Cite this](#/cite) gives the DOIs.
