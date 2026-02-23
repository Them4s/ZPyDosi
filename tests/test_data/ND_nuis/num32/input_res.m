
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
START_DATE                (idx, [1: 24])  = 'Tue Jan 27 18:24:00 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Wed Jan 28 14:01:37 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.18474E+00  1.00943E+00  1.00005E+00  9.97176E-01  1.00131E+00  9.91501E-01  9.88372E-01  9.96468E-01  9.95871E-01  9.82654E-01  9.94943E-01  9.99248E-01  9.88364E-01  9.95292E-01  9.89944E-01  9.94619E-01  9.94090E-01  9.88868E-01  9.95637E-01  9.94871E-01  9.91135E-01  9.86570E-01  9.96102E-01  9.97711E-01  9.86959E-01  9.95028E-01  9.95320E-01  9.88016E-01  9.82361E-01  9.97352E-01  ];
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
TOT_COL_EFF               (idx, [1:   4]) = [  9.81045E-01 9.3E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.63320E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.63224E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.66786E+00 0.00022  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.27615E+02 0.00024  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2090671579 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.48445E+05 0.00053 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.39813E+04 ;
RUNNING_TIME              (idx, 1)        =  1.17761E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.73650E-01  3.73650E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.35000E-03  9.35000E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.17722E+03  1.17722E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.17761E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85621 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88601E+01 4.6E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85786E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.24 ;

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

NORM_COEF                 (idx, [1:   4]) = [  3.32885E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.13957E-01 9.8E-05 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.38046E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.19541E-02 0.00025 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.32691E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  9.99603E-01 3.2E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.09509E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.72878E-01 2.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82387E-01 9.4E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98654E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.35579E+01 3.0E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.76131E-02 0.00052 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.12671E+01 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.44098E+00 1.3E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02241E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.00095E+00 5.3E-05  9.93407E-01 5.0E-05  7.52190E-03 0.00073 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.00088E+00 3.2E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.00096E+00 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.00088E+00 3.2E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.01885E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.02673E-03 0.00217  5.77675E-05 0.00982  2.93977E-04 0.00481  1.66671E-04 0.00546  3.76654E-04 0.00396  6.53151E-04 0.00310  2.22394E-04 0.00548  1.83495E-04 0.00567  7.26202E-05 0.00901 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.61908E-01 0.00075  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.58637E-03 0.00069  2.27151E-04 0.00408  1.09557E-03 0.00182  6.45786E-04 0.00236  1.42701E-03 0.00159  2.45219E-03 0.00121  8.09957E-04 0.00214  6.73329E-04 0.00231  2.55380E-04 0.00384 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.63535E-01 0.00108  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.81699E-05 0.00011  4.81479E-05 0.00011  5.10447E-05 0.00097 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.82149E-05 9.4E-05  4.81929E-05 9.4E-05  5.10926E-05 0.00097 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.51560E-03 0.00075  2.23971E-04 0.00433  1.08519E-03 0.00195  6.37218E-04 0.00257  1.41326E-03 0.00172  2.42909E-03 0.00131  8.05453E-04 0.00230  6.68232E-04 0.00253  2.53177E-04 0.00418 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.64095E-01 0.00117  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.74016E-05 0.00021  4.73786E-05 0.00022  5.03435E-05 0.00223 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.74459E-05 0.00021  4.74229E-05 0.00021  5.03913E-05 0.00223 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.65877E-03 0.00214  2.30147E-04 0.01256  1.10784E-03 0.00568  6.56064E-04 0.00743  1.45413E-03 0.00496  2.47805E-03 0.00381  8.06733E-04 0.00664  6.79008E-04 0.00707  2.46791E-04 0.01196 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.57584E-01 0.00331  1.24667E-02 5.0E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.65294E-03 0.00210  2.29926E-04 0.01225  1.10777E-03 0.00553  6.54271E-04 0.00727  1.45311E-03 0.00485  2.47590E-03 0.00372  8.05868E-04 0.00650  6.78556E-04 0.00698  2.47538E-04 0.01170 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.58025E-01 0.00327  1.24667E-02 5.0E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.61707E+02 0.00216 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.77933E-05 6.8E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.78380E-05 4.2E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.63169E-03 0.00041 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.59685E+02 0.00042 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.38880E-06 5.3E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96225E-06 4.8E-05  1.96209E-06 4.8E-05  1.98328E-06 0.00060 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.33080E-05 7.6E-05  7.33699E-05 7.6E-05  6.51911E-05 0.00086 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.02857E-01 2.1E-05 -3.41370E-02 0.00191  2.50162E-04 0.00193 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21910E+01 0.00109 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.01893E+00 5.3E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.71760E+01 4.0E-05  1.63821E+01 6.4E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.94488E-01 2.7E-05  2.58783E+00 3.0E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  4.96650E-03 7.8E-05  2.67312E-02 3.4E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.73581E-03 6.3E-05  4.87936E-02 5.8E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.76931E-03 6.4E-05  2.20624E-02 9.4E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.64099E-03 6.6E-05  5.33196E-02 9.4E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.62305E+00 8.1E-06  2.41676E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04491E+02 7.2E-07  2.01942E+02 7.7E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.33789E-08 5.1E-05  3.58755E-06 1.3E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.87744E-01 2.7E-05  2.53904E+00 3.1E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.50305E-01 3.0E-05  5.22498E-01 3.3E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.36910E-01 3.5E-05  8.98669E-02 8.5E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.12425E-03 0.00030  2.37927E-02 0.00025 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.59630E-02 0.00015 -2.05628E-02 0.00026 ];
INF_SCATT5                (idx, [1:   4]) = [  7.05329E-05 0.03108  1.14737E-02 0.00042 ];
INF_SCATT6                (idx, [1:   4]) = [  7.25237E-03 0.00027 -3.11695E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.11731E-04 0.00238  1.07552E-02 0.00042 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.87800E-01 2.7E-05  2.53904E+00 3.1E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.50308E-01 3.0E-05  5.22498E-01 3.3E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.36912E-01 3.5E-05  8.98669E-02 8.5E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.12446E-03 0.00030  2.37927E-02 0.00025 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.59629E-02 0.00015 -2.05628E-02 0.00026 ];
INF_SCATTP5               (idx, [1:   4]) = [  7.05504E-05 0.03107  1.14737E-02 0.00042 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.25242E-03 0.00027 -3.11695E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.11736E-04 0.00238  1.07552E-02 0.00042 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.42327E-01 3.8E-05  1.73746E+00 3.6E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.37555E+00 3.8E-05  1.91851E-01 3.6E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.67985E-03 6.5E-05  4.87929E-02 5.8E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.63804E-02 4.1E-05  4.90153E-02 7.5E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 6.6E-10  1.53381E-10 0.68265 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 1.4E-08  2.02508E-08 0.68115 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.58108E-01 2.7E-05  2.96359E-02 3.8E-05  2.25428E-04 0.00067  2.53882E+00 3.1E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.41612E-01 3.0E-05  8.69294E-03 7.6E-05  1.29609E-04 0.00087  5.22368E-01 3.3E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.39942E-01 3.5E-05 -3.03142E-03 0.00018  8.18929E-05 0.00110  8.97850E-02 8.5E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.25079E-02 0.00021 -3.38363E-03 0.00012  4.20166E-05 0.00166  2.37507E-02 0.00025 ];
INF_S4                    (idx, [1:   8]) = [ -1.51698E-02 0.00016 -7.93181E-04 0.00048  1.34589E-05 0.00410 -2.05763E-02 0.00026 ];
INF_S5                    (idx, [1:   8]) = [ -2.62776E-04 0.00821  3.33309E-04 0.00106 -2.52770E-06 0.01863  1.14762E-02 0.00042 ];
INF_S6                    (idx, [1:   8]) = [  7.51711E-03 0.00026 -2.64739E-04 0.00119 -9.34442E-06 0.00504 -3.11601E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.27833E-03 0.00147 -4.66601E-04 0.00068 -1.11918E-05 0.00370  1.07664E-02 0.00042 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.58164E-01 2.7E-05  2.96359E-02 3.8E-05  2.25428E-04 0.00067  2.53882E+00 3.1E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.41615E-01 3.0E-05  8.69294E-03 7.6E-05  1.29609E-04 0.00087  5.22368E-01 3.3E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.39943E-01 3.5E-05 -3.03142E-03 0.00018  8.18929E-05 0.00110  8.97850E-02 8.5E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.25081E-02 0.00022 -3.38363E-03 0.00012  4.20166E-05 0.00166  2.37507E-02 0.00025 ];
INF_SP4                   (idx, [1:   8]) = [ -1.51697E-02 0.00016 -7.93181E-04 0.00048  1.34589E-05 0.00410 -2.05763E-02 0.00026 ];
INF_SP5                   (idx, [1:   8]) = [ -2.62759E-04 0.00821  3.33309E-04 0.00106 -2.52771E-06 0.01863  1.14762E-02 0.00042 ];
INF_SP6                   (idx, [1:   8]) = [  7.51716E-03 0.00026 -2.64739E-04 0.00119 -9.34442E-06 0.00504 -3.11601E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.27834E-03 0.00147 -4.66601E-04 0.00068 -1.11918E-05 0.00370  1.07664E-02 0.00042 ];

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

