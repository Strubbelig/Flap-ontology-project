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

# ── Perforator flap axioms ────────
PERFORATOR_VESSEL_OF  = OFL.OFLID120000   # Perforator vessel of (new object property)  
PERFORATOR_VESSEL_CLS = OFL.OFLID106012      # Perforator vessel class  
SEGMENT_ARTERIAL_TREE = OBO.FMA_86187          # Segment of arterial tree organ  
SEGMENT_VENOUS_TREE   = OBO.FMA_86188         # Segment of venous tree organ  
