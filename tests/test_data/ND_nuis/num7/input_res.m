
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
START_DATE                (idx, [1: 24])  = 'Sat Jan 17 22:06:23 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Sun Jan 18 17:51:59 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.22301E+00  1.01065E+00  1.01892E+00  9.91634E-01  9.91327E-01  9.89710E-01  9.90722E-01  9.96249E-01  9.88987E-01  9.90913E-01  9.87705E-01  9.92298E-01  9.97356E-01  9.97086E-01  9.96791E-01  9.92255E-01  9.98024E-01  9.91388E-01  9.93836E-01  9.94344E-01  9.94658E-01  9.84963E-01  9.93766E-01  9.86104E-01  9.86193E-01  9.80856E-01  9.88578E-01  9.87084E-01  9.87227E-01  9.77371E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 71])  = '/home/thomasligonnet/Documents/XS/xs_lib/jeff33_modif_eurofusion/xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1:  3])  = 'N/A' ;
SFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
NFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  2.95583E-01 1.3E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  0.00000E+00  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TMS_SAMPLING_EFF          (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  9.80312E-01 9.8E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.51917E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.51820E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.71072E+00 0.00022  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.26426E+02 0.00024  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2115402299 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.52567E+05 0.00051 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.42113E+04 ;
RUNNING_TIME              (idx, 1)        =  1.18559E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.74367E-01  3.74367E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.28333E-03  9.28333E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.18521E+03  1.18521E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.18559E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85584 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88636E+01 3.0E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85789E-01 ;
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

NORM_COEF                 (idx, [1:   4]) = [  3.32921E-05 3.3E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.19729E-01 9.8E-05 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.38323E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.16774E-02 0.00025 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.31704E-11 3.1E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  9.93132E-01 3.1E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.06465E-01 3.1E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.75688E-01 2.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82153E-01 9.0E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98762E-01 3.3E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.33042E+01 3.0E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.78472E-02 0.00050 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.05215E+01 4.9E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.44334E+00 1.3E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02240E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  9.94361E-01 5.2E-05  9.86906E-01 4.9E-05  7.45920E-03 0.00072 ];
IMP_KEFF                  (idx, [1:   2]) = [  9.94409E-01 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  9.94369E-01 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  9.94409E-01 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.01250E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  1.98016E-03 0.00199  5.55593E-05 0.00846  2.85647E-04 0.00417  1.64314E-04 0.00577  3.69164E-04 0.00375  6.37519E-04 0.00299  2.17857E-04 0.00502  1.78876E-04 0.00535  7.12205E-05 0.00949 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.61051E-01 0.00075  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.57620E-03 0.00068  2.23500E-04 0.00391  1.09588E-03 0.00179  6.48153E-04 0.00235  1.42927E-03 0.00156  2.44583E-03 0.00119  8.08102E-04 0.00209  6.72907E-04 0.00235  2.52561E-04 0.00376 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.62373E-01 0.00106  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.81919E-05 0.00010  4.81696E-05 0.00010  5.11106E-05 0.00095 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.79194E-05 9.0E-05  4.78972E-05 9.1E-05  5.08216E-05 0.00095 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.50101E-03 0.00074  2.21460E-04 0.00425  1.08456E-03 0.00197  6.41464E-04 0.00258  1.41676E-03 0.00169  2.41944E-03 0.00128  8.01292E-04 0.00227  6.64978E-04 0.00254  2.51052E-04 0.00417 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.62561E-01 0.00117  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.74829E-05 0.00022  4.74613E-05 0.00022  5.02758E-05 0.00218 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.72144E-05 0.00021  4.71929E-05 0.00021  4.99918E-05 0.00218 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.62930E-03 0.00212  2.27151E-04 0.01210  1.10651E-03 0.00561  6.53489E-04 0.00717  1.44730E-03 0.00485  2.46151E-03 0.00376  8.17429E-04 0.00655  6.71103E-04 0.00727  2.44803E-04 0.01168 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.56871E-01 0.00332  1.24667E-02 5.0E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.63066E-03 0.00207  2.27385E-04 0.01197  1.10534E-03 0.00552  6.53058E-04 0.00705  1.44891E-03 0.00475  2.46404E-03 0.00368  8.17224E-04 0.00641  6.68070E-04 0.00715  2.46633E-04 0.01148 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.57136E-01 0.00327  1.24667E-02 5.0E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.60789E+02 0.00213 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.78384E-05 6.5E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.75679E-05 4.1E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.61313E-03 0.00042 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.59147E+02 0.00042 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.37553E-06 5.1E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96242E-06 4.8E-05  1.96226E-06 4.8E-05  1.98280E-06 0.00054 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.21960E-05 7.4E-05  7.22548E-05 7.4E-05  6.44871E-05 0.00081 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.02285E-01 2.1E-05 -3.50835E-02 0.00175  2.56492E-04 0.00177 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21825E+01 0.00108 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.01245E+00 5.1E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.71546E+01 4.5E-05  1.61498E+01 6.3E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.93998E-01 3.1E-05  2.58063E+00 3.2E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  4.98478E-03 8.3E-05  2.72656E-02 3.1E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.75283E-03 6.8E-05  4.94614E-02 5.4E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.76805E-03 6.3E-05  2.21958E-02 8.8E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.64004E-03 6.5E-05  5.36937E-02 8.8E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.62439E+00 8.1E-06  2.41909E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04465E+02 7.4E-07  2.01942E+02 7.8E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.34094E-08 5.5E-05  3.58180E-06 1.3E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.87236E-01 3.1E-05  2.53117E+00 3.3E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.49917E-01 3.5E-05  5.21644E-01 3.6E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.36710E-01 4.0E-05  8.98846E-02 9.3E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.06069E-03 0.00028  2.37972E-02 0.00027 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.59977E-02 0.00015 -2.04838E-02 0.00028 ];
INF_SCATT5                (idx, [1:   4]) = [  5.24491E-05 0.04295  1.14167E-02 0.00047 ];
INF_SCATT6                (idx, [1:   4]) = [  7.24687E-03 0.00028 -3.10559E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.11817E-04 0.00216  1.06936E-02 0.00042 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.87292E-01 3.1E-05  2.53117E+00 3.3E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.49920E-01 3.5E-05  5.21644E-01 3.6E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.36711E-01 4.0E-05  8.98846E-02 9.3E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.06089E-03 0.00028  2.37972E-02 0.00027 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.59976E-02 0.00015 -2.04838E-02 0.00028 ];
INF_SCATTP5               (idx, [1:   4]) = [  5.24651E-05 0.04292  1.14167E-02 0.00047 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.24688E-03 0.00028 -3.10559E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.11834E-04 0.00216  1.06936E-02 0.00042 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.43119E-01 4.1E-05  1.73104E+00 3.8E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.37107E+00 4.1E-05  1.92563E-01 3.8E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.69642E-03 6.8E-05  4.94607E-02 5.4E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.64035E-02 4.2E-05  4.96924E-02 7.2E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 2.0E-09  2.64887E-09 0.71558 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  3.04981E-11 1.00000 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 2.6E-07  3.56914E-07 0.72497 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.57595E-01 3.1E-05  2.96411E-02 4.2E-05  2.28131E-04 0.00065  2.53094E+00 3.3E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.41220E-01 3.5E-05  8.69757E-03 7.4E-05  1.31413E-04 0.00086  5.21512E-01 3.6E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.39742E-01 3.9E-05 -3.03264E-03 0.00017  8.30958E-05 0.00107  8.98015E-02 9.3E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24446E-02 0.00020 -3.38394E-03 0.00012  4.26569E-05 0.00167  2.37545E-02 0.00027 ];
INF_S4                    (idx, [1:   8]) = [ -1.52044E-02 0.00016 -7.93314E-04 0.00049  1.36867E-05 0.00426 -2.04975E-02 0.00028 ];
INF_S5                    (idx, [1:   8]) = [ -2.80050E-04 0.00787  3.32499E-04 0.00103 -2.55487E-06 0.02150  1.14193E-02 0.00047 ];
INF_S6                    (idx, [1:   8]) = [  7.51213E-03 0.00027 -2.65262E-04 0.00120 -9.47191E-06 0.00565 -3.10465E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.27846E-03 0.00134 -4.66644E-04 0.00066 -1.12687E-05 0.00418  1.07049E-02 0.00042 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.57651E-01 3.1E-05  2.96411E-02 4.2E-05  2.28132E-04 0.00065  2.53094E+00 3.3E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.41223E-01 3.5E-05  8.69757E-03 7.4E-05  1.31413E-04 0.00086  5.21512E-01 3.6E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.39744E-01 3.9E-05 -3.03264E-03 0.00017  8.30958E-05 0.00107  8.98015E-02 9.3E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24448E-02 0.00020 -3.38395E-03 0.00012  4.26569E-05 0.00167  2.37546E-02 0.00027 ];
INF_SP4                   (idx, [1:   8]) = [ -1.52043E-02 0.00016 -7.93315E-04 0.00049  1.36866E-05 0.00426 -2.04975E-02 0.00028 ];
INF_SP5                   (idx, [1:   8]) = [ -2.80034E-04 0.00786  3.32500E-04 0.00103 -2.55489E-06 0.02150  1.14193E-02 0.00047 ];
INF_SP6                   (idx, [1:   8]) = [  7.51215E-03 0.00027 -2.65262E-04 0.00120 -9.47191E-06 0.00565 -3.10465E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.27848E-03 0.00134 -4.66644E-04 0.00066 -1.12687E-05 0.00418  1.07049E-02 0.00042 ];

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

