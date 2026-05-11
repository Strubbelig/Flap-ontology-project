"""
OFL vocabulary constants — namespaces, class IRIs, and property IRIs.

Import from here rather than hard-coding OFL IRIs in generator classes.
"""
from rdflib import Namespace, URIRef

OFL     = Namespace("https://purl.bioontology.org/ontology/OFL/")
OBO     = Namespace("http://purl.obolibrary.org/obo/")
FMA     = Namespace("http://purl.obolibrary.org/obo/FMA_")
DCTERMS = Namespace("http://purl.org/dc/terms/")

# ── Ontology roots ────────────────────────────────────────────────────────────
FLAP_ROOT   = OFL.OFLID10002   # top-level flap class
ORIGIN_ROOT = OFL.OFLID10098   # Flaps classified by region of origin

# ── OFL object properties ─────────────────────────────────────────────────────
HAS_PART   = OFL.OFLID13296
PART_OF    = OFL.OFLID13297
HAS_ORIGIN = OFL.OFLID12003

# ── RO / OBI properties ───────────────────────────────────────────────────────
HAS_PARTICIPANT            = OBO.RO_0000057   # has participant
CONCRETIZES                = OBO.RO_0000059   # concretizes (sdc concretizes gdc)
HAS_FUNCTION               = OBO.RO_0000085   # has function
HAS_QUALITY                = OBO.RO_0000086   # has quality
HAS_ROLE                   = OBO.RO_0000087   # has role
IS_OUTPUT_OF               = OBO.OBI_0000312  # is specified output of
HAS_SPECIFIED_OUTPUT       = OBO.OBI_0000299  # has specified output
REALIZES                   = OBO.RO_0000055   # realizes
EXISTENCE_STARTS_AT_END_OF = OBO.RO_0002230   # existence starts at end of
EXISTENCE_STARTS_DURING    = OBO.RO_0002082   # existence starts during

# ── Modification classes ──────────────────────────────────────────────────────
MOD_NO  = OFL.OFLID10130   # without preharvest modification
MOD_YES = OFL.OFLID10131   # with preharvest modification

# ── Survival outcome classes ──────────────────────────────────────────────────
SURVIVAL_NO_LOSS  = OFL.OFLID10184
SURVIVAL_APEX     = OFL.OFLID10179
SURVIVAL_TOTAL    = OFL.OFLID10183
SURVIVAL_ARTERIAL = OFL.OFLID10180
SURVIVAL_VENOUS   = OFL.OFLID10181

LEAF_SURVIVAL = [SURVIVAL_NO_LOSS, SURVIVAL_APEX, SURVIVAL_TOTAL,
                 SURVIVAL_ARTERIAL, SURVIVAL_VENOUS]
MAIN_SURVIVAL = [SURVIVAL_NO_LOSS, SURVIVAL_APEX, SURVIVAL_TOTAL]

# ── Transfer distance classes ─────────────────────────────────────────────────
LOCAL_FLAP    = OFL.OFLID10134
REGIONAL_FLAP = OFL.OFLID10140
DISTANT_FLAP  = OFL.OFLID10085

# ── Transfer process classes ──────────────────────────────────────────────────
FREE_TRANSFER     = OFL.OFLID1000137
PEDICLED_TRANSFER = OFL.OFLID1000138

# ── Operative process / plan classes ─────────────────────────────────────────
FLAP_HARVEST_PROCESS = OFL.OFLID1000132   # Flap harvest process
COMPLETE_OPERATION   = OFL.OFLID1000128   # Complete flap operation process
FLAP_SURGERY_PLAN    = OFL.OFLID10507     # Flap surgery plan (gdc)

# ── BFO / PATO / NCBITaxon types ─────────────────────────────────────────────
CONC_PLAN_TYPE = OBO.BFO_0000020      # specifically dependent continuant
PATIENT_TYPE   = OBO.NCBITaxon_9606   # Homo sapiens
VOL_TYPE       = OBO.PATO_0001679     # volume

# ── OFL role / function types ─────────────────────────────────────────────────
ROLE_TYPE             = OFL.OFLID106000   # Wound coverage role
MOTOR_FUNC_ROLE_TYPE  = OFL.OFLID106001   # Motor function role
TISSUE_LOSS_ROLE_TYPE = OFL.OFLID106002   # Tissue loss restoration role
FUNC_TYPE             = OFL.OFLID106029   # Oxygenated blood supply to flap function

# ── PATO additional quality types ─────────────────────────────────────────────
MASS_TYPE = OBO.PATO_0000128   # mass

