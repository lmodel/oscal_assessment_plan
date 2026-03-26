# About oscal_assessment_plan

OSCAL Assessment Plan Model: LinkML Schema

## References

- [Oscal Assessment Plan Model](https://pages.nist.gov/OSCAL-Reference/release-assets/latest/oscal_assessment-plan_schema.json)

## Notes on just test

The intended layout is:

Directory	Keys	       Used by
valid	    underscored	   yaml_loader pytest tests
invalid	    underscored	   yaml_loader pytest tests (invalid object loading)
valid	    hyphenated	   linkml-run-examples valid examples
invalid  	hyphenated	   linkml-run-examples counter-examples

The justfile _test-examples recipe currently points --input-directory at valid and --counter-example-input-directory at invalid — both of which use underscored keys. It should instead point at the problem/ subdirectories

The problem/ directory is designed for data that the current toolchain can't handle yet — not for linkml-run-examples. The files we created there with native OSCAL hyphenated keys are a good fit for documenting that limitation.
