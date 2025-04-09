# 📚 Internals

## Design

To be documented

## SPLE Artifacts Uploader Details

### Requirements

```{item} REQ-ARTIFACTS-UPLOADER-1.0 Upload artifacts
   :status: Done

   The artifacts uploader **shall** upload files to a remote server.
```

### Reports

```{item-matrix} Trace requirements to implementation
    :source: REQ-ARTIFACTS-UPLOADER
    :target: IMPL
    :sourcetitle: Requirement
    :targettitle: Implementation
    :stats:
```

```{item-piechart} Implementation coverage chart
    :id_set: REQ-ARTIFACTS-UPLOADER IMPL
    :label_set: Not implemented, Implemented
    :sourcetype: fulfilled_by
```

```{item-matrix} Requirements to test case description traceability
    :source: REQ-ARTIFACTS-UPLOADER
    :target: "[IU]TEST"
    :sourcetitle: Requirements
    :targettitle: Test cases
    :sourcecolumns: status
    :group: bottom
    :stats:
```

### API

```{eval-rst}
.. autoclass:: sple_artifacts_uploader.artifact_uploader::ArtifactUploader
   :members:
   :undoc-members:
```

## Testing

```{eval-rst}
.. automodule:: test_artifact_uploader
   :members:
   :show-inheritance:
```