# ── OBI process properties ────────────────────────────────────────────────────
HAS_SPECIFIED_INPUT = OBO.OBI_0000293   # has specified input

# ── RO participation ──────────────────────────────────────────────────────────
PARTICIPATES_IN = OBO.RO_0000056   # participates in

# ── Transfer destination ──────────
FLAP_TRANSFER_PROCESS_CLS = OFL.OFLID1000136           # Flap transfer process  
HAS_TARGET_START_LOCATION = OBO.RO_0002338        # has target start location
HAS_TARGET_END_LOCATION   = OBO.RO_0002339        # has target end location
SUBDIVISION_CARDINAL_BODY = OBO.FMA_67504      # Subdivision of cardinal body part

# ── Anatomical entity ────────────
ANATOMICAL_ENT_TYPE = OBO.FMA_62955 # anatomical entity

# ── Perforator flap axioms ────────────────────────────────────────────────────
PERFORATOR_VESSEL_OF  = OFL.OFLID120000   # Perforator vessel of (new object property)
PERFORATOR_VESSEL_CLS = OFL.OFLID106012   # Perforator vessel class
SEGMENT_ARTERIAL_TREE = OBO.FMA_86187     # Segment of arterial tree organ
SEGMENT_VENOUS_TREE   = OBO.FMA_86188     # Segment of venous tree organ

# ── Anastomosis result classes (CQ16) ────────────────────────────────────────
# OFLID1000170 subtypes are explicitly asserted in the ABox because the
# vessel-type subclasses (1000172/73) use allValuesFrom which OWL RL does not
# use for individual classification; configuration subclasses (1000176-78)
# are primitive (no equivalentClass), so they also cannot be auto-inferred.
CONNECTS         = OBO.RO_0002176     # connects (RO:connects, links anastomosis to vessel)
ANASTOMOSIS_BASE = OFL.OFLID1000170  # Surgically produced vessel anastomosis (root)
ANASTOMOSIS_ART  = OFL.OFLID1000172  # Arterial anastomosis
ANASTOMOSIS_VEN  = OFL.OFLID1000173  # Venous anastomosis
ANASTOMOSIS_AV   = OFL.OFLID1000174  # Arteriovenous anastomosis
ANASTOMOSIS_ETE  = OFL.OFLID1000176  # End-to-end anastomosis (configuration)
ANASTOMOSIS_ETS  = OFL.OFLID1000177  # End-to-side anastomosis (configuration)
ANASTOMOSIS_STS  = OFL.OFLID1000178  # Side-to-side anastomosis (configuration)

ANASTOMOSIS_VESSEL_TYPES = [ANASTOMOSIS_ART, ANASTOMOSIS_VEN, ANASTOMOSIS_AV]
ANASTOMOSIS_CONFIGS      = [ANASTOMOSIS_ETE, ANASTOMOSIS_ETS, ANASTOMOSIS_STS]

# ── Chimeric flap subtype classes (CQ9) ──────────────────────────────────────
# Subtypes of OFLID1000093 are primitive (no equivalentClass), so they must
# be explicitly asserted in the ABox.  OFLID1000092 (Chimeric flaps) IS a
# defined class (equivalentClass: Surgical flap AND hasPart some Surgical flap)
# and will be auto-inferred by OWL RL once the has-part relation is asserted.
CHIMERIC_TYPE_I   = OFL.OFLID1000094  # Type i:   classical chimerism
CHIMERIC_TYPE_II  = OFL.OFLID1000097  # Type ii:  anastomotic chimerism
CHIMERIC_TYPE_III = OFL.OFLID1000100  # Type iii: perforator chimerism
CHIMERIC_TYPE_IV  = OFL.OFLID1000103  # Type iv:  mixed chimerism
CHIMERIC_TYPES    = [CHIMERIC_TYPE_I, CHIMERIC_TYPE_II, CHIMERIC_TYPE_III, CHIMERIC_TYPE_IV]

# ── Has flap destination ──────────────────────────────────────────────────────
# Derived via property chain (participates_in ∘ has_target_end_location_of) but
# also asserted explicitly for direct queryability without reasoning.
HAS_FLAP_DESTINATION = OFL.OFLID12004

# ── Tissue topology ───────────────────────────────────────────────────────────
CONTINUOUS_WITH       = OBO.RO_0002150   # continuous with (RO)
FMA_TISSUE            = OBO.FMA_67135    # FMA tissue class

FLAP_TISSUE_ROLE      = OFL.OFLID120027  # Flap tissue role
SOURCE_TISSUE_ROLE    = OFL.OFLID120026  # Source tissue role
RECIPIENT_TISSUE_ROLE = OFL.OFLID120028  # Recipient tissue role

