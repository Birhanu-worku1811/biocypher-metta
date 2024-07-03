from biocypher_metta.adapters.ontologies_adapter import OntologyAdapter


class BtoOntologyAdapter(OntologyAdapter):
    ONTOLOGIES = {
        'bto': 'http://purl.obolibrary.org/obo/bto.owl'
    }

    def __init__(self, write_properties, add_provenance, ontology, type, label='bto', dry_run=False):
        super(BtoOntologyAdapter, self).__init__(write_properties, add_provenance, ontology, type, label, dry_run)

    def get_ontology_source(self):
        """
        Returns the source and source URL for the Gene Ontology.
        """
        return 'BTO Ontology', 'http://purl.obolibrary.org/obo/bto.owl'
