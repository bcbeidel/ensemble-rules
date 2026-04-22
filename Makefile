# ensemble-rules one-shot runs, one topic per target.
#
# Sources .env at parse time; does not assume the caller has exported
# provider credentials. Remaps GOOGLE_ADC_CREDENTIAL_PATH → the
# LiteLLM-expected GOOGLE_APPLICATION_CREDENTIALS, and pins the Vertex
# project/location below.
#
# Usage:
#   make help            # list all targets
#   make agent-rules     # run one topic end-to-end
#
# Each run issues 8 API calls (6 panel elicitations + synthesis +
# LLM-judged coverage) and typically takes 60–120s.

SHELL := /bin/bash

-include .env
export

export GOOGLE_APPLICATION_CREDENTIALS := $(GOOGLE_ADC_CREDENTIAL_PATH)
export VERTEXAI_PROJECT := rv-rvgt-sandbox
export VERTEXAI_LOCATION := us-central1

ENSEMBLE := .venv/bin/ensemble-rules

.PHONY: help
help:
	@echo "ensemble-rules topic targets"
	@echo
	@echo "AI / agent artifacts:"
	@echo "  make agent-rules         Agent rule files (.claude/rules/*.md, path-scoped instructions)"
	@echo "  make agent-skills        Agent skills (SKILL.md reusable capabilities)"
	@echo "  make subagents           Claude Code custom subagent definitions"
	@echo "  make slash-commands      Claude Code slash commands"
	@echo "  make agentic-hooks       Claude Code hooks (PreToolUse/PostToolUse/etc.)"
	@echo "  make claude-md           CLAUDE.md / AGENTS.md project memory files"
	@echo "  make mcp-servers         MCP (Model Context Protocol) servers"
	@echo "  make llm-evals           LLM evaluation suites"
	@echo "  make prompts             LLM prompts"
	@echo
	@echo "CI / automation:"
	@echo "  make github-actions      GitHub Actions workflows"
	@echo "  make precommit-hooks     pre-commit framework hooks"
	@echo "  make makefile            Makefile targets"
	@echo
	@echo "Scripts / infra:"
	@echo "  make bash-scripts        Bash / POSIX shell scripts"
	@echo "  make python-scripts      Standalone Python scripts"
	@echo "  make dockerfiles         Dockerfiles"
	@echo "  make terraform-modules   Terraform modules"
	@echo "  make dbt-models          dbt SQL models"
	@echo
	@echo "Docs:"
	@echo "  make readme              README.md files"
	@echo "  make pr-templates        GitHub PR / issue templates"
	@echo
	@echo "Each run hits 8 models (6 panel + 2 synthesizer calls) — ~60–120s."

.PHONY: preflight
preflight:
	@test -x $(ENSEMBLE) || { echo "error: $(ENSEMBLE) not found. Run: python -m venv .venv && .venv/bin/pip install -e '.[dev]'"; exit 1; }
	@test -n "$${ANTHROPIC_API_KEY}" || { echo "error: ANTHROPIC_API_KEY not set — check .env"; exit 1; }
	@test -n "$${OPENAI_API_KEY}" || { echo "error: OPENAI_API_KEY not set — check .env"; exit 1; }
	@test -n "$${XAI_API_KEY}" || { echo "error: XAI_API_KEY not set — check .env"; exit 1; }
	@test -f "$${GOOGLE_APPLICATION_CREDENTIALS}" || { echo "error: GOOGLE_APPLICATION_CREDENTIALS not a file: '$${GOOGLE_APPLICATION_CREDENTIALS}' — check .env's GOOGLE_ADC_CREDENTIAL_PATH"; exit 1; }

.PHONY: agent-rules
agent-rules: preflight
	$(ENSEMBLE) run "Agent Rule Files" --description "Path-scoped markdown instruction files (e.g. .claude/rules/*.md with a paths: frontmatter) that AI coding assistants load conditionally based on the files being edited, used to encode project-specific conventions without bloating top-level project memory."

.PHONY: agent-skills
agent-skills: preflight
	$(ENSEMBLE) run "Agent Skills" --description "Reusable, model-invocable capability definitions packaged as SKILL.md files — with a name, description, when-to-use trigger language, and step-by-step instructions — that AI agents load on demand to perform a specific workflow."

.PHONY: subagents
subagents: preflight
	$(ENSEMBLE) run "Claude Code Subagent Definitions" --description "Claude Code custom subagent definitions placed in .claude/agents/*.md — each a specialized agent with its own description, tool allowlist, and system prompt that the main agent delegates specific tasks to."