# ── Pedicle / recipient vessel roles ─────────────────────────────────────────
# OFLID120023 (Flap pedicle vessel)  = defined: vessel AND HAS_ROLE some OFLID120017
# OFLID120024 (Recipient vessel)     = defined: vessel AND HAS_ROLE some OFLID120018
# Both roles must be asserted on separate role individuals so OWL RL can infer
# the vessel subtypes, and then infer OFLID120014 (Flap pedicle vessel to
# recipient vessel anastomosis) when an anastomosis CONNECTS both.
PEDICLE_VESSEL_ROLE   = OFL.OFLID120017
RECIPIENT_VESSEL_ROLE = OFL.OFLID120018

# ── Survival-related process types ───────────────────────────────────────────
NECROTIC_PROCESS_CLS = OFL.OFLID120039  # Necrotic process
VESSEL_OCCLUSION_CLS = OFL.OFLID120045  # Vessel occlusion process

# ── Surgical vessel anastomosis process ──────────────────────────────────────
# OFLID120019 (Flap vessel anastomosis process) is defined as
# OFLID106031 AND (part_of some OFLID1000128).  Asserting an OFLID106031
# individual as part of the operation lets OWL RL infer OFLID120019.
ANASTOMOSIS_PROCESS_CLS = OFL.OFLID106031

# ── CQ11: Movement-type transfer process classes ─────────────────────────────
# OFLID10068 (Flaps classified by movement) = OFLID10002 AND
#   (participates_in some (OFLID1000128 AND (has_part some OFLID1000138))).
# Its three subclasses each add a further participates_in restriction:
#   OFLID10014 (Rotation)     + participates_in some OFLID120025
#   OFLID10067 (Transposition)+ participates_in some OFLID120057
#   OFLID10070 (Advancement)  + participates_in some OFLID120056
# All three movement classes are subClassOf OFLID1000138 (PEDICLED_TRANSFER),
# so typing transfer_id with one of them lets OWL RL infer PEDICLED_TRANSFER
# upward AND satisfies the participates_in restriction for the specific subclass.
MOVEMENT_ROTATION     = OFL.OFLID120025  # Pedicled flap transfer process with rotational component
MOVEMENT_ADVANCEMENT  = OFL.OFLID120056  # Pedicled flap transfer process with advancement component
MOVEMENT_TRANSPOSITION = OFL.OFLID120057  # Superficial transfer of the pedicled flap with lifting
PEDICLED_MOVEMENTS    = [MOVEMENT_ROTATION, MOVEMENT_ADVANCEMENT, MOVEMENT_TRANSPOSITION]

# ── CQ13: Insertion site preparation ─────────────────────────────────────────
# OFLID130001 (Flaps classified by insertion site preparation) is defined as
# OFLID10002 AND (participates_in some (OFLID1000128 AND (has_part some OFLID120048))).
# Asserting an OFLID120048 individual as part of the complete operation
# satisfies the nested restriction, letting OWL RL infer OFLID130001.
PREINSERTION_TREATMENT_CLS = OFL.OFLID120048  # Preinsertion treatment of the flap recipient site

# ── CQ15: Skin graft ──────────────────────────────────────────────────────────
# OFLID120066 (Flaps with skin graft) is defined as
# OFLID120065 AND (OFLID12002 someValuesFrom (OFLID10702 AND (RO_0000057 someValuesFrom OFLID106021))).
# OFLID12002 is the object property "target end location of":
#   assert (flap_id, OFLID12002, graft_transfer_id) so OWL RL evaluates the
#   someValuesFrom restriction directly on the flap individual.
GRAFT_TRANSFER_CLS     = OFL.OFLID10702   # Graft transfer process
SKIN_GRAFT_CLS         = OFL.OFLID106021  # Skin graft
TARGET_END_LOCATION_OF = OFL.OFLID12002   # target end location of (object property)

# ── CQ16: Anastomosis technique classes (OFLID10223 subclasses) ───────────────
# OFLID10223 (Flaps classified by technique of vessel anastomosis) is a
# primitive class; its subclasses are also primitive — they cannot be inferred
# and must be explicitly asserted on free flap instances.
ANASTOMOSIS_SUTURED    = OFL.OFLID10233  # Flaps with sutured vessel anastomosis
ANASTOMOSIS_COUPLED    = OFL.OFLID10235  # Flaps with coupled vessel anastomosis
ANASTOMOSIS_TECHNIQUES = [ANASTOMOSIS_SUTURED, ANASTOMOSIS_COUPLED]
