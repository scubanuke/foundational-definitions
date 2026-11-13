# The Sixteen Sectors

<p class="lede">The Foundational Definitions are defined once and applied everywhere. A sector framework may express them in its own vocabulary and apply them to its own actions. It may not vary the placement criterion, the granularity, the scope or the obligation. A sector guide may raise the Bright Line but never lower it.</p>

Each example below is drawn from a use case or worked example already in the corpus, and each shows one or two of the definitions doing work. These are illustrative readings written for this site. The sector's own framework, facility class and use case govern, and each is cited by designator so that you can go to it. The point to watch for is the same in every sector: **placement is made action by action, on consequence, and never by component.**

<table>
<tr><th>Sector</th><th>Drawn from</th><th>The definitions at work</th></tr>
<tr><td>Chemical</td><td>DBA-CHEM-UC-5</td><td>Scope, Indication Integrity</td></tr>
<tr><td>Commercial Facilities</td><td>DBA-CF-UC-1</td><td>Placement, Design Basis Layers</td></tr>
<tr><td>Communications</td><td>DBA-COMM-UC-1</td><td>Placement by state, Indication Integrity</td></tr>
<tr><td>Critical Manufacturing</td><td>DBA-CM-UC-1</td><td>Placement of an allocation</td></tr>
<tr><td>Dams</td><td>DBA-DAMS-UC-2</td><td>Placement, Indication Integrity</td></tr>
<tr><td>Defense Industrial Base</td><td>DBA-DIB-UC-1</td><td>Placement on the confidentiality axis</td></tr>
<tr><td>Emergency Services</td><td>DBA-ESS-UC-2</td><td>Mode of Discharge, the envelope</td></tr>
<tr><td>Energy</td><td>Balancing the Daily Use Curve (Analyst’s WorkBench)</td><td>Mode of Discharge, The Broker</td></tr>
<tr><td>Financial Services</td><td>DBA-FIN-UC-1</td><td>Placement, Indication Integrity</td></tr>
<tr><td>Food and Agriculture</td><td>DBA-FA-UC-1</td><td>One action: recommendation and acceptance</td></tr>
<tr><td>Government Facilities</td><td>DBA-GF-UC-1</td><td>The Broker, Design Basis Layers</td></tr>
<tr><td>Healthcare and Public Health</td><td>DBA-HPH-UC-1</td><td>One action, Indication Integrity</td></tr>
<tr><td>Information Technology</td><td>DBA-IT-UC-1</td><td>The vendor’s release</td></tr>
<tr><td>Nuclear Reactors, Materials and Waste</td><td>The Bright Line §4.5; the nuclear system-engineer support example</td><td>Scope versus placement</td></tr>
<tr><td>Transportation Systems</td><td>DBA-TRAN-UC-4</td><td>Design Basis Layers, an independent layer</td></tr>
<tr><td>Water and Wastewater Systems</td><td>DBA-W-UC-1</td><td>Placement, Indication Integrity</td></tr>
</table>

## Chemical