.PHONY: slash-commands
slash-commands: preflight
	$(ENSEMBLE) run "Claude Code Slash Commands" --description "Claude Code slash commands defined as markdown files in .claude/commands/*.md that users invoke with /<name> to trigger reusable workflows with argument interpolation and optional scripted side effects."

.PHONY: agentic-hooks
agentic-hooks: preflight
	$(ENSEMBLE) run "Claude Code Agentic Hooks" --description "Claude Code hook scripts (configured under the hooks: key in settings.json) that execute in response to agent events — PreToolUse, PostToolUse, UserPromptSubmit, Stop — to enforce quality gates, block unsafe actions, or instrument agent behavior."

.PHONY: claude-md
claude-md: preflight
	$(ENSEMBLE) run "CLAUDE.md Project Memory Files" --description "Top-level CLAUDE.md (or AGENTS.md) project-memory files that document how a repository expects to be worked in — conventions, architectural decisions, key file locations — loaded automatically by AI coding assistants on every session."

.PHONY: mcp-servers
mcp-servers: preflight
	$(ENSEMBLE) run "MCP Servers" --description "Model Context Protocol servers that expose tools, resources, or prompts to AI assistants over stdio or HTTP transports, enabling the assistant to interact with external systems (databases, APIs, filesystems, internal services) through a standardized interface."

.PHONY: llm-evals
llm-evals: preflight
	$(ENSEMBLE) run "LLM Evaluation Suites" --description "Evaluation test suites for LLM applications — prompts, agents, RAG pipelines — covering dataset design, scoring methods (exact match, rubric-based, LLM-as-judge), regression tracking, and cost/latency instrumentation."

.PHONY: prompts
prompts: preflight
	$(ENSEMBLE) run "LLM Prompts" --description "User-facing prompts sent to LLMs for coding assistants, content generation, RAG pipelines, or agentic workflows — treated as durable, version-controlled artifacts with clear goals, constraints, and explicit output-format specifications."

.PHONY: github-actions
github-actions: preflight
	$(ENSEMBLE) run "GitHub Actions Workflows" --description "YAML workflow definitions under .github/workflows/ that run CI/CD jobs (tests, builds, deployments, checks) on GitHub-hosted or self-hosted runners in response to repository events."

.PHONY: precommit-hooks
precommit-hooks: preflight
	$(ENSEMBLE) run "pre-commit Hooks" --description "Git pre-commit hooks (via the pre-commit framework or raw .git/hooks scripts) that run formatters, linters, and validators against staged changes before a commit is recorded."

.PHONY: makefile
makefile: preflight
	$(ENSEMBLE) run "Makefile" --description "Makefile targets used to orchestrate developer workflows (build, test, lint, run, deploy, format) — portable across contributors, self-documenting via a make help target, and a single source of truth for the commands a newcomer needs."

.PHONY: bash-scripts
bash-scripts: preflight
	$(ENSEMBLE) run "Bash Scripts" --description "Bash and POSIX shell scripts used in production ops tooling, CI pipelines, and local developer workflows — where portability across systems, safe error handling, and quoting discipline matter."

.PHONY: python-scripts
python-scripts: preflight
	$(ENSEMBLE) run "Python Scripts" --description "Standalone Python scripts (single-file executables, not packaged libraries) used as CLI tools, automation, and data-wrangling utilities — where shebang discipline, stdlib-first dependencies, argument parsing, and exit codes matter."

.PHONY: dockerfiles
dockerfiles: preflight
	$(ENSEMBLE) run "Dockerfiles" --description "Dockerfiles that define reproducible container builds — base image selection, multi-stage builds, layer caching, security hardening, non-root users, build-arg hygiene, and entrypoint discipline."

.PHONY: terraform-modules
terraform-modules: preflight
	$(ENSEMBLE) run "Terraform Modules" --description "Reusable Terraform modules defining cloud infrastructure — variable naming conventions, output contracts, state layout, versioning strategy, and CI-driven plan/apply workflows."

.PHONY: dbt-models
dbt-models: preflight
	$(ENSEMBLE) run "dbt SQL Models" --description "dbt SQL models defining analytics transformations — layering (staging / intermediate / mart), naming conventions, tests, documentation, materialization choices, and incremental strategies."

.PHONY: readme
readme: preflight
	$(ENSEMBLE) run "README Files" --description "Project README.md files — the first document a visitor reads — covering what the project is and why, prerequisites, how to install and run it, common workflows, and where to go next."

.PHONY: pr-templates
pr-templates: preflight
	$(ENSEMBLE) run "GitHub PR and Issue Templates" --description "GitHub pull-request and issue templates (.github/PULL_REQUEST_TEMPLATE.md, .github/ISSUE_TEMPLATE/*.md) that guide contributors to provide the context reviewers and maintainers need to triage and respond."
