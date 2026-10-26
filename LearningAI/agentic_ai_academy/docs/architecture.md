# Reference architecture

## Core boundaries
1. API layer: authenticates caller and validates request.
2. Orchestrator: owns state, plan, budget and termination.
3. Model adapter: converts context into provider-specific request.
4. Tool gateway: enforces schemas, scopes, timeouts and approvals.
5. Storage: checkpoints, controlled memory, immutable audit events.
6. Evaluation: validates results and maintains regression cases.
7. Human review: authorizes high-impact operations with action-specific approvals.

## Agent decision loop
Input → policy validation → propose step → authorize → execute → observe → checkpoint → verify/continue.

## Failure semantics
- Recoverable: rate limit, temporary connection failure. Retry with bounded delay.
- Nonrecoverable: bad credentials, policy denial, invalid schema. Stop and escalate.
- Side effects: never retry without an idempotency strategy.
- Interrupted workflow: resume from durable checkpoint; reconcile effects before repeating.
