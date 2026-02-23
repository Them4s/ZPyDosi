
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
START_DATE                (idx, [1: 24])  = 'Fri Jan 16 07:54:09 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Sat Jan 17 03:17:38 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.21984E+00  1.00855E+00  9.94708E-01  9.91276E-01  9.92752E-01  9.85991E-01  9.91209E-01  9.93676E-01  9.87464E-01  9.87367E-01  9.97095E-01  9.96520E-01  9.93352E-01  1.00584E+00  9.93913E-01  9.95007E-01  9.88381E-01  9.85154E-01  9.87936E-01  9.91214E-01  9.99324E-01  9.92537E-01  1.00103E+00  9.94229E-01  9.97845E-01  9.82872E-01  9.87709E-01  9.85316E-01  9.72839E-01  9.99052E-01  ];
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
TOT_COL_EFF               (idx, [1:   4]) = [  9.80928E-01 9.8E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.54563E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.54472E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.66128E+00 0.00022  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.26915E+02 0.00025  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2067744017 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.44624E+05 0.00053 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.35774E+04 ;
RUNNING_TIME              (idx, 1)        =  1.16350E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.73017E-01  3.73017E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.78334E-03  9.78334E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.16311E+03  1.16311E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.16349E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85906 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88672E+01 3.1E-05 ];
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

