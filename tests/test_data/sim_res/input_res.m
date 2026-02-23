
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
START_DATE                (idx, [1: 24])  = 'Fri Dec 22 16:49:09 2023' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Tue Jan  9 23:02:28 2024' ;

% Run parameters:

POP                       (idx, 1)        = 10000 ;
CYCLES                    (idx, 1)        = 600000 ;
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
CPU_MHZ                   (idx, 1)        = 167805444.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 5 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_HISTORY_PROFILE       (idx, [1:   5]) = [  1.04973E+00  9.82030E-01  9.75019E-01  9.95489E-01  9.97730E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 71])  = '/home/thomasligonnet/Documents/XS/xs_lib/jeff33_modif_eurofusion/xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1:  3])  = 'N/A' ;
SFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
NFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  2.95583E-01 6.3E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  0.00000E+00  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TMS_SAMPLING_EFF          (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  9.80639E-01 4.2E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  7.95223E+01 4.5E-05  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  7.95147E+01 4.5E-05  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.56995E+00 4.9E-05  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.20229E+02 5.9E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 136576 ;
SOURCE_NEUTRONS           (idx, 1)        = 9540303250 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  6.98534E+04 0.00014 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  1.00007E+04 0.00003 ];
SIMULATION_COMPLETED      (idx, 1)        = 0 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  1.30409E+05 ;
RUNNING_TIME              (idx, 1)        =  2.62933E+04 ;
INIT_TIME                 (idx, [1:  2])  = [  5.64517E-01  5.64517E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.91667E-03  9.91667E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  2.62927E+04  0.00000E+00  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.15488E+05  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 4.95979 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  4.96010E+00 5.8E-06 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.97494E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 4.95 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 257585.87 ;
ALLOC_MEMSIZE             (idx, 1)        = 11111.16;
MEMSIZE                   (idx, 1)        = 10868.24;
XS_MEMSIZE                (idx, 1)        = 4145.10;
MAT_MEMSIZE               (idx, 1)        = 1576.07;
RES_MEMSIZE               (idx, 1)        = 138.15;
MISC_MEMSIZE              (idx, 1)        = 5008.91;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 242.92;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 3513 ;
UNION_CELLS               (idx, 1)        = 19 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 1274560 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  2.25000E-03 ;
URES_EMAX                 (idx, 1)        =  3.86050E-01 ;
URES_AVAIL                (idx, 1)        = 5 ;
URES_USED                 (idx, 1)        = 5 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 66 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 66 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 2127 ;
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

NORM_COEF                 (idx, [1:   4]) = [  9.98772E-05 1.5E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.15444E-01 4.3E-05 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.38409E-01 7.3E-06 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.15910E-02 0.00011 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.32460E-11 1.4E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.00128E+00 1.4E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.08800E-01 1.4E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.73541E-01 1.0E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82341E-01 4.2E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98772E-01 1.5E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.31926E+01 1.4E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.76588E-02 0.00023 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.06636E+01 2.2E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.44932E+00 5.6E-07 ];
FISSE                     (idx, [1:   2]) = [  2.02239E+02 5.9E-08 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.00256E+00 2.3E-05  9.95062E-01 2.2E-05  7.49997E-03 0.00032 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.00256E+00 1.4E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.00254E+00 2.0E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.00256E+00 1.4E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.02061E+00 1.3E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.93892E-03 0.00064  8.47251E-05 0.00339  4.25117E-04 0.00153  2.42588E-04 0.00197  5.48173E-04 0.00134  9.48065E-04 0.00105  3.21125E-04 0.00183  2.64934E-04 0.00201  1.04192E-04 0.00331 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.61579E-01 0.00033  1.24667E-02 0.0E+00  2.82917E-02 6.7E-09  4.25244E-02 7.8E-09  1.33042E-01 1.6E-09  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 2.2E-09  3.55460E+00 4.7E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.55125E-03 0.00030  2.24626E-04 0.00175  1.09086E-03 0.00079  6.42255E-04 0.00103  1.42315E-03 0.00069  2.44039E-03 0.00053  8.06610E-04 0.00093  6.69983E-04 0.00101  2.53377E-04 0.00166 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.63158E-01 0.00047  1.24667E-02 0.0E+00  2.82917E-02 6.7E-09  4.25244E-02 7.8E-09  1.33042E-01 1.6E-09  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 2.2E-09  3.55460E+00 4.7E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.78950E-05 4.6E-05  4.78730E-05 4.7E-05  5.07701E-05 0.00042 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.80140E-05 4.0E-05  4.79920E-05 4.0E-05  5.08962E-05 0.00042 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.48077E-03 0.00032  2.22616E-04 0.00188  1.08116E-03 0.00085  6.35397E-04 0.00111  1.40980E-03 0.00075  2.41755E-03 0.00057  7.98053E-04 0.00100  6.64503E-04 0.00110  2.51694E-04 0.00180 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.63459E-01 0.00051  1.24667E-02 0.0E+00  2.82917E-02 6.7E-09  4.25244E-02 7.8E-09  1.33042E-01 1.6E-09  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 2.2E-09  3.55460E+00 4.7E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.71423E-05 9.4E-05  4.71206E-05 9.5E-05  4.99781E-05 0.00095 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.72595E-05 9.2E-05  4.72377E-05 9.2E-05  5.01026E-05 0.00095 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.61031E-03 0.00094  2.29694E-04 0.00542  1.10477E-03 0.00248  6.51179E-04 0.00321  1.43742E-03 0.00216  2.45887E-03 0.00165  8.05634E-04 0.00289  6.70361E-04 0.00316  2.52375E-04 0.00517 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.60255E-01 0.00143  1.24667E-02 0.0E+00  2.82917E-02 6.7E-09  4.25244E-02 7.7E-09  1.33042E-01 2.2E-09  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 0.0E+00  3.55460E+00 0.0E+00 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.60625E-03 0.00092  2.29638E-04 0.00532  1.10389E-03 0.00243  6.51201E-04 0.00315  1.43638E-03 0.00212  2.45877E-03 0.00162  8.04670E-04 0.00283  6.69761E-04 0.00309  2.51938E-04 0.00506 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.60104E-01 0.00141  1.24667E-02 0.0E+00  2.82917E-02 6.7E-09  4.25244E-02 7.7E-09  1.33042E-01 2.2E-09  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 0.0E+00  3.55460E+00 0.0E+00 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.61698E+02 0.00094 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.75242E-05 2.9E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.76424E-05 1.8E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.58438E-03 0.00018 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.59608E+02 0.00019 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.38320E-06 2.3E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96090E-06 2.2E-05  1.96074E-06 2.2E-05  1.98248E-06 0.00024 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.23464E-05 3.3E-05  7.24049E-05 3.3E-05  6.46298E-05 0.00036 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.03071E-01 9.3E-06 -7.64402E-02 0.00063  5.29663E-04 0.00062 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21992E+01 0.00048 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.02058E+00 2.3E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.69969E+01 1.9E-05  1.61964E+01 2.8E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.98379E-01 1.3E-05  2.58152E+00 1.4E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  4.99600E-03 3.5E-05  2.70853E-02 1.5E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.77047E-03 2.9E-05  4.93686E-02 2.6E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.77446E-03 2.7E-05  2.22833E-02 4.2E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.66618E-03 2.8E-05  5.40456E-02 4.2E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.62963E+00 3.5E-06  2.42538E+00 4.9E-10 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04483E+02 3.2E-07  2.01943E+02 1.4E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.37877E-08 2.4E-05  3.58258E-06 6.0E-06 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.91607E-01 1.3E-05  2.53215E+00 1.4E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.52207E-01 1.5E-05  5.21456E-01 1.5E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.37580E-01 1.7E-05  8.98312E-02 4.0E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.07984E-03 0.00013  2.37871E-02 0.00012 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.61326E-02 6.6E-05 -2.04739E-02 0.00012 ];
INF_SCATT5                (idx, [1:   4]) = [  3.76171E-05 0.02507  1.14160E-02 0.00020 ];
INF_SCATT6                (idx, [1:   4]) = [  7.28757E-03 0.00012 -3.10534E-02 6.8E-05 ];
INF_SCATT7                (idx, [1:   4]) = [  8.12487E-04 0.00098  1.06958E-02 0.00019 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.91655E-01 1.3E-05  2.53215E+00 1.4E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.52208E-01 1.5E-05  5.21456E-01 1.5E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.37581E-01 1.7E-05  8.98312E-02 4.0E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.07989E-03 0.00013  2.37871E-02 0.00012 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.61326E-02 6.6E-05 -2.04739E-02 0.00012 ];
INF_SCATTP5               (idx, [1:   4]) = [  3.76267E-05 0.02506  1.14160E-02 0.00020 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.28758E-03 0.00012 -3.10534E-02 6.8E-05 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.12491E-04 0.00098  1.06958E-02 0.00019 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.45179E-01 1.7E-05  1.73261E+00 1.7E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.35955E+00 1.7E-05  1.92388E-01 1.7E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.72161E-03 2.9E-05  4.93685E-02 2.6E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.66170E-02 1.9E-05  4.95978E-02 3.2E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 1.7E-09  2.60633E-09 0.63888 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  6.44948E-11 0.95431 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 2.2E-07  3.32613E-07 0.64655 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.61762E-01 1.3E-05  2.98444E-02 1.8E-05  2.28182E-04 0.00030  2.53192E+00 1.4E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.43454E-01 1.5E-05  8.75280E-03 3.4E-05  1.31201E-04 0.00039  5.21325E-01 1.5E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.40633E-01 1.7E-05 -3.05303E-03 7.6E-05  8.28779E-05 0.00047  8.97483E-02 4.0E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24868E-02 9.5E-05 -3.40697E-03 5.7E-05  4.25522E-05 0.00072  2.37446E-02 0.00012 ];
INF_S4                    (idx, [1:   8]) = [ -1.53339E-02 6.9E-05 -7.98727E-04 0.00021  1.36574E-05 0.00186 -2.04875E-02 0.00012 ];
INF_S5                    (idx, [1:   8]) = [ -2.97644E-04 0.00313  3.35261E-04 0.00046 -2.56091E-06 0.00883  1.14186E-02 0.00020 ];
INF_S6                    (idx, [1:   8]) = [  7.55381E-03 0.00011 -2.66241E-04 0.00054 -9.43582E-06 0.00220 -3.10440E-02 6.8E-05 ];
INF_S7                    (idx, [1:   8]) = [  1.28233E-03 0.00061 -4.69838E-04 0.00029 -1.12355E-05 0.00172  1.07070E-02 0.00018 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.61811E-01 1.3E-05  2.98444E-02 1.8E-05  2.28182E-04 0.00030  2.53192E+00 1.4E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.43455E-01 1.5E-05  8.75280E-03 3.4E-05  1.31201E-04 0.00039  5.21325E-01 1.5E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.40634E-01 1.7E-05 -3.05303E-03 7.6E-05  8.28779E-05 0.00047  8.97483E-02 4.0E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24869E-02 9.5E-05 -3.40697E-03 5.7E-05  4.25522E-05 0.00072  2.37446E-02 0.00012 ];
INF_SP4                   (idx, [1:   8]) = [ -1.53339E-02 6.9E-05 -7.98727E-04 0.00021  1.36574E-05 0.00186 -2.04875E-02 0.00012 ];
INF_SP5                   (idx, [1:   8]) = [ -2.97635E-04 0.00313  3.35261E-04 0.00046 -2.56091E-06 0.00883  1.14186E-02 0.00020 ];
INF_SP6                   (idx, [1:   8]) = [  7.55382E-03 0.00011 -2.66241E-04 0.00054 -9.43582E-06 0.00220 -3.10440E-02 6.8E-05 ];
INF_SP7                   (idx, [1:   8]) = [  1.28233E-03 0.00061 -4.69838E-04 0.00029 -1.12355E-05 0.00172  1.07070E-02 0.00018 ];

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