*The Safety System Defeated Without a Trip* (DBA-CHEM-UC-5) runs forward what the TRITON attack would have done had its code not failed. The safety system is reprogrammed not to trip, and the process is driven toward its unsafe limit while the operators see normal readings. An anomaly-detection or state-estimation model that meets the carve-out needs no Command Broker while its inputs stay in range. That is an exemption of **scope, not placement** ([*Layer Decomposition and Determinism* §4.3](#/fd-ld)). But it reads the same instruments the adversary has blinded, so it reports the plant healthy as faithfully as the screens do. Where its output could ground an authorization, [*Indication Integrity*](#/fd-bl-d2) requires a confirming path that no single cause, chosen or not, can corrupt along with it.

## Commercial Facilities

*The Refuge Struck* (DBA-CF-UC-1) strikes a venue in its disaster-support role, while it shelters people displaced by the conflict, and denies the power, water and transport that sustain and would evacuate them. The use case states three governing points, each placed on its consequence, action by action, and none by component. The scenario also shows [*Design Basis Layers*](#/fd-dbl) at work. A venue's function changes when it becomes a refuge, and success at the adversary layer means holding a protected state with what is on site, not waiting for a response that denial may stop from arriving.

## Communications

*Coordinated Severance of a Region's Paths with Repair Denied* (DBA-COMM-UC-1) shows that **the same kind of action places differently as the state changes**. Early in the scenario, a traffic-engineering controller within scope moves a circuit between paths with spare capacity. That move cannot reach the surviving service and is below the line. Later, the same kind of move onto an inland route near capacity can leave the region with less than its surviving service. It is above the line, and it needs Command Broker authorization the control system cannot bypass ([*The Bright Line* §4.2, §4.3](#/fd-bl)). A fault-location model's output makes no change of its own and is below the line. It carries the obligation of [*Indication Integrity*](#/fd-bl-d2) wherever it grounds the decision to take a path out of service.

## Critical Manufacturing

*The Asset and Its Replacement Struck Together* (DBA-CM-UC-1) destroys a sector's installed long-lead assets and, in the same campaign, the capacity to replace them. Where a system within scope allocates the plants' output or the reserve's spares among waiting facilities, **each allocation is an action**, placed on the consequence of the delay it imposes on the facilities it does not serve first. An allocation whose consequence can reach the threshold needs the authorization of the qualified human the coordination class names as Command Broker, given on a basis the system cannot alter.

## Dams

*Gates Opened at High Pool Behind Normal Readings* (DBA-DAMS-UC-2) runs forward what the Bowman Avenue intrusion would have done had the gate been connected. Where an automated gate-scheduling system within scope issues a command, each command is placed on its consequence. A command that could release a flood reaching the endpoint downstream is above the line. Whether it can depends on the pool and the river, so placement by consequence needs a sound basis. In the scenario's second form a falsified reading leads operators to hold the gates closed while the reservoir rises. That is the confident-and-wrong authorization [*Indication Integrity*](#/fd-bl-d2) exists to prevent.

## Defense Industrial Base

*Production Struck at Depth* (DBA-DIB-UC-1) joins a campaign against defense production to a compromise made before the conflict. Its first governing point is the release of data. Where a system within scope sends a file to a supplier, answers a query or passes data to a model outside the facility's control, **each release is an action placed on the consequence of the release**. On the confidentiality axis, that consequence is the compromise scope of what is released, and it cannot be undone. A release that can reach the threshold needs Command Broker authorization before it goes.

## Emergency Services

*Dispatch Corrupted, Not Encrypted, During a Primary Attack* (DBA-ESS-UC-2) tests [*Mode of Discharge*](#/fd-bl-d1). An automatic dispatch for a call type whose error cannot reach the threshold may sit below the line. A recommendation for a structure fire or a cardiac arrest, accepted with one keystroke, is above it, and recommendation and acceptance are one action. Each was authorized in advance under a pre-authorized envelope. Advance discharge is valid only while the gatekeeper admits each action against measured unit status, location and capability, on inputs that satisfy [*Indication Integrity*](#/fd-bl-d2). The act of restoring automation afterwards re-enables advance discharge on whatever envelope the restored system holds, so **it is above the line on its own consequence**.

## Energy

*Balancing the Daily Use Curve* (Analyst's WorkBench, use case V5) is the corpus's fullest example of advance discharge. A generative assistant supports a balancing-authority operator through a weather event. In decision-support mode it recommends and the operator acts. In conditional autonomous mode it proposes, and a separate deterministic, formally verified gatekeeper in the energy management system admits each operation only inside a pre-authorized envelope for one circuit set. The assistant can neither modify nor bypass the gatekeeper. The Chief Reliability Engineer, holding the advance-mode endorsement, is the Command Broker discharging in advance. The months of engineering that produced the proof authorized nothing; the Broker's acceptance did ([*The Broker* §4.2](#/fd-br)).

## Financial Services

*Settlement Through a Campaign on the Grid and Communications* (DBA-FIN-UC-1) is illustrated by a systemic bank. A treasury agent within scope composes routine payments, and releases above the bank's threshold wait for a qualified human, the Command Broker. The bank reconciles what its endpoint sent against what it intended, by a path independent of the system that composed it. That is the corroboration [*Indication Integrity*](#/fd-bl-d2) I3 requires, applied to a payment.

## Food and Agriculture

*Deliberate Contamination at the Processing Chokepoint With Detection Denied* (DBA-FA-UC-1) applies the rule that **a recommendation and its acceptance are one action** ([*The Bright Line* §4.3](#/fd-bl)). Where a system within scope recommends the release of a lot, the recommendation and its acceptance are placed together on the consequence of the release, which is set by the exposed population. For a plant whose release reaches a metropolitan population, that consequence meets the threshold. The release needs the food-safety officer's authorization, on a basis the system cannot alter. The same use case raised the question the November Edition answered: a correct indication can still be insufficient.

## Government Facilities

*The Seat Struck During the Conflict* (DBA-GF-UC-1) strikes seats of government when the people who decide are present, and attacks the enterprise systems and records the government would move and act on. In a class whose substance is the continuity of governing authority, the Command Broker is the qualified human the coordination class names. The architecture requires that person's authorization before any action a component within scope proposes, and whose consequence reaches the threshold, can execute. [*The Broker*](#/fd-br) is a role, so it survives the loss of particular people only if the class names who holds it next.

## Healthcare and Public Health

*A Mass-Casualty Surge During a Grid and Communications Outage* (DBA-HPH-UC-1) starts with triage. Where a system within scope scores the injured for their place in the queue for definitive care, each score is an action placed on the consequence of the delay it can impose. Where a clinician accepts it with a single keystroke, the score and the acceptance are one action. In the scenario the shared record is unreachable, so a score that draws on it is computed from incomplete inputs. That is where [*Indication Integrity*](#/fd-bl-d2) bites, and where its sufficiency rule asks what is missing before the score is relied on.

## Information Technology

*A Capability Pre-Positioned in a Trusted Product and Activated During an Attack on the Grid* (DBA-IT-UC-1) is the case behind a November change to [*The Bright Line* §4.3](#/fd-bl). A vendor's release to hosts outside any one facility is not, by itself, a Bright Line action of the vendor. Its controls are obligations the asset owner-operator places on the vendor by contract. At the facility, taking the release in is an action placed on its consequence that comes in only through a governed act. Each widening of a staged release is its own action, and the first ring is placed on the whole planned reach.

## Nuclear Reactors, Materials and Waste

The plainest example of **scope versus placement** comes from nuclear. A reactor trip or an engineered-safety-feature actuation performs an action of the highest consequence with no Command Broker. It is not below the line, and saying so would be false. It is outside the obligation by the carve-out, because a deterministic protective function's behavior is bounded by proof ([*The Bright Line* §4.5](#/fd-bl); [*Layer Decomposition and Determinism* §4.3](#/fd-ld)). A generative support tool for a plant system engineer sits on the other side of the same rule. Its assessment output makes no change of its own and is below the line, carrying the indication-integrity obligation. The maintenance work orders it drafts on safety-related equipment, and the test executions against Technical Specifications, are above the line on their consequence. The nuclear sector framework, DBA-NUC-SF, is in preparation.

## Transportation Systems

*Denial of the Control Plane During a Deployment* (DBA-TRAN-UC-4) tests a class with a sharp asymmetry: a stop is safe and a proceed is dangerous. An adversary who denies the control plane pushes the system toward the wrong grant. The use case requires that every proceed be enforced by a layer whose basis is independent of the grant. This is the adversary layer's precision and denial ([*Design Basis Layers* §4.4](#/fd-dbl)) met by independence, the same question [*Indication Integrity*](#/fd-bl-d2) and [*Local Sovereignty*](#/fd-ls) ask: can anything the adversary reaches affect both paths?

## Water and Wastewater Systems

*Area-Denial Attack on a Large Surface-Water Treatment Plant* (DBA-W-UC-1) shows the two AI-governance requirements working as a pair. If an automated or generative component of dosing control can move the disinfection setpoint on its own authority, the adversary's cleanest path is to induce it to make the move. A change that can drive the disinfection setpoint out of band is above the Bright Line on its own consequence, and the Command Broker's authorization forecloses that path. But the authorization is only as good as the picture shown. Where the displayed residual is falsified, [*Indication Integrity*](#/fd-bl-d2) is what lets the operator refuse to trust it.
