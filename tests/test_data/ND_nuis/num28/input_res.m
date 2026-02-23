
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
START_DATE                (idx, [1: 24])  = 'Mon Jan 26 03:05:05 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Mon Jan 26 22:22:28 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.19465E+00  1.01127E+00  9.91962E-01  9.91766E-01  9.89055E-01  9.80821E-01  9.88323E-01  9.93418E-01  9.93379E-01  9.91718E-01  9.91556E-01  9.99322E-01  9.91547E-01  9.98038E-01  9.88208E-01  9.95351E-01  9.88476E-01  9.95371E-01  9.92802E-01  9.90355E-01  9.99376E-01  1.00242E+00  9.85859E-01  9.90671E-01  9.89884E-01  9.96733E-01  9.88820E-01  9.96784E-01  9.96347E-01  9.95713E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 71])  = '/home/thomasligonnet/Documents/XS/xs_lib/jeff33_modif_eurofusion/xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1:  3])  = 'N/A' ;
SFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
NFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  2.95583E-01 1.7E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  0.00000E+00  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TMS_SAMPLING_EFF          (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  9.81018E-01 9.3E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.58006E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.57918E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.66000E+00 0.00022  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.25083E+02 0.00025  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2063965552 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.43994E+05 0.00052 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.33969E+04 ;
RUNNING_TIME              (idx, 1)        =  1.15739E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.73550E-01  3.73550E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  8.91666E-03  8.91666E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.15701E+03  1.15701E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.15739E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85533 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88634E+01 3.2E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85567E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.15 ;

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

CONVERSION_RATIO          (idx, [1:   2]) = [  5.11069E-01 0.00010 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.40989E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  5.90112E-02 0.00027 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.34388E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.01441E+00 3.2E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.14774E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.68076E-01 2.4E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82850E-01 9.5E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98714E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.30177E+01 3.1E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.71501E-02 0.00055 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.12029E+01 5.3E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.44569E+00 1.2E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02227E+02 1.3E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.01567E+00 5.4E-05  1.00811E+00 5.1E-05  7.57477E-03 0.00074 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.01567E+00 3.2E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.01572E+00 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.01567E+00 3.2E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03342E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.05910E-03 0.00185  6.05491E-05 0.00877  2.98077E-04 0.00423  1.72144E-04 0.00558  3.84163E-04 0.00368  6.62027E-04 0.00284  2.23555E-04 0.00476  1.85754E-04 0.00576  7.28314E-05 0.00901 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.58882E-01 0.00076  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.51744E-03 0.00069  2.27511E-04 0.00409  1.08962E-03 0.00181  6.41181E-04 0.00241  1.41530E-03 0.00160  2.42916E-03 0.00121  7.99833E-04 0.00212  6.64412E-04 0.00234  2.50418E-04 0.00395 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.61451E-01 0.00111  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.78767E-05 0.00011  4.78563E-05 0.00011  5.05771E-05 0.00102 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.86262E-05 9.5E-05  4.86054E-05 9.5E-05  5.13688E-05 0.00102 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.45621E-03 0.00076  2.24504E-04 0.00443  1.07813E-03 0.00199  6.36500E-04 0.00261  1.40388E-03 0.00174  2.41112E-03 0.00132  7.93177E-04 0.00231  6.60391E-04 0.00255  2.48502E-04 0.00424 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.61850E-01 0.00119  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.70825E-05 0.00022  4.70625E-05 0.00022  4.96950E-05 0.00230 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.78195E-05 0.00021  4.77993E-05 0.00021  5.04732E-05 0.00230 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.58941E-03 0.00219  2.37645E-04 0.01231  1.10066E-03 0.00567  6.57061E-04 0.00757  1.43641E-03 0.00497  2.44362E-03 0.00382  7.98169E-04 0.00670  6.68570E-04 0.00727  2.47284E-04 0.01198 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.57498E-01 0.00338  1.24667E-02 5.0E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.58620E-03 0.00214  2.37253E-04 0.01210  1.09966E-03 0.00554  6.57449E-04 0.00737  1.43637E-03 0.00489  2.44200E-03 0.00375  7.98820E-04 0.00659  6.68322E-04 0.00709  2.46319E-04 0.01175 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.57033E-01 0.00329  1.24667E-02 5.0E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.61314E+02 0.00221 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.74807E-05 6.8E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.82240E-05 4.2E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.55389E-03 0.00042 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.59098E+02 0.00043 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.40554E-06 5.4E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.95778E-06 4.9E-05  1.95764E-06 4.9E-05  1.97678E-06 0.00054 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.31127E-05 7.9E-05  7.31706E-05 7.9E-05  6.54615E-05 0.00089 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.04558E-01 2.2E-05 -3.30413E-02 0.00177  2.40717E-04 0.00179 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.22158E+01 0.00113 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.03347E+00 5.4E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.66372E+01 4.6E-05  1.63806E+01 7.0E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  7.08783E-01 3.0E-05  2.58374E+00 3.2E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  5.05764E-03 8.0E-05  2.64556E-02 3.5E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.82348E-03 6.5E-05  4.89053E-02 6.3E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.76585E-03 6.4E-05  2.24497E-02 0.00010 ];
INF_NSF                   (idx, [1:   4]) = [  4.62701E-03 6.6E-05  5.44037E-02 0.00010 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.62028E+00 8.3E-06  2.42336E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04456E+02 7.3E-07  2.01942E+02 7.8E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.46198E-08 5.5E-05  3.58610E-06 1.4E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  7.01952E-01 3.1E-05  2.53484E+00 3.3E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.56798E-01 3.5E-05  5.21459E-01 3.6E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.39231E-01 3.8E-05  8.97363E-02 8.8E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.02079E-03 0.00032  2.37532E-02 0.00029 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.64861E-02 0.00016 -2.04958E-02 0.00030 ];
INF_SCATT5                (idx, [1:   4]) = [ -1.46183E-05 0.15426  1.14373E-02 0.00046 ];
INF_SCATT6                (idx, [1:   4]) = [  7.36865E-03 0.00028 -3.10845E-02 0.00017 ];
INF_SCATT7                (idx, [1:   4]) = [  8.16438E-04 0.00228  1.07288E-02 0.00039 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  7.02007E-01 3.1E-05  2.53484E+00 3.3E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.56801E-01 3.5E-05  5.21459E-01 3.6E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.39232E-01 3.8E-05  8.97363E-02 8.8E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.02099E-03 0.00032  2.37532E-02 0.00029 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.64860E-02 0.00016 -2.04958E-02 0.00030 ];
INF_SCATTP5               (idx, [1:   4]) = [ -1.46142E-05 0.15427  1.14373E-02 0.00046 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.36867E-03 0.00028 -3.10845E-02 0.00017 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.16456E-04 0.00228  1.07288E-02 0.00039 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.51283E-01 4.2E-05  1.73522E+00 3.9E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.32652E+00 4.2E-05  1.92099E-01 3.9E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.76797E-03 6.6E-05  4.89046E-02 6.3E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.71329E-02 4.5E-05  4.91306E-02 7.6E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 6.6E-10  9.46775E-11 0.73372 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 9.0E-09  1.23423E-08 0.72999 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.71650E-01 3.0E-05  3.03014E-02 4.2E-05  2.26393E-04 0.00066  2.53461E+00 3.3E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.47912E-01 3.5E-05  8.88595E-03 8.3E-05  1.30192E-04 0.00088  5.21329E-01 3.6E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.42330E-01 3.7E-05 -3.09870E-03 0.00019  8.21161E-05 0.00103  8.96542E-02 8.8E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24796E-02 0.00023 -3.45884E-03 0.00013  4.20429E-05 0.00172  2.37111E-02 0.00029 ];
INF_S4                    (idx, [1:   8]) = [ -1.56750E-02 0.00017 -8.11144E-04 0.00053  1.34229E-05 0.00441 -2.05092E-02 0.00030 ];
INF_S5                    (idx, [1:   8]) = [ -3.54915E-04 0.00622  3.40296E-04 0.00110 -2.65337E-06 0.01976  1.14400E-02 0.00046 ];
INF_S6                    (idx, [1:   8]) = [  7.63894E-03 0.00027 -2.70283E-04 0.00129 -9.42455E-06 0.00505 -3.10751E-02 0.00017 ];
INF_S7                    (idx, [1:   8]) = [  1.29309E-03 0.00143 -4.76652E-04 0.00070 -1.11779E-05 0.00379  1.07400E-02 0.00039 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.71706E-01 3.0E-05  3.03014E-02 4.2E-05  2.26393E-04 0.00066  2.53461E+00 3.3E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.47915E-01 3.5E-05  8.88596E-03 8.3E-05  1.30192E-04 0.00088  5.21329E-01 3.6E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.42331E-01 3.7E-05 -3.09870E-03 0.00019  8.21161E-05 0.00103  8.96542E-02 8.8E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24798E-02 0.00023 -3.45884E-03 0.00013  4.20429E-05 0.00172  2.37111E-02 0.00029 ];
INF_SP4                   (idx, [1:   8]) = [ -1.56749E-02 0.00017 -8.11144E-04 0.00053  1.34229E-05 0.00441 -2.05092E-02 0.00030 ];
INF_SP5                   (idx, [1:   8]) = [ -3.54911E-04 0.00622  3.40296E-04 0.00110 -2.65338E-06 0.01976  1.14400E-02 0.00046 ];
INF_SP6                   (idx, [1:   8]) = [  7.63896E-03 0.00027 -2.70283E-04 0.00129 -9.42456E-06 0.00505 -3.10751E-02 0.00017 ];
INF_SP7                   (idx, [1:   8]) = [  1.29311E-03 0.00143 -4.76652E-04 0.00070 -1.11779E-05 0.00379  1.07400E-02 0.00039 ];

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

