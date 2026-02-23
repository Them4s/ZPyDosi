
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
COMPLETE_DATE             (idx, [1: 24])  = 'Fri Jan 16 07:54:07 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.23142E+00  1.01731E+00  1.00695E+00  9.93967E-01  1.00249E+00  9.98123E-01  9.93607E-01  9.97400E-01  9.67267E-01  9.84851E-01  9.91777E-01  9.84859E-01  1.00502E+00  9.89529E-01  9.85244E-01  9.91433E-01  9.90622E-01  9.95337E-01  9.91163E-01  9.93285E-01  9.96416E-01  9.84453E-01  9.88279E-01  9.81491E-01  9.84196E-01  9.99399E-01  9.91642E-01  9.85579E-01  9.87035E-01  9.89850E-01  ];
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
TOT_COL_EFF               (idx, [1:   4]) = [  9.80439E-01 9.5E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.49224E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.49127E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.69407E+00 0.00021  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.25131E+02 0.00024  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2137488310 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.56248E+05 0.00051 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00007 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.44248E+04 ;
RUNNING_TIME              (idx, 1)        =  1.19283E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.48100E-01  3.48100E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.85000E-03  9.85000E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.19247E+03  1.19247E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.19283E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85978 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88671E+01 3.0E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85800E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.25 ;

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

NORM_COEF                 (idx, [1:   4]) = [  3.32905E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.15166E-01 9.9E-05 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.40528E-01 1.6E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  5.94718E-02 0.00026 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.33336E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.00842E+00 3.1E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.11522E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.70799E-01 2.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82321E-01 9.0E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98716E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.31856E+01 3.0E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.76788E-02 0.00050 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.06155E+01 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.45046E+00 1.2E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02229E+02 1.3E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.00972E+00 5.2E-05  1.00218E+00 5.0E-05  7.53193E-03 0.00072 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.00972E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.00972E+00 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.00972E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.02792E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  1.95878E-03 0.00202  5.69552E-05 0.01023  2.83747E-04 0.00421  1.61625E-04 0.00514  3.63882E-04 0.00376  6.33115E-04 0.00304  2.12745E-04 0.00481  1.77158E-04 0.00606  6.95560E-05 0.00982 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.59636E-01 0.00076  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.53021E-03 0.00069  2.24457E-04 0.00390  1.08882E-03 0.00180  6.41376E-04 0.00232  1.42100E-03 0.00159  2.43704E-03 0.00120  8.00707E-04 0.00214  6.65112E-04 0.00232  2.51700E-04 0.00380 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.61925E-01 0.00108  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.74813E-05 0.00011  4.74603E-05 0.00011  5.02353E-05 0.00096 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.79421E-05 9.2E-05  4.79209E-05 9.2E-05  5.07230E-05 0.00096 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.45889E-03 0.00074  2.22165E-04 0.00426  1.07914E-03 0.00193  6.34030E-04 0.00253  1.40529E-03 0.00171  2.41586E-03 0.00129  7.94394E-04 0.00231  6.58583E-04 0.00253  2.49431E-04 0.00406 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.62055E-01 0.00116  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.67057E-05 0.00021  4.66856E-05 0.00021  4.93359E-05 0.00216 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.71590E-05 0.00021  4.71386E-05 0.00021  4.98152E-05 0.00216 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.60914E-03 0.00210  2.31336E-04 0.01217  1.09016E-03 0.00562  6.57503E-04 0.00718  1.44735E-03 0.00486  2.44934E-03 0.00369  8.13331E-04 0.00666  6.67892E-04 0.00727  2.52232E-04 0.01203 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.59687E-01 0.00333  1.24667E-02 5.0E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.60690E-03 0.00205  2.31867E-04 0.01197  1.09149E-03 0.00552  6.58024E-04 0.00704  1.44594E-03 0.00479  2.44703E-03 0.00360  8.11197E-04 0.00654  6.69042E-04 0.00714  2.52309E-04 0.01179 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.59871E-01 0.00327  1.24667E-02 5.0E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.63030E+02 0.00211 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.70996E-05 6.8E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.75567E-05 4.2E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.57108E-03 0.00040 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.60751E+02 0.00040 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.38134E-06 5.2E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96143E-06 4.7E-05  1.96127E-06 4.7E-05  1.98369E-06 0.00053 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.22952E-05 7.6E-05  7.23540E-05 7.6E-05  6.45197E-05 0.00084 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.02448E-01 2.1E-05 -3.50724E-02 0.00180  2.54530E-04 0.00181 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.22273E+01 0.00110 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.02793E+00 5.3E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.70150E+01 4.6E-05  1.61707E+01 6.4E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.98083E-01 2.8E-05  2.58227E+00 3.3E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  5.00991E-03 7.9E-05  2.69289E-02 3.3E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.78684E-03 6.5E-05  4.94091E-02 5.7E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.77693E-03 6.2E-05  2.24802E-02 9.3E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.66234E-03 6.3E-05  5.45723E-02 9.3E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.62382E+00 8.0E-06  2.42757E+00 2.0E-09 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04405E+02 7.0E-07  2.01942E+02 7.6E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.37336E-08 5.3E-05  3.58258E-06 1.4E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.91287E-01 2.9E-05  2.53286E+00 3.4E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.51390E-01 3.2E-05  5.21742E-01 3.6E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.37184E-01 3.5E-05  8.98711E-02 9.1E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.00018E-03 0.00030  2.38015E-02 0.00028 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.61454E-02 0.00014 -2.04908E-02 0.00027 ];
INF_SCATT5                (idx, [1:   4]) = [  1.77794E-05 0.11687  1.14236E-02 0.00048 ];
INF_SCATT6                (idx, [1:   4]) = [  7.26497E-03 0.00027 -3.10825E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.06777E-04 0.00229  1.06969E-02 0.00039 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.91344E-01 2.8E-05  2.53286E+00 3.4E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.51392E-01 3.2E-05  5.21742E-01 3.6E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.37185E-01 3.5E-05  8.98711E-02 9.1E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.00040E-03 0.00030  2.38015E-02 0.00028 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.61454E-02 0.00014 -2.04908E-02 0.00027 ];
INF_SCATTP5               (idx, [1:   4]) = [  1.77753E-05 0.11680  1.14236E-02 0.00048 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.26501E-03 0.00027 -3.10825E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.06774E-04 0.00229  1.06969E-02 0.00039 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.45662E-01 3.9E-05  1.73279E+00 4.1E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.35688E+00 3.9E-05  1.92368E-01 4.1E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.73003E-03 6.5E-05  4.94084E-02 5.7E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.65949E-02 4.3E-05  4.96362E-02 7.7E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  6.06214E-10 0.41564 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 3.4E-08  8.27155E-08 0.41572 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.61488E-01 2.8E-05  2.97987E-02 4.0E-05  2.27748E-04 0.00069  2.53263E+00 3.4E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.42648E-01 3.1E-05  8.74131E-03 7.6E-05  1.31078E-04 0.00089  5.21611E-01 3.6E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.40234E-01 3.5E-05 -3.04944E-03 0.00017  8.27396E-05 0.00105  8.97884E-02 9.1E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24029E-02 0.00021 -3.40272E-03 0.00013  4.24406E-05 0.00165  2.37590E-02 0.00028 ];
INF_S4                    (idx, [1:   8]) = [ -1.53483E-02 0.00015 -7.97097E-04 0.00049  1.35400E-05 0.00436 -2.05043E-02 0.00026 ];
INF_S5                    (idx, [1:   8]) = [ -3.16991E-04 0.00647  3.34771E-04 0.00111 -2.63325E-06 0.02043  1.14262E-02 0.00048 ];
INF_S6                    (idx, [1:   8]) = [  7.53160E-03 0.00025 -2.66629E-04 0.00130 -9.47560E-06 0.00497 -3.10730E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.27591E-03 0.00142 -4.69128E-04 0.00070 -1.12496E-05 0.00386  1.07081E-02 0.00039 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.61545E-01 2.8E-05  2.97987E-02 4.0E-05  2.27748E-04 0.00069  2.53263E+00 3.4E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.42651E-01 3.1E-05  8.74131E-03 7.6E-05  1.31078E-04 0.00089  5.21611E-01 3.6E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.40235E-01 3.5E-05 -3.04944E-03 0.00017  8.27397E-05 0.00105  8.97884E-02 9.1E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24031E-02 0.00021 -3.40272E-03 0.00013  4.24406E-05 0.00165  2.37590E-02 0.00028 ];
INF_SP4                   (idx, [1:   8]) = [ -1.53483E-02 0.00015 -7.97097E-04 0.00049  1.35400E-05 0.00436 -2.05043E-02 0.00026 ];
INF_SP5                   (idx, [1:   8]) = [ -3.16996E-04 0.00647  3.34771E-04 0.00111 -2.63325E-06 0.02043  1.14262E-02 0.00048 ];
INF_SP6                   (idx, [1:   8]) = [  7.53164E-03 0.00025 -2.66629E-04 0.00130 -9.47561E-06 0.00497 -3.10730E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.27590E-03 0.00142 -4.69128E-04 0.00070 -1.12496E-05 0.00386  1.07081E-02 0.00039 ];

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

