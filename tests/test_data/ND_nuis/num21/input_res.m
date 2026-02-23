
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
START_DATE                (idx, [1: 24])  = 'Fri Jan 23 15:34:15 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Sat Jan 24 10:39:28 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.18588E+00  1.01116E+00  9.91565E-01  9.93711E-01  9.90139E-01  9.97340E-01  9.95642E-01  9.95868E-01  1.00108E+00  9.87793E-01  9.93775E-01  9.79557E-01  9.93916E-01  9.94008E-01  9.91632E-01  9.93597E-01  9.85909E-01  9.95935E-01  9.91087E-01  9.96369E-01  9.86092E-01  9.94468E-01  9.95306E-01  9.95049E-01  9.89359E-01  9.88725E-01  9.92381E-01  9.97069E-01  9.94674E-01  1.00091E+00  ];
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
TOT_COL_EFF               (idx, [1:   4]) = [  9.81075E-01 9.7E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.54210E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.54123E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.64763E+00 0.00023  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.26958E+02 0.00025  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2031236783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.38539E+05 0.00053 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00006E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.30433E+04 ;
RUNNING_TIME              (idx, 1)        =  1.14521E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.70833E-01  3.70833E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.45000E-03  9.45000E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.14483E+03  1.14483E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.14521E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85348 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88617E+01 3.1E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85776E-01 ;
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

NORM_COEF                 (idx, [1:   4]) = [  3.32923E-05 3.5E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.16555E-01 0.00010 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.37838E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.21619E-02 0.00026 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.32261E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  9.92972E-01 3.2E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.08180E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.74657E-01 2.4E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82836E-01 9.6E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98768E-01 3.5E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.30050E+01 3.1E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.71637E-02 0.00055 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.05322E+01 5.1E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.43268E+00 1.5E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02242E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  9.94338E-01 5.4E-05  9.86885E-01 5.1E-05  7.46173E-03 0.00074 ];
IMP_KEFF                  (idx, [1:   2]) = [  9.94237E-01 3.2E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  9.94203E-01 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  9.94237E-01 3.2E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.01162E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.12452E-03 0.00212  5.99268E-05 0.01030  3.06648E-04 0.00465  1.75989E-04 0.00564  3.95211E-04 0.00396  6.84309E-04 0.00319  2.36179E-04 0.00552  1.90447E-04 0.00617  7.58127E-05 0.00927 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.61115E-01 0.00077  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.59382E-03 0.00069  2.24742E-04 0.00407  1.09868E-03 0.00184  6.45475E-04 0.00237  1.43309E-03 0.00161  2.44876E-03 0.00123  8.13100E-04 0.00213  6.74966E-04 0.00234  2.55017E-04 0.00385 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.63480E-01 0.00110  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.83148E-05 0.00011  4.82912E-05 0.00011  5.14153E-05 0.00099 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.80404E-05 9.5E-05  4.80169E-05 9.6E-05  5.11231E-05 0.00099 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.50327E-03 0.00076  2.21586E-04 0.00446  1.08776E-03 0.00196  6.38260E-04 0.00257  1.41180E-03 0.00174  2.42041E-03 0.00135  8.04523E-04 0.00239  6.66810E-04 0.00254  2.52119E-04 0.00420 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.63593E-01 0.00120  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.75729E-05 0.00022  4.75507E-05 0.00022  5.04693E-05 0.00228 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.73027E-05 0.00021  4.72807E-05 0.00021  5.01825E-05 0.00228 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.62329E-03 0.00215  2.25519E-04 0.01271  1.10476E-03 0.00579  6.51995E-04 0.00761  1.44426E-03 0.00503  2.45863E-03 0.00386  8.08691E-04 0.00674  6.74270E-04 0.00723  2.55162E-04 0.01217 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.62121E-01 0.00340  1.24667E-02 5.2E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.62608E-03 0.00212  2.25095E-04 0.01248  1.10504E-03 0.00567  6.50882E-04 0.00744  1.44408E-03 0.00494  2.46281E-03 0.00378  8.08284E-04 0.00660  6.75110E-04 0.00714  2.54771E-04 0.01193 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.62129E-01 0.00335  1.24667E-02 5.2E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.60366E+02 0.00216 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.79648E-05 6.8E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.76924E-05 4.2E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.61688E-03 0.00043 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.58805E+02 0.00043 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.38560E-06 5.4E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96051E-06 4.7E-05  1.96035E-06 4.8E-05  1.98023E-06 0.00053 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.21407E-05 7.7E-05  7.21978E-05 7.8E-05  6.46868E-05 0.00086 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.03198E-01 2.2E-05 -3.25843E-02 0.00185  2.40266E-04 0.00187 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21828E+01 0.00112 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.01161E+00 5.0E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.68473E+01 4.8E-05  1.61579E+01 6.9E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  7.03431E-01 2.9E-05  2.57752E+00 3.5E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  5.05251E-03 8.5E-05  2.71703E-02 3.4E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.82303E-03 7.0E-05  4.94906E-02 6.1E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.77052E-03 6.4E-05  2.23203E-02 9.9E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.69662E-03 6.7E-05  5.36511E-02 9.9E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.65268E+00 8.5E-06  2.40369E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04521E+02 7.4E-07  2.01942E+02 7.9E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.41235E-08 5.1E-05  3.58134E-06 1.5E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.96600E-01 2.9E-05  2.52803E+00 3.6E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.54468E-01 3.3E-05  5.20609E-01 3.7E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.38463E-01 4.0E-05  8.97342E-02 8.6E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.12095E-03 0.00031  2.37602E-02 0.00028 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.62484E-02 0.00016 -2.04305E-02 0.00027 ];
INF_SCATT5                (idx, [1:   4]) = [  1.85133E-05 0.12176  1.13939E-02 0.00045 ];
INF_SCATT6                (idx, [1:   4]) = [  7.31615E-03 0.00027 -3.09785E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.11395E-04 0.00233  1.06713E-02 0.00040 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.96656E-01 2.9E-05  2.52803E+00 3.6E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.54470E-01 3.3E-05  5.20609E-01 3.7E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.38464E-01 4.0E-05  8.97343E-02 8.6E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.12117E-03 0.00031  2.37602E-02 0.00028 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.62483E-02 0.00016 -2.04305E-02 0.00027 ];
INF_SCATTP5               (idx, [1:   4]) = [  1.85459E-05 0.12157  1.13939E-02 0.00045 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.31620E-03 0.00027 -3.09785E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.11423E-04 0.00232  1.06713E-02 0.00040 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.50268E-01 3.8E-05  1.73039E+00 4.2E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.33191E+00 3.8E-05  1.92635E-01 4.2E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.76689E-03 7.2E-05  4.94900E-02 6.1E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.68460E-02 4.5E-05  4.97229E-02 8.3E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 1.1E-08  1.08599E-08 0.98420 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  9.99999E-01 1.4E-06  1.46846E-06 0.98430 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.66584E-01 2.9E-05  3.00152E-02 4.0E-05  2.29202E-04 0.00069  2.52780E+00 3.6E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.45666E-01 3.3E-05  8.80170E-03 7.6E-05  1.31732E-04 0.00097  5.20477E-01 3.7E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.41533E-01 3.9E-05 -3.07002E-03 0.00018  8.31121E-05 0.00119  8.96511E-02 8.6E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.25473E-02 0.00022 -3.42633E-03 0.00014  4.26158E-05 0.00175  2.37176E-02 0.00028 ];
INF_S4                    (idx, [1:   8]) = [ -1.54446E-02 0.00016 -8.03813E-04 0.00053  1.37080E-05 0.00428 -2.04443E-02 0.00027 ];
INF_S5                    (idx, [1:   8]) = [ -3.18447E-04 0.00692  3.36960E-04 0.00110 -2.55720E-06 0.01979  1.13964E-02 0.00045 ];
INF_S6                    (idx, [1:   8]) = [  7.58354E-03 0.00026 -2.67387E-04 0.00129 -9.47591E-06 0.00490 -3.09690E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.28324E-03 0.00144 -4.71847E-04 0.00065 -1.13273E-05 0.00413  1.06827E-02 0.00040 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.66641E-01 2.9E-05  3.00152E-02 4.0E-05  2.29203E-04 0.00069  2.52780E+00 3.6E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.45669E-01 3.3E-05  8.80170E-03 7.6E-05  1.31732E-04 0.00097  5.20477E-01 3.7E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.41534E-01 3.9E-05 -3.07002E-03 0.00018  8.31121E-05 0.00119  8.96511E-02 8.6E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.25475E-02 0.00022 -3.42633E-03 0.00014  4.26158E-05 0.00175  2.37176E-02 0.00028 ];
INF_SP4                   (idx, [1:   8]) = [ -1.54445E-02 0.00016 -8.03813E-04 0.00053  1.37080E-05 0.00428 -2.04443E-02 0.00027 ];
INF_SP5                   (idx, [1:   8]) = [ -3.18414E-04 0.00692  3.36960E-04 0.00110 -2.55720E-06 0.01979  1.13964E-02 0.00045 ];
INF_SP6                   (idx, [1:   8]) = [  7.58359E-03 0.00026 -2.67387E-04 0.00129 -9.47591E-06 0.00490 -3.09690E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.28327E-03 0.00144 -4.71847E-04 0.00065 -1.13273E-05 0.00413  1.06827E-02 0.00040 ];

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

