## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Patch linkml_runtime bugs in the generated Python datamodel.
# Issues and PR fixes raised upstream for these workarounds:
#
# Issue 1 (linkml#3316): gen-python emits Python reserved keywords verbatim.
#   Workaround: slot is named _class (no alias:) so gen-python emits _class natively.
#
# Issue 2 (linkml-runtime): _normalize_inlined_as_list calls slot_type(json_obj)
#   positionally for single-field inlined list entries instead of slot_type(**as_dict(json_obj)).
#   Affected slots: guidelines (ParameterGuideline.prose), rlinks (ResourceLink.href),
#   related_observations (RelatedObservation.observation_uuid).
fix-python-keywords:
    # Step 1: Convert hyphenated key_name values to underscored Python attribute names
    # (must run before step 2 so sed patterns can match the underscored forms)
    uv run python scripts/fix_key_names.py {{pymodel}}/{{schema_name}}.py
    # Step 2: Patch _normalize_inlined_as_list calls that fail for single-key inlined entries
    sed -i \
        -e 's|self._normalize_inlined_as_list(slot_name="guidelines", slot_type=ParameterGuideline, key_name="prose", keyed=False)|if self.guidelines is not None:\n            self.guidelines = [g if isinstance(g, ParameterGuideline) else ParameterGuideline(**as_dict(g)) if isinstance(g, (dict, JsonObj)) else ParameterGuideline(prose=str(g)) for g in (self.guidelines if isinstance(self.guidelines, list) else [self.guidelines])]|g' \
        -e 's|self._normalize_inlined_as_list(slot_name="rlinks", slot_type=ResourceLink, key_name="href", keyed=False)|if self.rlinks is not None:\n            self.rlinks = [r if isinstance(r, ResourceLink) else ResourceLink(**as_dict(r)) if isinstance(r, (dict, JsonObj)) else ResourceLink(href=str(r)) for r in (self.rlinks if isinstance(self.rlinks, list) else [self.rlinks])]|g' \
        -e 's|self._normalize_inlined_as_list(slot_name="related_observations", slot_type=RelatedObservation, key_name="observation_uuid", keyed=False)|if self.related_observations is not None:\n            self.related_observations = [r if isinstance(r, RelatedObservation) else RelatedObservation(**as_dict(r)) if isinstance(r, (dict, JsonObj)) else RelatedObservation(observation_uuid=str(r)) for r in (self.related_observations if isinstance(self.related_observations, list) else [self.related_observations])]|g' \
        {{pymodel}}/{{schema_name}}.py
