# Architecture

**Primary skill:** `d-design-product-architecture`

ARCH-001 is approved and Complete. Read [architecture.md](architecture.md) for the arc42 narrative, developer CLI decision, capability coverage, validation, and approval record.

- [CLI Application](containers/cli-application/architecture.md): the single internal container.
- [Canonical Structurizr model](diagrams/workspace.dsl): System Context (`SystemContext`) and Container (`Containers`) views.
- [Viewer configuration](diagrams/docker-compose.yml): Docker Compose documentation viewer; see root narrative for start/stop instructions.
- [ADR index](adr/README.md): rationale for retaining no standalone ADRs.

No Component, Dynamic, or Deployment views are needed for this baseline. No images are exported. Structurizr runtime files are excluded by `diagrams/.gitignore`.
