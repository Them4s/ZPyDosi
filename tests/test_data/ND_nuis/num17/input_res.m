
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
START_DATE                (idx, [1: 24])  = 'Thu Jan 22 00:19:59 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Jan 22 20:24:10 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.19960E+00  1.00506E+00  1.00013E+00  9.90541E-01  9.91533E-01  9.90051E-01  9.98238E-01  9.95267E-01  9.97227E-01  9.86252E-01  9.91866E-01  9.95893E-01  9.82677E-01  9.95922E-01  9.91256E-01  9.91772E-01  9.98706E-01  9.92696E-01  9.84047E-01  1.00273E+00  9.89806E-01  9.89283E-01  1.00201E+00  9.90245E-01  9.95571E-01  9.82835E-01  9.93724E-01  9.94681E-01  9.94285E-01  9.86096E-01  ];
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
TOT_COL_EFF               (idx, [1:   4]) = [  9.80251E-01 9.7E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.59261E+01 0.00023  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.59163E+01 0.00023  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.73091E+00 0.00022  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.27005E+02 0.00025  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2127707056 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.54618E+05 0.00054 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.47575E+04 ;
RUNNING_TIME              (idx, 1)        =  1.20418E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.72267E-01  3.72267E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.53333E-03  9.53333E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.20380E+03  1.20380E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.20418E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.86410 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88716E+01 3.1E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85907E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.30 ;

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

NORM_COEF                 (idx, [1:   4]) = [  3.32902E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.16835E-01 1.0E-04 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.39377E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.06227E-02 0.00026 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.30960E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  9.99999E-01 3.2E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.04178E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.77782E-01 2.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.81960E-01 9.3E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98707E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.35507E+01 3.1E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.80402E-02 0.00051 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.11121E+01 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.47416E+00 1.3E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02234E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.00142E+00 5.3E-05  9.94011E-01 5.1E-05  7.41368E-03 0.00073 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.00129E+00 3.2E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.00130E+00 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.00129E+00 3.2E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.01971E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  1.94638E-03 0.00199  5.60155E-05 0.00880  2.82903E-04 0.00439  1.60227E-04 0.00509  3.62957E-04 0.00370  6.26588E-04 0.00293  2.12759E-04 0.00513  1.75326E-04 0.00577  6.96001E-05 0.00914 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.60667E-01 0.00075  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.47158E-03 0.00069  2.22600E-04 0.00406  1.08125E-03 0.00182  6.35964E-04 0.00236  1.40698E-03 0.00157  2.41511E-03 0.00121  7.96531E-04 0.00215  6.61932E-04 0.00232  2.51209E-04 0.00384 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.63023E-01 0.00107  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.83654E-05 0.00011  4.83436E-05 0.00011  5.12620E-05 0.00101 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.84332E-05 9.2E-05  4.84114E-05 9.2E-05  5.13339E-05 0.00101 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.40374E-03 0.00075  2.19493E-04 0.00435  1.07123E-03 0.00196  6.29490E-04 0.00259  1.39432E-03 0.00171  2.39416E-03 0.00131  7.91237E-04 0.00232  6.55503E-04 0.00248  2.48303E-04 0.00413 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.62868E-01 0.00118  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.76187E-05 0.00021  4.75972E-05 0.00021  5.04151E-05 0.00221 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.76855E-05 0.00020  4.76640E-05 0.00020  5.04862E-05 0.00221 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.55179E-03 0.00216  2.26824E-04 0.01252  1.09768E-03 0.00559  6.47593E-04 0.00757  1.42678E-03 0.00497  2.44446E-03 0.00381  7.98080E-04 0.00665  6.62588E-04 0.00723  2.47791E-04 0.01204 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.58597E-01 0.00338  1.24667E-02 5.0E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.55174E-03 0.00211  2.27225E-04 0.01225  1.09805E-03 0.00547  6.46591E-04 0.00738  1.42712E-03 0.00490  2.44556E-03 0.00373  7.97363E-04 0.00654  6.62296E-04 0.00708  2.47530E-04 0.01180 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.58482E-01 0.00331  1.24667E-02 5.0E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.58715E+02 0.00218 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.79977E-05 6.7E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.80651E-05 4.1E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.51031E-03 0.00043 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.56476E+02 0.00043 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.38838E-06 5.2E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96129E-06 4.8E-05  1.96112E-06 4.8E-05  1.98280E-06 0.00053 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.32659E-05 7.5E-05  7.33254E-05 7.5E-05  6.53426E-05 0.00086 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.02903E-01 2.1E-05 -3.59928E-02 0.00181  2.58819E-04 0.00182 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.22249E+01 0.00110 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.01975E+00 5.2E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.71741E+01 4.2E-05  1.63768E+01 6.0E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.91949E-01 2.7E-05  2.58350E+00 3.0E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  4.98014E-03 7.8E-05  2.70172E-02 3.3E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.72060E-03 6.4E-05  4.88094E-02 5.6E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.74045E-03 6.2E-05  2.17922E-02 8.9E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.61696E-03 6.5E-05  5.34015E-02 8.9E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.65274E+00 8.0E-06  2.45049E+00 1.7E-09 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04445E+02 6.9E-07  2.01942E+02 7.4E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.33716E-08 5.4E-05  3.58701E-06 1.3E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.85219E-01 2.7E-05  2.53469E+00 3.1E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.50214E-01 3.1E-05  5.22148E-01 3.3E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.36862E-01 3.6E-05  8.98263E-02 8.3E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.09417E-03 0.00030  2.37759E-02 0.00027 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.59965E-02 0.00015 -2.05523E-02 0.00027 ];
INF_SCATT5                (idx, [1:   4]) = [  5.72337E-05 0.03638  1.14547E-02 0.00048 ];
INF_SCATT6                (idx, [1:   4]) = [  7.25496E-03 0.00028 -3.11363E-02 0.00015 ];
INF_SCATT7                (idx, [1:   4]) = [  8.10701E-04 0.00236  1.07386E-02 0.00038 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.85276E-01 2.7E-05  2.53469E+00 3.1E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.50217E-01 3.1E-05  5.22148E-01 3.3E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.36863E-01 3.6E-05  8.98263E-02 8.3E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.09438E-03 0.00030  2.37759E-02 0.00027 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.59965E-02 0.00015 -2.05523E-02 0.00027 ];
INF_SCATTP5               (idx, [1:   4]) = [  5.72614E-05 0.03637  1.14547E-02 0.00048 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.25496E-03 0.00028 -3.11363E-02 0.00015 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.10698E-04 0.00236  1.07386E-02 0.00038 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.40269E-01 4.1E-05  1.73327E+00 3.8E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.38734E+00 4.1E-05  1.92314E-01 3.8E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.66371E-03 6.5E-05  4.88087E-02 5.6E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.63698E-02 3.8E-05  4.90332E-02 6.7E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 1.3E-09  1.40370E-09 0.95619 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 1.8E-07  1.88504E-07 0.95637 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.55579E-01 2.7E-05  2.96405E-02 3.7E-05  2.24285E-04 0.00068  2.53447E+00 3.1E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.41513E-01 3.0E-05  8.70122E-03 8.0E-05  1.29748E-04 0.00089  5.22018E-01 3.3E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.39895E-01 3.6E-05 -3.03301E-03 0.00018  8.21739E-05 0.00106  8.97441E-02 8.3E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24795E-02 0.00022 -3.38534E-03 0.00014  4.21926E-05 0.00159  2.37337E-02 0.00027 ];
INF_S4                    (idx, [1:   8]) = [ -1.52027E-02 0.00016 -7.93805E-04 0.00052  1.36020E-05 0.00412 -2.05659E-02 0.00027 ];
INF_S5                    (idx, [1:   8]) = [ -2.75911E-04 0.00739  3.33144E-04 0.00108 -2.50211E-06 0.01955  1.14572E-02 0.00048 ];
INF_S6                    (idx, [1:   8]) = [  7.51960E-03 0.00026 -2.64648E-04 0.00124 -9.31590E-06 0.00505 -3.11270E-02 0.00015 ];
INF_S7                    (idx, [1:   8]) = [  1.27724E-03 0.00148 -4.66535E-04 0.00065 -1.11615E-05 0.00411  1.07498E-02 0.00038 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.55636E-01 2.7E-05  2.96405E-02 3.7E-05  2.24286E-04 0.00068  2.53447E+00 3.1E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.41516E-01 3.0E-05  8.70122E-03 8.0E-05  1.29748E-04 0.00089  5.22018E-01 3.3E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.39896E-01 3.6E-05 -3.03302E-03 0.00018  8.21739E-05 0.00106  8.97442E-02 8.3E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24797E-02 0.00022 -3.38534E-03 0.00014  4.21926E-05 0.00159  2.37337E-02 0.00027 ];
INF_SP4                   (idx, [1:   8]) = [ -1.52027E-02 0.00016 -7.93806E-04 0.00052  1.36019E-05 0.00412 -2.05659E-02 0.00027 ];
INF_SP5                   (idx, [1:   8]) = [ -2.75883E-04 0.00739  3.33144E-04 0.00108 -2.50212E-06 0.01955  1.14572E-02 0.00048 ];
INF_SP6                   (idx, [1:   8]) = [  7.51961E-03 0.00026 -2.64649E-04 0.00124 -9.31591E-06 0.00505 -3.11270E-02 0.00015 ];
INF_SP7                   (idx, [1:   8]) = [  1.27723E-03 0.00148 -4.66535E-04 0.00065 -1.11615E-05 0.00411  1.07498E-02 0.00038 ];

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

