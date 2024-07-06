from biocypher_metta.adapters.ontologies_adapter import OntologyAdapter


class ExperimentalFactorOntologyAdapter(OntologyAdapter):
    ONTOLOGIES = {
        'efo': 'http://www.ebi.ac.uk/efo/efo.owl'
    }

    def __init__(self, write_properties, add_provenance, ontology, type, label='efo', dry_run=False):
        super(ExperimentalFactorOntologyAdapter, self).__init__(write_properties, add_provenance, ontology, type, label, dry_run)

    def get_ontology_source(self):
        """
        Returns the source and source URL for the Gene Ontology.
        """
        return 'efo Ontology', 'http://www.ebi.ac.uk/efo/efo.owl'
