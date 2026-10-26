# Jira-to-production AI Software Factory — staged blueprint

1. Intake: read Jira issue using scoped credentials and pin issue revision.
2. Analysis: extract acceptance criteria and identify unknowns.
3. Design: propose architecture and impacted code paths; human design review.
4. Plan: dependency DAG and estimated tool/model budgets.
5. Implement: read-only repo analysis followed by changes in an isolated branch/workspace.
6. Validate: formatting, static checks, unit and integration tests.
7. Secure: secrets scan, dependency scan, authorization review.
8. Review: generate diff summary, provenance, failure list and draft PR.
9. Merge: protected branch policy and human/code-owner approval.
10. Release: deployment plan, migration strategy and separate privileged approval.
11. Monitor: metrics, rollback triggers, incident escalation and feedback into evaluations.

## Critical controls
No agent should silently merge, publish packages, access production secrets or deploy without the configured human approvals and access controls. Treat issue text, source comments, commit messages, tool output and external pages as untrusted content.

## Suggested domain models
Task(id, issue_revision, owner, status, budget)
Action(id, task_id, kind, args_digest, approval_status)
Checkpoint(task_id, state_version, state_blob, created_at)
RunEvent(trace_id, step_id, actor, kind, result_status)
Review(task_id, patch_digest, reviewer_id, decision)
Release(change_id, artifact_digest, approval_id, outcome)
