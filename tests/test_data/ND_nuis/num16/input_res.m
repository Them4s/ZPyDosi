
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
START_DATE                (idx, [1: 24])  = 'Wed Jan 21 05:29:20 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Jan 22 01:00:31 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.22027E+00  1.00483E+00  9.97810E-01  9.88934E-01  9.89336E-01  9.88581E-01  1.00295E+00  9.94819E-01  9.98669E-01  9.97044E-01  9.88598E-01  9.99624E-01  9.95695E-01  9.92582E-01  9.82265E-01  9.91053E-01  9.82131E-01  9.87400E-01  9.99467E-01  9.92577E-01  9.99061E-01  9.91918E-01  9.98308E-01  9.92040E-01  9.86819E-01  9.75159E-01  9.89910E-01  9.95340E-01  9.89484E-01  9.87323E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 71])  = '/home/thomasligonnet/Documents/XS/xs_lib/jeff33_modif_eurofusion/xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1:  3])  = 'N/A' ;
SFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
NFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  2.95583E-01 1.1E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  0.00000E+00  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TMS_SAMPLING_EFF          (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  9.80849E-01 1.0E-06  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.45516E+01 0.00023  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.45424E+01 0.00023  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.65061E+00 0.00022  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.26251E+02 0.00025  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2100163159 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.50027E+05 0.00058 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.37850E+04 ;
RUNNING_TIME              (idx, 1)        =  1.17119E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.71550E-01  3.71550E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.33333E-03  9.33333E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.17080E+03  1.17080E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.17118E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.84686 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88549E+01 3.4E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85744E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.23 ;

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

NORM_COEF                 (idx, [1:   4]) = [  3.32908E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.18233E-01 9.9E-05 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.37945E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.20550E-02 0.00025 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.32044E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  9.97795E-01 3.2E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.07511E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.75111E-01 2.4E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82623E-01 9.5E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98725E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.30684E+01 3.1E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.73774E-02 0.00054 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.02139E+01 5.1E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.44851E+00 1.2E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02241E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  9.99027E-01 5.3E-05  9.91563E-01 5.0E-05  7.46688E-03 0.00073 ];
IMP_KEFF                  (idx, [1:   2]) = [  9.99066E-01 3.2E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  9.99075E-01 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  9.99066E-01 3.2E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.01676E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.02418E-03 0.00208  5.85879E-05 0.00907  2.91736E-04 0.00450  1.65886E-04 0.00561  3.77206E-04 0.00403  6.53968E-04 0.00310  2.22540E-04 0.00499  1.82207E-04 0.00536  7.20446E-05 0.00956 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.61215E-01 0.00076  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.54901E-03 0.00068  2.24950E-04 0.00405  1.08962E-03 0.00179  6.38729E-04 0.00235  1.42102E-03 0.00160  2.44163E-03 0.00122  8.08635E-04 0.00211  6.70550E-04 0.00232  2.53875E-04 0.00383 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.63825E-01 0.00108  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.78425E-05 0.00011  4.78201E-05 0.00011  5.07885E-05 0.00100 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.77952E-05 9.3E-05  4.77728E-05 9.3E-05  5.07381E-05 0.00099 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.47114E-03 0.00074  2.21348E-04 0.00441  1.07663E-03 0.00198  6.32701E-04 0.00257  1.40865E-03 0.00173  2.41484E-03 0.00134  8.01360E-04 0.00234  6.64745E-04 0.00255  2.50858E-04 0.00418 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.63920E-01 0.00118  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.71331E-05 0.00021  4.71117E-05 0.00022  4.99235E-05 0.00216 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.70864E-05 0.00021  4.70650E-05 0.00021  4.98744E-05 0.00216 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.58877E-03 0.00214  2.24613E-04 0.01245  1.09951E-03 0.00571  6.51543E-04 0.00720  1.43113E-03 0.00497  2.46185E-03 0.00373  8.04110E-04 0.00658  6.70057E-04 0.00728  2.45958E-04 0.01201 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.57862E-01 0.00339  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.58609E-03 0.00209  2.25116E-04 0.01224  1.09731E-03 0.00561  6.50950E-04 0.00706  1.43138E-03 0.00487  2.46007E-03 0.00365  8.05327E-04 0.00642  6.70898E-04 0.00710  2.45046E-04 0.01173 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.57986E-01 0.00331  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.61123E+02 0.00215 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.74951E-05 6.6E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.74481E-05 4.1E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.57503E-03 0.00041 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.59495E+02 0.00042 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.37205E-06 5.3E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96311E-06 4.8E-05  1.96297E-06 4.8E-05  1.98213E-06 0.00053 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.15633E-05 7.7E-05  7.16197E-05 7.7E-05  6.41496E-05 0.00084 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.02772E-01 2.1E-05 -3.43230E-02 0.00189  2.50674E-04 0.00191 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21718E+01 0.00110 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.01679E+00 5.3E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.70372E+01 4.4E-05  1.60314E+01 6.6E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.98891E-01 2.8E-05  2.57734E+00 3.1E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  5.00147E-03 8.1E-05  2.74393E-02 3.4E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.78044E-03 6.5E-05  4.98588E-02 5.9E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.77897E-03 6.0E-05  2.24195E-02 9.5E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.66551E-03 6.2E-05  5.43721E-02 9.5E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.62259E+00 7.6E-06  2.42521E+00 2.6E-09 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04480E+02 7.2E-07  2.01942E+02 8.4E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.37359E-08 5.2E-05  3.57857E-06 1.4E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.92102E-01 2.8E-05  2.52748E+00 3.2E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.51343E-01 3.1E-05  5.20469E-01 3.7E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.37229E-01 3.9E-05  8.97795E-02 9.1E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.04416E-03 0.00032  2.37750E-02 0.00028 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.61050E-02 0.00014 -2.03897E-02 0.00027 ];
INF_SCATT5                (idx, [1:   4]) = [  2.05792E-05 0.10213  1.13783E-02 0.00044 ];
INF_SCATT6                (idx, [1:   4]) = [  7.25746E-03 0.00028 -3.09355E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.04460E-04 0.00227  1.06417E-02 0.00045 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.92158E-01 2.8E-05  2.52748E+00 3.2E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.51346E-01 3.1E-05  5.20469E-01 3.7E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.37230E-01 3.9E-05  8.97795E-02 9.1E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.04436E-03 0.00032  2.37750E-02 0.00028 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.61049E-02 0.00014 -2.03897E-02 0.00027 ];
INF_SCATTP5               (idx, [1:   4]) = [  2.06441E-05 0.10184  1.13783E-02 0.00044 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.25751E-03 0.00028 -3.09355E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.04446E-04 0.00227  1.06417E-02 0.00045 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.47107E-01 3.8E-05  1.73065E+00 3.9E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.34895E+00 3.8E-05  1.92606E-01 3.9E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.72421E-03 6.6E-05  4.98581E-02 5.9E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.65768E-02 4.2E-05  5.00892E-02 7.5E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 1.3E-09  1.24779E-09 0.58177 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 6.6E-10  6.75547E-10 1.00000 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 4.0E-08  7.94811E-08 0.49937 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.62314E-01 2.8E-05  2.97876E-02 3.8E-05  2.31361E-04 0.00068  2.52725E+00 3.2E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.42612E-01 3.1E-05  8.73078E-03 7.8E-05  1.32366E-04 0.00088  5.20337E-01 3.7E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.40275E-01 3.8E-05 -3.04637E-03 0.00017  8.34076E-05 0.00108  8.96961E-02 9.1E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24437E-02 0.00023 -3.39958E-03 0.00012  4.27595E-05 0.00160  2.37322E-02 0.00028 ];
INF_S4                    (idx, [1:   8]) = [ -1.53085E-02 0.00015 -7.96492E-04 0.00051  1.36601E-05 0.00425 -2.04034E-02 0.00027 ];
INF_S5                    (idx, [1:   8]) = [ -3.14074E-04 0.00665  3.34653E-04 0.00102 -2.62431E-06 0.01980  1.13810E-02 0.00044 ];
INF_S6                    (idx, [1:   8]) = [  7.52369E-03 0.00027 -2.66222E-04 0.00118 -9.49452E-06 0.00530 -3.09260E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.27335E-03 0.00143 -4.68886E-04 0.00065 -1.13191E-05 0.00394  1.06531E-02 0.00045 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.62370E-01 2.8E-05  2.97876E-02 3.8E-05  2.31362E-04 0.00068  2.52725E+00 3.2E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.42615E-01 3.1E-05  8.73078E-03 7.8E-05  1.32366E-04 0.00088  5.20337E-01 3.7E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.40277E-01 3.8E-05 -3.04637E-03 0.00017  8.34076E-05 0.00108  8.96961E-02 9.1E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24439E-02 0.00023 -3.39958E-03 0.00012  4.27595E-05 0.00160  2.37322E-02 0.00028 ];
INF_SP4                   (idx, [1:   8]) = [ -1.53084E-02 0.00015 -7.96493E-04 0.00051  1.36601E-05 0.00425 -2.04034E-02 0.00027 ];
INF_SP5                   (idx, [1:   8]) = [ -3.14009E-04 0.00665  3.34653E-04 0.00102 -2.62432E-06 0.01980  1.13810E-02 0.00044 ];
INF_SP6                   (idx, [1:   8]) = [  7.52373E-03 0.00027 -2.66222E-04 0.00118 -9.49452E-06 0.00530 -3.09260E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.27333E-03 0.00143 -4.68886E-04 0.00065 -1.13191E-05 0.00394  1.06531E-02 0.00045 ];

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

