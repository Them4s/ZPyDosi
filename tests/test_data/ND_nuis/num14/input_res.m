
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
START_DATE                (idx, [1: 24])  = 'Tue Jan 20 10:00:33 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Wed Jan 21 05:29:17 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.21807E+00  1.00578E+00  9.88718E-01  9.96023E-01  9.89768E-01  9.98475E-01  9.91163E-01  9.94192E-01  1.00149E+00  9.92110E-01  9.92939E-01  9.98213E-01  9.94857E-01  9.89697E-01  9.89049E-01  9.95696E-01  9.98841E-01  9.85630E-01  9.92600E-01  9.84054E-01  9.92878E-01  9.78030E-01  9.96787E-01  9.91252E-01  9.92798E-01  9.91602E-01  9.86412E-01  9.82724E-01  9.96742E-01  9.93415E-01  ];
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
TOT_COL_EFF               (idx, [1:   4]) = [  9.80673E-01 9.5E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.53001E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.52906E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.68098E+00 0.00023  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.27295E+02 0.00024  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2071190838 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.45198E+05 0.00052 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00006E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.37263E+04 ;
RUNNING_TIME              (idx, 1)        =  1.16874E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.70517E-01  3.70517E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.36667E-03  9.36667E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.16836E+03  1.16836E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.16873E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85705 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88651E+01 3.1E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85801E-01 ;
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

NORM_COEF                 (idx, [1:   4]) = [  3.32925E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.17552E-01 0.00010 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.36813E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.31869E-02 0.00026 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.31319E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  9.85724E-01 3.2E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.05263E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.77177E-01 2.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82440E-01 9.3E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98774E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.31998E+01 3.0E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75598E-02 0.00052 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.04711E+01 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.43231E+00 1.3E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02247E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  9.86938E-01 5.4E-05  9.79509E-01 5.1E-05  7.43933E-03 0.00074 ];
IMP_KEFF                  (idx, [1:   2]) = [  9.86994E-01 3.2E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  9.86940E-01 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  9.86994E-01 3.2E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.00466E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.08583E-03 0.00189  6.01300E-05 0.00914  3.02367E-04 0.00409  1.70286E-04 0.00495  3.88010E-04 0.00356  6.73187E-04 0.00287  2.29702E-04 0.00476  1.87544E-04 0.00560  7.46015E-05 0.01005 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.61421E-01 0.00075  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.61449E-03 0.00070  2.27266E-04 0.00400  1.09979E-03 0.00183  6.44670E-04 0.00238  1.43272E-03 0.00159  2.45948E-03 0.00122  8.18468E-04 0.00215  6.75434E-04 0.00235  2.56656E-04 0.00384 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.64003E-01 0.00109  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.83974E-05 0.00011  4.83744E-05 0.00011  5.14028E-05 0.00098 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.77644E-05 9.4E-05  4.77416E-05 9.4E-05  5.07305E-05 0.00098 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.53860E-03 0.00076  2.24063E-04 0.00434  1.09147E-03 0.00200  6.36989E-04 0.00261  1.41790E-03 0.00172  2.43443E-03 0.00130  8.12745E-04 0.00231  6.67657E-04 0.00254  2.53345E-04 0.00416 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.63563E-01 0.00117  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.76624E-05 0.00022  4.76410E-05 0.00022  5.04034E-05 0.00223 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.70390E-05 0.00021  4.70178E-05 0.00021  4.97444E-05 0.00223 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.68667E-03 0.00215  2.34166E-04 0.01237  1.11213E-03 0.00563  6.58450E-04 0.00737  1.45275E-03 0.00499  2.48120E-03 0.00382  8.20496E-04 0.00681  6.79775E-04 0.00723  2.47704E-04 0.01208 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.57433E-01 0.00333  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.68348E-03 0.00210  2.35210E-04 0.01228  1.11183E-03 0.00553  6.58171E-04 0.00726  1.45202E-03 0.00490  2.48118E-03 0.00376  8.19136E-04 0.00668  6.79625E-04 0.00705  2.46307E-04 0.01183 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.56861E-01 0.00327  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.61390E+02 0.00216 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.80343E-05 6.9E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.74060E-05 4.2E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.63920E-03 0.00043 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.59041E+02 0.00043 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.37430E-06 5.3E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96013E-06 4.8E-05  1.95996E-06 4.8E-05  1.98132E-06 0.00056 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.20214E-05 7.5E-05  7.20810E-05 7.6E-05  6.42783E-05 0.00085 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.01537E-01 2.1E-05 -3.32976E-02 0.00179  2.45817E-04 0.00181 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21720E+01 0.00111 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.00455E+00 5.7E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.71023E+01 4.3E-05  1.60977E+01 6.8E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.96806E-01 2.8E-05  2.58338E+00 3.1E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  5.02716E-03 7.9E-05  2.73911E-02 3.4E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.80520E-03 6.5E-05  4.95730E-02 6.2E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.77805E-03 6.2E-05  2.21819E-02 0.00010 ];
INF_NSF                   (idx, [1:   4]) = [  4.64184E-03 6.4E-05  5.34193E-02 0.00010 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.61064E+00 7.8E-06  2.40824E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04510E+02 7.1E-07  2.01942E+02 7.6E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.34249E-08 5.1E-05  3.58134E-06 1.4E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.89990E-01 2.8E-05  2.53380E+00 3.2E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.51121E-01 3.2E-05  5.21591E-01 3.4E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.37287E-01 3.8E-05  8.98829E-02 9.3E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.15208E-03 0.00031  2.37935E-02 0.00028 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.59994E-02 0.00016 -2.04636E-02 0.00029 ];
INF_SCATT5                (idx, [1:   4]) = [  6.16486E-05 0.03560  1.14116E-02 0.00044 ];
INF_SCATT6                (idx, [1:   4]) = [  7.26640E-03 0.00028 -3.10423E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.13612E-04 0.00239  1.06839E-02 0.00040 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.90047E-01 2.8E-05  2.53380E+00 3.2E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.51123E-01 3.2E-05  5.21591E-01 3.4E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.37288E-01 3.8E-05  8.98829E-02 9.3E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.15229E-03 0.00031  2.37935E-02 0.00028 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.59994E-02 0.00016 -2.04636E-02 0.00029 ];
INF_SCATTP5               (idx, [1:   4]) = [  6.16648E-05 0.03560  1.14116E-02 0.00044 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.26647E-03 0.00028 -3.10423E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.13611E-04 0.00239  1.06839E-02 0.00040 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.44785E-01 3.8E-05  1.73461E+00 3.8E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.36174E+00 3.8E-05  1.92166E-01 3.8E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.74864E-03 6.6E-05  4.95723E-02 6.2E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.64871E-02 4.3E-05  4.98078E-02 7.8E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  2.48385E-10 0.82511 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 2.7E-08  3.29801E-08 0.83128 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.60319E-01 2.8E-05  2.96716E-02 3.8E-05  2.29756E-04 0.00068  2.53357E+00 3.2E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.42424E-01 3.2E-05  8.69692E-03 7.6E-05  1.31820E-04 0.00090  5.21459E-01 3.4E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.40322E-01 3.8E-05 -3.03498E-03 0.00017  8.31142E-05 0.00105  8.97998E-02 9.3E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.25380E-02 0.00022 -3.38590E-03 0.00013  4.26863E-05 0.00163  2.37508E-02 0.00028 ];
INF_S4                    (idx, [1:   8]) = [ -1.52056E-02 0.00016 -7.93851E-04 0.00048  1.36659E-05 0.00452 -2.04773E-02 0.00029 ];
INF_S5                    (idx, [1:   8]) = [ -2.71478E-04 0.00809  3.33127E-04 0.00110 -2.51476E-06 0.02105  1.14141E-02 0.00044 ];
INF_S6                    (idx, [1:   8]) = [  7.53092E-03 0.00027 -2.64513E-04 0.00124 -9.44343E-06 0.00497 -3.10329E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.28026E-03 0.00147 -4.66652E-04 0.00064 -1.12622E-05 0.00405  1.06952E-02 0.00040 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.60375E-01 2.8E-05  2.96716E-02 3.8E-05  2.29757E-04 0.00068  2.53357E+00 3.2E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.42426E-01 3.2E-05  8.69693E-03 7.6E-05  1.31820E-04 0.00090  5.21459E-01 3.4E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.40323E-01 3.8E-05 -3.03498E-03 0.00017  8.31141E-05 0.00105  8.97998E-02 9.3E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.25382E-02 0.00022 -3.38590E-03 0.00013  4.26863E-05 0.00163  2.37508E-02 0.00028 ];
INF_SP4                   (idx, [1:   8]) = [ -1.52056E-02 0.00016 -7.93851E-04 0.00048  1.36659E-05 0.00452 -2.04773E-02 0.00029 ];
INF_SP5                   (idx, [1:   8]) = [ -2.71462E-04 0.00809  3.33127E-04 0.00110 -2.51475E-06 0.02105  1.14141E-02 0.00044 ];
INF_SP6                   (idx, [1:   8]) = [  7.53099E-03 0.00027 -2.64513E-04 0.00124 -9.44342E-06 0.00497 -3.10329E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.28026E-03 0.00148 -4.66652E-04 0.00064 -1.12622E-05 0.00405  1.06952E-02 0.00040 ];

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