NORM_COEF                 (idx, [1:   4]) = [  3.32873E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.15567E-01 0.00010 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.38977E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.10227E-02 0.00026 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.31478E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  9.96144E-01 3.2E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.05773E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.76768E-01 2.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82540E-01 9.5E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98618E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.31321E+01 3.1E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.74595E-02 0.00054 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.05825E+01 5.1E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.45493E+00 1.2E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02236E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  9.97481E-01 5.3E-05  9.90052E-01 5.1E-05  7.43299E-03 0.00075 ];
IMP_KEFF                  (idx, [1:   2]) = [  9.97419E-01 3.2E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  9.97528E-01 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  9.97419E-01 3.2E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.01517E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.06666E-03 0.00204  5.91872E-05 0.00908  2.98974E-04 0.00447  1.71593E-04 0.00570  3.86388E-04 0.00380  6.65132E-04 0.00318  2.27610E-04 0.00526  1.86016E-04 0.00609  7.17651E-05 0.00867 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.60547E-01 0.00076  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.52017E-03 0.00071  2.22525E-04 0.00416  1.08806E-03 0.00184  6.40363E-04 0.00240  1.42024E-03 0.00162  2.42518E-03 0.00124  8.03669E-04 0.00216  6.69443E-04 0.00236  2.50689E-04 0.00383 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.62782E-01 0.00109  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.81070E-05 0.00011  4.80856E-05 0.00011  5.09206E-05 0.00101 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.79850E-05 9.4E-05  4.79637E-05 9.4E-05  5.07912E-05 0.00101 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.45322E-03 0.00077  2.20953E-04 0.00440  1.07989E-03 0.00205  6.34041E-04 0.00260  1.40883E-03 0.00176  2.40213E-03 0.00134  7.95383E-04 0.00232  6.62872E-04 0.00261  2.49118E-04 0.00421 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.62790E-01 0.00120  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.73564E-05 0.00022  4.73335E-05 0.00022  5.03580E-05 0.00225 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.72363E-05 0.00021  4.72134E-05 0.00021  5.02309E-05 0.00225 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.59743E-03 0.00215  2.23925E-04 0.01262  1.09297E-03 0.00574  6.51428E-04 0.00754  1.43993E-03 0.00507  2.46864E-03 0.00383  8.05918E-04 0.00678  6.67871E-04 0.00739  2.46739E-04 0.01207 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.58375E-01 0.00337  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.59714E-03 0.00211  2.24968E-04 0.01244  1.09356E-03 0.00561  6.49970E-04 0.00737  1.44315E-03 0.00498  2.46480E-03 0.00376  8.07609E-04 0.00666  6.67427E-04 0.00724  2.45664E-04 0.01181 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.57737E-01 0.00330  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.60558E+02 0.00216 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.77317E-05 6.8E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.76107E-05 4.3E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.56543E-03 0.00043 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.58504E+02 0.00044 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.38433E-06 5.3E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.95872E-06 4.9E-05  1.95855E-06 4.9E-05  1.98077E-06 0.00055 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.23493E-05 7.6E-05  7.24084E-05 7.6E-05  6.45473E-05 0.00087 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.02706E-01 2.2E-05 -3.37082E-02 0.00188  2.45126E-04 0.00190 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.22291E+01 0.00112 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.01530E+00 5.6E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.69471E+01 4.5E-05  1.61851E+01 7.3E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.98539E-01 2.7E-05  2.58010E+00 3.1E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  5.03284E-03 8.7E-05  2.72566E-02 3.8E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.80422E-03 7.2E-05  4.93782E-02 6.6E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.77138E-03 6.8E-05  2.21217E-02 0.00011 ];
INF_NSF                   (idx, [1:   4]) = [  4.62789E-03 7.0E-05  5.38422E-02 0.00011 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.61260E+00 7.6E-06  2.43391E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04449E+02 7.4E-07  2.01942E+02 7.9E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.38135E-08 5.7E-05  3.58292E-06 1.4E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.91727E-01 2.7E-05  2.53072E+00 3.2E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.53451E-01 3.1E-05  5.21477E-01 3.4E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.38108E-01 3.6E-05  8.98310E-02 9.6E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.15634E-03 0.00031  2.37885E-02 0.00027 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.61564E-02 0.00017 -2.04820E-02 0.00028 ];
INF_SCATT5                (idx, [1:   4]) = [  5.10281E-05 0.04591  1.14221E-02 0.00046 ];
INF_SCATT6                (idx, [1:   4]) = [  7.31839E-03 0.00028 -3.10631E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.17878E-04 0.00233  1.07001E-02 0.00043 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.91784E-01 2.7E-05  2.53072E+00 3.2E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.53454E-01 3.1E-05  5.21477E-01 3.4E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.38109E-01 3.6E-05  8.98310E-02 9.6E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.15653E-03 0.00031  2.37885E-02 0.00027 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.61564E-02 0.00017 -2.04820E-02 0.00028 ];
INF_SCATTP5               (idx, [1:   4]) = [  5.10302E-05 0.04587  1.14221E-02 0.00046 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.31838E-03 0.00028 -3.10631E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.17880E-04 0.00233  1.07002E-02 0.00043 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.44373E-01 3.7E-05  1.73089E+00 3.9E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.36403E+00 3.7E-05  1.92579E-01 3.9E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.74786E-03 7.2E-05  4.93775E-02 6.6E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.66923E-02 4.0E-05  4.96007E-02 8.5E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  6.12817E-10 0.62287 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 6.6E-10  9.30086E-11 1.00000 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 5.0E-08  6.94588E-08 0.71483 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.61847E-01 2.7E-05  2.98805E-02 4.0E-05  2.27459E-04 0.00069  2.53050E+00 3.2E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.44684E-01 3.1E-05  8.76674E-03 7.5E-05  1.31047E-04 0.00090  5.21346E-01 3.4E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.41167E-01 3.6E-05 -3.05924E-03 0.00017  8.27639E-05 0.00109  8.97482E-02 9.6E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.25690E-02 0.00022 -3.41271E-03 0.00013  4.24440E-05 0.00152  2.37460E-02 0.00027 ];
INF_S4                    (idx, [1:   8]) = [ -1.53575E-02 0.00017 -7.98999E-04 0.00051  1.35118E-05 0.00421 -2.04955E-02 0.00028 ];
INF_S5                    (idx, [1:   8]) = [ -2.85795E-04 0.00817  3.36823E-04 0.00107 -2.68985E-06 0.01947  1.14248E-02 0.00046 ];
INF_S6                    (idx, [1:   8]) = [  7.58496E-03 0.00027 -2.66573E-04 0.00129 -9.51300E-06 0.00522 -3.10536E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.28859E-03 0.00145 -4.70713E-04 0.00067 -1.13111E-05 0.00406  1.07115E-02 0.00043 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.61903E-01 2.7E-05  2.98805E-02 4.0E-05  2.27459E-04 0.00069  2.53050E+00 3.2E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.44687E-01 3.1E-05  8.76674E-03 7.5E-05  1.31047E-04 0.00090  5.21346E-01 3.4E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.41168E-01 3.6E-05 -3.05924E-03 0.00017  8.27639E-05 0.00109  8.97482E-02 9.6E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.25692E-02 0.00022 -3.41271E-03 0.00013  4.24440E-05 0.00152  2.37460E-02 0.00027 ];
INF_SP4                   (idx, [1:   8]) = [ -1.53574E-02 0.00017 -7.98999E-04 0.00051  1.35118E-05 0.00421 -2.04955E-02 0.00028 ];
INF_SP5                   (idx, [1:   8]) = [ -2.85793E-04 0.00816  3.36824E-04 0.00107 -2.68986E-06 0.01947  1.14248E-02 0.00046 ];
INF_SP6                   (idx, [1:   8]) = [  7.58496E-03 0.00027 -2.66573E-04 0.00129 -9.51301E-06 0.00522 -3.10536E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.28859E-03 0.00145 -4.70713E-04 0.00067 -1.13110E-05 0.00406  1.07115E-02 0.00043 ];

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

