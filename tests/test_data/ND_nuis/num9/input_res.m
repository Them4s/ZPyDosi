
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
START_DATE                (idx, [1: 24])  = 'Sun Jan 18 17:52:01 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Mon Jan 19 12:51:06 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.24435E+00  1.00343E+00  9.93669E-01  9.90234E-01  9.84528E-01  9.78127E-01  9.89494E-01  1.00029E+00  9.84571E-01  9.94116E-01  9.94937E-01  9.90518E-01  9.94252E-01  9.88107E-01  9.98080E-01  9.89606E-01  9.93032E-01  9.90066E-01  9.98754E-01  1.00386E+00  9.97758E-01  9.90890E-01  9.89676E-01  9.86708E-01  9.89248E-01  9.94725E-01  9.80755E-01  9.88735E-01  9.85450E-01  9.92039E-01  ];
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
TOT_COL_EFF               (idx, [1:   4]) = [  9.81189E-01 9.7E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.51430E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.51340E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.63216E+00 0.00022  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.26422E+02 0.00025  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2031641969 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.38607E+05 0.00054 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00006E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.28631E+04 ;
RUNNING_TIME              (idx, 1)        =  1.13908E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.72917E-01  3.72917E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.33333E-03  9.33333E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.13870E+03  1.13870E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.13908E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85041 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88586E+01 3.2E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85674E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.19 ;

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

NORM_COEF                 (idx, [1:   4]) = [  3.32929E-05 3.5E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.09198E-01 0.00010 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.38529E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.14709E-02 0.00026 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.32836E-11 3.3E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.00119E+00 3.3E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.09959E-01 3.3E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.72944E-01 2.4E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82903E-01 9.6E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98787E-01 3.5E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.30323E+01 3.2E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.70966E-02 0.00055 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.05132E+01 5.2E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.44216E+00 1.4E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02238E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.00254E+00 5.5E-05  9.95022E-01 5.2E-05  7.49853E-03 0.00075 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.00246E+00 3.3E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.00241E+00 4.6E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.00246E+00 3.3E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.01992E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.13621E-03 0.00208  6.01566E-05 0.00893  3.09624E-04 0.00433  1.76521E-04 0.00546  3.98802E-04 0.00391  6.88992E-04 0.00322  2.33593E-04 0.00544  1.93144E-04 0.00569  7.53777E-05 0.01035 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.60613E-01 0.00077  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.55917E-03 0.00071  2.24561E-04 0.00405  1.09540E-03 0.00187  6.44198E-04 0.00243  1.42381E-03 0.00164  2.43891E-03 0.00123  8.09496E-04 0.00221  6.69918E-04 0.00239  2.52879E-04 0.00385 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.62692E-01 0.00110  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.80471E-05 0.00011  4.80245E-05 0.00011  5.10299E-05 0.00101 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.81683E-05 9.5E-05  4.81456E-05 9.5E-05  5.11589E-05 0.00101 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.47956E-03 0.00076  2.22192E-04 0.00445  1.08014E-03 0.00199  6.38897E-04 0.00267  1.40849E-03 0.00176  2.41384E-03 0.00134  8.03179E-04 0.00236  6.62878E-04 0.00260  2.49935E-04 0.00425 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.62792E-01 0.00121  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.73073E-05 0.00022  4.72846E-05 0.00022  5.02726E-05 0.00225 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.74266E-05 0.00021  4.74039E-05 0.00022  5.03991E-05 0.00225 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.58330E-03 0.00222  2.30754E-04 0.01283  1.09273E-03 0.00590  6.58674E-04 0.00761  1.43029E-03 0.00510  2.45170E-03 0.00393  8.02507E-04 0.00690  6.67754E-04 0.00747  2.48893E-04 0.01211 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.58866E-01 0.00346  1.24667E-02 5.2E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.58629E-03 0.00218  2.32047E-04 0.01260  1.09319E-03 0.00576  6.59599E-04 0.00748  1.43049E-03 0.00503  2.45286E-03 0.00385  8.02611E-04 0.00673  6.66707E-04 0.00733  2.48786E-04 0.01184 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.58434E-01 0.00338  1.24667E-02 5.2E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.60429E+02 0.00223 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.76838E-05 7.0E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.78040E-05 4.3E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.57596E-03 0.00044 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.58884E+02 0.00044 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.38681E-06 5.4E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96495E-06 5.0E-05  1.96481E-06 5.0E-05  1.98335E-06 0.00054 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.22159E-05 7.8E-05  7.22722E-05 7.9E-05  6.48430E-05 0.00087 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.03534E-01 2.2E-05 -3.22771E-02 0.00189  2.36975E-04 0.00191 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21883E+01 0.00112 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.01985E+00 5.5E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.68516E+01 4.6E-05  1.61808E+01 7.0E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  7.01289E-01 3.0E-05  2.57607E+00 3.1E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  5.02673E-03 8.2E-05  2.70674E-02 3.4E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.81057E-03 6.8E-05  4.94436E-02 6.1E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.78384E-03 6.3E-05  2.23761E-02 0.00010 ];
INF_NSF                   (idx, [1:   4]) = [  4.70128E-03 6.4E-05  5.40738E-02 0.00010 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.63548E+00 8.9E-06  2.41659E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04484E+02 7.4E-07  2.01942E+02 8.0E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.42679E-08 5.5E-05  3.58158E-06 1.4E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.94468E-01 3.1E-05  2.52662E+00 3.3E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.53260E-01 3.4E-05  5.20315E-01 3.6E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.37876E-01 4.1E-05  8.96681E-02 9.1E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.00302E-03 0.00032  2.37491E-02 0.00028 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.62668E-02 0.00015 -2.04167E-02 0.00029 ];
INF_SCATT5                (idx, [1:   4]) = [ -1.35901E-05 0.15583  1.13816E-02 0.00047 ];
INF_SCATT6                (idx, [1:   4]) = [  7.28071E-03 0.00028 -3.09648E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.07341E-04 0.00246  1.06621E-02 0.00043 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.94524E-01 3.1E-05  2.52662E+00 3.3E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.53263E-01 3.4E-05  5.20315E-01 3.6E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.37877E-01 4.1E-05  8.96681E-02 9.1E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.00316E-03 0.00032  2.37491E-02 0.00028 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.62668E-02 0.00015 -2.04167E-02 0.00029 ];
INF_SCATTP5               (idx, [1:   4]) = [ -1.35724E-05 0.15606  1.13816E-02 0.00047 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.28075E-03 0.00028 -3.09648E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.07349E-04 0.00246  1.06621E-02 0.00043 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.52068E-01 4.0E-05  1.72959E+00 3.6E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.32240E+00 4.0E-05  1.92724E-01 3.6E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.75460E-03 6.9E-05  4.94429E-02 6.1E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.68436E-02 4.2E-05  4.96754E-02 7.6E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 9.3E-10  6.95935E-10 0.78513 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 7.4E-08  9.37846E-08 0.78896 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.64445E-01 3.0E-05  3.00233E-02 4.0E-05  2.28599E-04 0.00066  2.52639E+00 3.3E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.44455E-01 3.4E-05  8.80524E-03 8.5E-05  1.31107E-04 0.00089  5.20184E-01 3.6E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.40947E-01 4.0E-05 -3.07115E-03 0.00019  8.27823E-05 0.00105  8.95853E-02 9.1E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24310E-02 0.00022 -3.42793E-03 0.00014  4.24480E-05 0.00156  2.37067E-02 0.00028 ];
INF_S4                    (idx, [1:   8]) = [ -1.54632E-02 0.00015 -8.03610E-04 0.00054  1.35779E-05 0.00450 -2.04303E-02 0.00029 ];
INF_S5                    (idx, [1:   8]) = [ -3.50838E-04 0.00587  3.37248E-04 0.00113 -2.54491E-06 0.01991  1.13841E-02 0.00047 ];
INF_S6                    (idx, [1:   8]) = [  7.54827E-03 0.00027 -2.67560E-04 0.00134 -9.42216E-06 0.00494 -3.09554E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.27945E-03 0.00155 -4.72110E-04 0.00071 -1.12412E-05 0.00405  1.06733E-02 0.00043 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.64501E-01 3.1E-05  3.00233E-02 4.0E-05  2.28600E-04 0.00066  2.52640E+00 3.3E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.44458E-01 3.4E-05  8.80524E-03 8.5E-05  1.31107E-04 0.00089  5.20184E-01 3.6E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.40948E-01 4.0E-05 -3.07115E-03 0.00019  8.27823E-05 0.00105  8.95853E-02 9.1E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24311E-02 0.00022 -3.42794E-03 0.00014  4.24480E-05 0.00156  2.37067E-02 0.00028 ];
INF_SP4                   (idx, [1:   8]) = [ -1.54632E-02 0.00015 -8.03610E-04 0.00054  1.35779E-05 0.00450 -2.04303E-02 0.00029 ];
INF_SP5                   (idx, [1:   8]) = [ -3.50821E-04 0.00587  3.37248E-04 0.00113 -2.54491E-06 0.01991  1.13841E-02 0.00047 ];
INF_SP6                   (idx, [1:   8]) = [  7.54831E-03 0.00027 -2.67561E-04 0.00134 -9.42217E-06 0.00494 -3.09554E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.27946E-03 0.00155 -4.72110E-04 0.00071 -1.12412E-05 0.00405  1.06733E-02 0.00043 ];

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

