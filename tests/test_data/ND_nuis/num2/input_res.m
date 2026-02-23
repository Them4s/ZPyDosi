
% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.21' ;
TITLE                     (idx, [1: 13])  = 'CROCUS/PETALE' ;
INPUT_FILE_NAME           (idx, [1:  5])  = 'input' ;
START_DATE                (idx, [1: 24])  = 'Thu Jan 15 12:01:17 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Fri Jan 16 07:31:24 2026' ;

% Run parameters:

POP                       (idx, 1)        = 30000 ;
CYCLES                    (idx, 1)        = 6000 ;
SKIP                      (idx, 1)        = 50 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 42 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, [1:  3])  = [ 0 0 0 ];
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 42])  = 'AMD Ryzen Threadripper PRO 5975WX 32-Cores' ;
CPU_MHZ                   (idx, 1)        = 167805455.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 30 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.22835E+00  9.97622E-01  9.96335E-01  9.86170E-01  9.93904E-01  9.89403E-01  9.87371E-01  9.91007E-01  9.81324E-01  9.93997E-01  9.94440E-01  9.82358E-01  9.96866E-01  1.00238E+00  9.97068E-01  9.92855E-01  9.98634E-01  9.95144E-01  9.98628E-01  9.90304E-01  9.90331E-01  9.88274E-01  9.86829E-01  9.97712E-01  9.89688E-01  9.93441E-01  9.91397E-01  9.86844E-01  9.83102E-01  9.98216E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 71])  = '/home/thomasligonnet/Documents/XS/xs_lib/jeff33_modif_eurofusion/xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1:  3])  = 'N/A' ;
SFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
NFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  2.95583E-01 0.0E+00  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  0.00000E+00  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TMS_SAMPLING_EFF          (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  9.80379E-01 9.8E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.59989E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.59894E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.72091E+00 0.00021  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.26770E+02 0.00024  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2076870992 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.46145E+05 0.00050 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00006E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.37663E+04 ;
RUNNING_TIME              (idx, 1)        =  1.17011E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.48800E-01  3.48800E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.00000E-02  1.00000E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.16975E+03  1.16975E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.17011E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85726 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88644E+01 3.0E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85853E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.27 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 257582.82 ;
ALLOC_MEMSIZE             (idx, 1)        = 29304.45;
MEMSIZE                   (idx, 1)        = 21192.67;
XS_MEMSIZE                (idx, 1)        = 4715.71;
MAT_MEMSIZE               (idx, 1)        = 1450.61;
RES_MEMSIZE               (idx, 1)        = 2.93;
MISC_MEMSIZE              (idx, 1)        = 15023.40;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 8111.78;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 3455 ;
UNION_CELLS               (idx, 1)        = 19 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 1233146 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  2.25000E-03 ;
URES_EMAX                 (idx, 1)        =  3.86050E-01 ;
URES_AVAIL                (idx, 1)        = 5 ;
URES_USED                 (idx, 1)        = 5 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 64 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 64 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 2074 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_PREPROCESSOR      (idx, 1)        = 0 ;
TMS_MODE                  (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  0.00000E+00 ;
TOT_DECAY_HEAT            (idx, 1)        =  0.00000E+00 ;
TOT_SF_RATE               (idx, 1)        =  0.00000E+00 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  0.00000E+00 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  0.00000E+00 ;
INGESTION_TOXICITY        (idx, 1)        =  0.00000E+00 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Normaliation coefficient:

NORM_COEF                 (idx, [1:   4]) = [  3.32887E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.19618E-01 1.0E-04 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.38753E-01 1.6E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.12472E-02 0.00025 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.32866E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.00947E+00 3.1E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.10054E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.72170E-01 2.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82224E-01 9.4E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98660E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.33500E+01 3.1E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.77756E-02 0.00052 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.10375E+01 5.1E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46181E+00 1.1E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02237E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.01078E+00 5.3E-05  1.00326E+00 5.0E-05  7.51933E-03 0.00073 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.01076E+00 3.2E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.01084E+00 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.01076E+00 3.2E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.02908E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.00709E-03 0.00192  5.72757E-05 0.00866  2.90380E-04 0.00429  1.67041E-04 0.00580  3.72856E-04 0.00378  6.46739E-04 0.00296  2.19825E-04 0.00496  1.82289E-04 0.00568  7.06894E-05 0.00838 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.60891E-01 0.00076  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.50052E-03 0.00069  2.24063E-04 0.00416  1.08341E-03 0.00183  6.36715E-04 0.00236  1.41431E-03 0.00161  2.42259E-03 0.00123  8.00509E-04 0.00213  6.67922E-04 0.00235  2.51010E-04 0.00379 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.63300E-01 0.00109  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.78637E-05 0.00011  4.78435E-05 0.00011  5.05232E-05 0.00098 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.83786E-05 9.3E-05  4.83583E-05 9.4E-05  5.10667E-05 0.00098 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.43611E-03 0.00075  2.21412E-04 0.00445  1.07375E-03 0.00194  6.32323E-04 0.00255  1.39934E-03 0.00174  2.40206E-03 0.00134  7.95022E-04 0.00229  6.62969E-04 0.00255  2.49229E-04 0.00418 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.63716E-01 0.00119  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.70941E-05 0.00022  4.70742E-05 0.00022  4.96768E-05 0.00222 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.76008E-05 0.00021  4.75806E-05 0.00021  5.02116E-05 0.00222 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.56956E-03 0.00217  2.23522E-04 0.01247  1.08888E-03 0.00581  6.53623E-04 0.00735  1.43001E-03 0.00498  2.43744E-03 0.00377  8.14535E-04 0.00654  6.68818E-04 0.00741  2.52731E-04 0.01181 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.62142E-01 0.00335  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.57171E-03 0.00212  2.24806E-04 0.01228  1.08997E-03 0.00567  6.54492E-04 0.00720  1.42788E-03 0.00486  2.43745E-03 0.00369  8.14798E-04 0.00641  6.69535E-04 0.00731  2.52785E-04 0.01164 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.62012E-01 0.00329  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.60847E+02 0.00219 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.74723E-05 6.7E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.79830E-05 4.1E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.54640E-03 0.00041 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.58969E+02 0.00042 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.39338E-06 5.3E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96047E-06 4.6E-05  1.96033E-06 4.7E-05  1.97936E-06 0.00052 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.31798E-05 7.6E-05  7.32391E-05 7.6E-05  6.53359E-05 0.00087 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.03018E-01 2.1E-05 -3.43103E-02 0.00179  2.49074E-04 0.00182 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21788E+01 0.00111 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.02913E+00 5.8E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.69889E+01 4.1E-05  1.63613E+01 6.6E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.95504E-01 2.8E-05  2.58336E+00 3.1E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  5.01292E-03 8.4E-05  2.67021E-02 3.4E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.77293E-03 6.9E-05  4.88616E-02 6.0E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.76001E-03 6.0E-05  2.21594E-02 9.8E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.59990E-03 6.1E-05  5.41116E-02 9.8E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.61356E+00 7.7E-06  2.44192E+00 3.1E-09 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04497E+02 7.5E-07  2.01942E+02 7.5E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.38076E-08 5.5E-05  3.58663E-06 1.3E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.88723E-01 2.8E-05  2.53450E+00 3.2E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.52269E-01 3.2E-05  5.22260E-01 3.3E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.37544E-01 3.9E-05  8.98793E-02 9.0E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.04772E-03 0.00031  2.38036E-02 0.00027 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.61651E-02 0.00016 -2.05491E-02 0.00027 ];
INF_SCATT5                (idx, [1:   4]) = [  2.64722E-05 0.08442  1.14572E-02 0.00043 ];
INF_SCATT6                (idx, [1:   4]) = [  7.28775E-03 0.00028 -3.11534E-02 0.00015 ];
INF_SCATT7                (idx, [1:   4]) = [  8.13813E-04 0.00234  1.07523E-02 0.00047 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.88779E-01 2.8E-05  2.53450E+00 3.2E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.52272E-01 3.2E-05  5.22260E-01 3.3E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.37546E-01 3.9E-05  8.98793E-02 9.0E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.04791E-03 0.00031  2.38036E-02 0.00027 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.61651E-02 0.00016 -2.05491E-02 0.00027 ];
INF_SCATTP5               (idx, [1:   4]) = [  2.65010E-05 0.08434  1.14572E-02 0.00043 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.28778E-03 0.00028 -3.11534E-02 0.00015 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.13818E-04 0.00234  1.07523E-02 0.00047 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.44440E-01 3.8E-05  1.73248E+00 3.9E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.36366E+00 3.8E-05  1.92402E-01 3.9E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.71656E-03 6.9E-05  4.88609E-02 6.0E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.66280E-02 4.0E-05  4.90834E-02 6.8E-05 ];

% Poison cross sections:

INF_I135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_I135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Fission spectra:

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  1.16061E-09 0.61407 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 9.6E-08  1.57329E-07 0.61291 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.58876E-01 2.8E-05  2.98463E-02 3.9E-05  2.23739E-04 0.00067  2.53428E+00 3.2E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.43504E-01 3.2E-05  8.76508E-03 7.7E-05  1.29502E-04 0.00087  5.22130E-01 3.3E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.40598E-01 3.8E-05 -3.05398E-03 0.00017  8.19938E-05 0.00109  8.97973E-02 9.0E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24576E-02 0.00022 -3.40985E-03 0.00013  4.21722E-05 0.00168  2.37614E-02 0.00027 ];
INF_S4                    (idx, [1:   8]) = [ -1.53648E-02 0.00017 -8.00325E-04 0.00049  1.35969E-05 0.00418 -2.05627E-02 0.00027 ];
INF_S5                    (idx, [1:   8]) = [ -3.08516E-04 0.00715  3.34988E-04 0.00108 -2.44673E-06 0.02034  1.14597E-02 0.00043 ];
INF_S6                    (idx, [1:   8]) = [  7.55336E-03 0.00026 -2.65610E-04 0.00122 -9.32460E-06 0.00497 -3.11441E-02 0.00015 ];
INF_S7                    (idx, [1:   8]) = [  1.28291E-03 0.00143 -4.69101E-04 0.00071 -1.11344E-05 0.00398  1.07634E-02 0.00047 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.58933E-01 2.8E-05  2.98463E-02 3.9E-05  2.23740E-04 0.00067  2.53428E+00 3.2E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.43507E-01 3.2E-05  8.76508E-03 7.7E-05  1.29502E-04 0.00087  5.22130E-01 3.3E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.40600E-01 3.8E-05 -3.05398E-03 0.00017  8.19938E-05 0.00109  8.97973E-02 9.0E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24578E-02 0.00022 -3.40985E-03 0.00013  4.21722E-05 0.00168  2.37614E-02 0.00027 ];
INF_SP4                   (idx, [1:   8]) = [ -1.53648E-02 0.00017 -8.00325E-04 0.00049  1.35969E-05 0.00418 -2.05627E-02 0.00027 ];
INF_SP5                   (idx, [1:   8]) = [ -3.08487E-04 0.00716  3.34988E-04 0.00108 -2.44673E-06 0.02034  1.14597E-02 0.00043 ];
INF_SP6                   (idx, [1:   8]) = [  7.55339E-03 0.00026 -2.65610E-04 0.00122 -9.32461E-06 0.00497 -3.11441E-02 0.00015 ];
INF_SP7                   (idx, [1:   8]) = [  1.28292E-03 0.00143 -4.69101E-04 0.00071 -1.11344E-05 0.00398  1.07634E-02 0.00047 ];

% Integral parameters:

B1_KINF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_KEFF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_B2                     (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_ERR                    (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Critical spectrum in infinite geometry:

B1_FLX                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

B1_TOT                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CAPT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABS                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISS                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NUBAR                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_KAPPA                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INVV                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering cross sections:

B1_SCATT0                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT1                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT2                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT3                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT4                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT5                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT6                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT7                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering production cross sections:

B1_SCATTP0                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP1                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP2                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP3                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP4                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP5                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP6                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP7                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Diffusion parameters:

B1_TRANSPXS               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reduced absoption and removal:

B1_RABSXS                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Poison cross sections:

B1_I135_YIELD             (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_I135_MICRO_ABS         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Fission spectra:

B1_CHIT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHIP                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHID                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

B1_S0                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S1                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S2                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S3                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S4                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S5                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S6                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S7                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering production matrixes:

B1_SP0                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP1                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP2                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP3                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP4                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP5                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP6                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP7                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

