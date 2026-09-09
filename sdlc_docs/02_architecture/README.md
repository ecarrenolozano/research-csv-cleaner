# Architecture

**Primary skill:** `d-design-product-architecture`

ARCH-002 is approved for CR-0001. Read [architecture.md](architecture.md) for the arc42 narrative, local dual-interface decision, capability coverage, validation, and approval record.

- [CLI Application](containers/cli-application/architecture.md): the existing local command-line entry point.
- [Streamlit Interface](containers/streamlit-interface/architecture.md): the new local upload, selection, preview, count, and download interface.
- [Canonical Structurizr model](diagrams/workspace.dsl): System Context (`SystemContext`) and Container (`Containers`) views.
- [Viewer configuration](diagrams/docker-compose.yml): Docker Compose documentation viewer; see root narrative for start/stop instructions.
- [ADR index](adr/README.md): architecture decision records for material choices.

No Component, Dynamic, or Deployment views are needed for this baseline. No images are exported. Structurizr runtime files are excluded by `diagrams/.gitignore`.
