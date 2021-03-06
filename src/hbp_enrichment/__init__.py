# -*- coding: utf-8 -*-

"""This script converts the curation sheets to BEL."""

import os

import neurommsig_knowledge
from bel_enrichment import BELSheetsRepository
from bel_repository import BELMetadata
from bel_repository.utils import serialize_authors

__all__ = [
    'AUTHORS',
    'metadata',
    'repository',
    'main',
]

AUTHORS = [
    'Charles Tapley Hoyt',
    'Daniel Domingo-Fernández',
    'Esther Wollert',
    'Sandra Spalek',
    'Keerthika Lohanadan',
    'Rana Al Disi',
    'Lingling Xu',
    'Kristian Kolpeja',
]

AUTHOR_STRING = serialize_authors(AUTHORS)

# Folder pointers
HERE = os.path.abspath(os.path.dirname(__file__))
ROUNDS_DIRECTORY = os.path.join(HERE, 'rounds')
DATA_DIRECTORY = os.path.join(HERE, 'data')
VERSION = '0.1.0'

metadata = BELMetadata(
    name='HBP - INDRA Curation',
    version=VERSION,
    description="This knowledge graph contains content generated by the rational enrichment approach described by "
                "Hoyt et al. (2019) applied to the NeuroMMSig inventory.",
    authors=AUTHOR_STRING,
    contact='charles.hoyt@scai.fraunhofer.de',
    license='CC BY 4.0',
)

repository = BELSheetsRepository(
    directory=ROUNDS_DIRECTORY,
    output_directory=DATA_DIRECTORY,
    metadata=metadata,
    prior=neurommsig_knowledge.repository,
)

main = repository.build_cli()

if __name__ == '__main__':
    main()
