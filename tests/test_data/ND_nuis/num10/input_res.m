
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
START_DATE                (idx, [1: 24])  = 'Sun Jan 18 18:34:12 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Mon Jan 19 14:17:40 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.19632E+00  1.01634E+00  9.92289E-01  9.85823E-01  1.00486E+00  9.90759E-01  9.93857E-01  9.98908E-01  9.99936E-01  9.92178E-01  9.91462E-01  9.98189E-01  9.88099E-01  9.84156E-01  9.89724E-01  1.00139E+00  9.88041E-01  9.96249E-01  9.87140E-01  9.85267E-01  9.98167E-01  9.97920E-01  9.90826E-01  9.93177E-01  9.92674E-01  9.90027E-01  9.84657E-01  9.94202E-01  9.91264E-01  9.86091E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 71])  = '/home/thomasligonnet/Documents/XS/xs_lib/jeff33_modif_eurofusion/xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1:  3])  = 'N/A' ;
SFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
NFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  2.95583E-01 1.8E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  0.00000E+00  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TMS_SAMPLING_EFF          (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  9.80608E-01 9.4E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.50192E+01 0.00021  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.50095E+01 0.00021  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.68107E+00 0.00020  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.27154E+02 0.00024  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2100650728 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.50108E+05 0.00050 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.41516E+04 ;
RUNNING_TIME              (idx, 1)        =  1.18346E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.72483E-01  3.72483E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.01666E-03  9.01666E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.18308E+03  1.18308E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.18346E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85748 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88650E+01 3.0E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85834E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.26 ;

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

NORM_COEF                 (idx, [1:   4]) = [  3.32918E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.12451E-01 9.8E-05 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.37181E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.28191E-02 0.00025 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.32451E-11 3.1E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  9.96416E-01 3.1E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.08759E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.73430E-01 2.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82189E-01 9.3E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98753E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.33462E+01 3.1E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.78115E-02 0.00051 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.03825E+01 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.43766E+00 1.3E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02245E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  9.97779E-01 5.2E-05  9.90231E-01 5.0E-05  7.52481E-03 0.00071 ];
IMP_KEFF                  (idx, [1:   2]) = [  9.97682E-01 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  9.97667E-01 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  9.97682E-01 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.01580E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.04154E-03 0.00212  5.91483E-05 0.01015  2.93966E-04 0.00424  1.69102E-04 0.00623  3.79712E-04 0.00388  6.57735E-04 0.00325  2.23759E-04 0.00556  1.83939E-04 0.00598  7.41810E-05 0.00864 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.62248E-01 0.00075  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.60472E-03 0.00068  2.26550E-04 0.00405  1.09597E-03 0.00177  6.45384E-04 0.00238  1.43383E-03 0.00160  2.45645E-03 0.00120  8.13177E-04 0.00206  6.76479E-04 0.00234  2.56887E-04 0.00376 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.64369E-01 0.00107  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.78281E-05 0.00011  4.78052E-05 0.00011  5.08067E-05 0.00099 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.77211E-05 9.3E-05  4.76983E-05 9.3E-05  5.06928E-05 0.00099 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.54065E-03 0.00073  2.24658E-04 0.00429  1.08513E-03 0.00193  6.41437E-04 0.00258  1.42422E-03 0.00170  2.43623E-03 0.00130  8.05671E-04 0.00227  6.70674E-04 0.00250  2.52643E-04 0.00409 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.63361E-01 0.00115  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.71117E-05 0.00022  4.70900E-05 0.00022  4.99160E-05 0.00220 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.70063E-05 0.00021  4.69847E-05 0.00021  4.98046E-05 0.00220 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.65587E-03 0.00214  2.30675E-04 0.01225  1.11479E-03 0.00555  6.53532E-04 0.00732  1.44529E-03 0.00495  2.46688E-03 0.00374  8.10530E-04 0.00663  6.82842E-04 0.00726  2.51330E-04 0.01187 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.60452E-01 0.00334  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.65489E-03 0.00210  2.31108E-04 0.01197  1.11572E-03 0.00544  6.54173E-04 0.00721  1.44458E-03 0.00484  2.46582E-03 0.00366  8.09589E-04 0.00648  6.82433E-04 0.00714  2.51461E-04 0.01170 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.60201E-01 0.00329  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.62625E+02 0.00216 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.74739E-05 6.8E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.73676E-05 4.1E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.64207E-03 0.00043 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.60979E+02 0.00043 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.37389E-06 5.3E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96353E-06 4.8E-05  1.96336E-06 4.8E-05  1.98465E-06 0.00054 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.20843E-05 7.5E-05  7.21435E-05 7.5E-05  6.43608E-05 0.00084 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.03300E-01 2.1E-05 -3.39141E-02 0.00184  2.49631E-04 0.00186 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21862E+01 0.00110 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.01581E+00 5.4E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.71995E+01 4.5E-05  1.61469E+01 6.2E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.89531E-01 3.0E-05  2.57808E+00 3.1E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  4.91956E-03 7.6E-05  2.72266E-02 3.1E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.70607E-03 6.2E-05  4.95324E-02 5.7E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.78651E-03 6.2E-05  2.23058E-02 9.4E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.66266E-03 6.4E-05  5.38557E-02 9.4E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.60992E+00 8.0E-06  2.41442E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04495E+02 6.9E-07  2.01942E+02 7.8E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.34220E-08 5.5E-05  3.58140E-06 1.3E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.82816E-01 3.0E-05  2.52855E+00 3.3E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.49968E-01 3.5E-05  5.21705E-01 3.5E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.36724E-01 3.9E-05  8.99326E-02 8.7E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.09225E-03 0.00029  2.38259E-02 0.00029 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.59860E-02 0.00015 -2.04904E-02 0.00028 ];
INF_SCATT5                (idx, [1:   4]) = [  5.13942E-05 0.04104  1.14155E-02 0.00045 ];
INF_SCATT6                (idx, [1:   4]) = [  7.24726E-03 0.00028 -3.10726E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.07769E-04 0.00236  1.06911E-02 0.00042 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.82872E-01 3.0E-05  2.52855E+00 3.3E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.49970E-01 3.5E-05  5.21705E-01 3.5E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.36725E-01 3.9E-05  8.99326E-02 8.7E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.09243E-03 0.00029  2.38259E-02 0.00029 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.59860E-02 0.00015 -2.04904E-02 0.00028 ];
INF_SCATTP5               (idx, [1:   4]) = [  5.14301E-05 0.04102  1.14155E-02 0.00045 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.24730E-03 0.00028 -3.10726E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.07747E-04 0.00236  1.06911E-02 0.00042 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.40338E-01 3.7E-05  1.72786E+00 3.9E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.38693E+00 3.7E-05  1.92917E-01 3.9E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.65030E-03 6.3E-05  4.95317E-02 5.7E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.63432E-02 4.1E-05  4.97606E-02 6.8E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  3.81199E-10 0.83986 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 4.2E-08  5.03784E-08 0.83746 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.53188E-01 3.0E-05  2.96286E-02 4.2E-05  2.27200E-04 0.00067  2.52832E+00 3.3E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.41267E-01 3.5E-05  8.70067E-03 7.5E-05  1.31208E-04 0.00088  5.21574E-01 3.5E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.39757E-01 3.8E-05 -3.03343E-03 0.00017  8.31154E-05 0.00102  8.98495E-02 8.7E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24772E-02 0.00021 -3.38490E-03 0.00013  4.26194E-05 0.00148  2.37833E-02 0.00029 ];
INF_S4                    (idx, [1:   8]) = [ -1.51927E-02 0.00016 -7.93323E-04 0.00049  1.36361E-05 0.00371 -2.05041E-02 0.00028 ];
INF_S5                    (idx, [1:   8]) = [ -2.82293E-04 0.00749  3.33687E-04 0.00108 -2.54512E-06 0.01857  1.14181E-02 0.00045 ];
INF_S6                    (idx, [1:   8]) = [  7.51157E-03 0.00027 -2.64306E-04 0.00134 -9.46128E-06 0.00481 -3.10631E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.27452E-03 0.00146 -4.66747E-04 0.00067 -1.13069E-05 0.00363  1.07024E-02 0.00042 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.53243E-01 3.0E-05  2.96286E-02 4.2E-05  2.27200E-04 0.00067  2.52832E+00 3.3E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.41270E-01 3.5E-05  8.70067E-03 7.5E-05  1.31208E-04 0.00088  5.21574E-01 3.5E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.39759E-01 3.8E-05 -3.03343E-03 0.00017  8.31154E-05 0.00102  8.98495E-02 8.7E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24773E-02 0.00021 -3.38490E-03 0.00013  4.26194E-05 0.00148  2.37833E-02 0.00029 ];
INF_SP4                   (idx, [1:   8]) = [ -1.51927E-02 0.00016 -7.93323E-04 0.00049  1.36361E-05 0.00371 -2.05041E-02 0.00028 ];
INF_SP5                   (idx, [1:   8]) = [ -2.82257E-04 0.00750  3.33687E-04 0.00108 -2.54512E-06 0.01857  1.14181E-02 0.00045 ];
INF_SP6                   (idx, [1:   8]) = [  7.51161E-03 0.00027 -2.64306E-04 0.00134 -9.46128E-06 0.00481 -3.10631E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.27449E-03 0.00146 -4.66747E-04 0.00067 -1.13069E-05 0.00363  1.07024E-02 0.00042 ];

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

